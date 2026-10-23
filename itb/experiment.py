"""Plan and execute bursts into chosen leaders' windows.

A *burst* = K probe transactions with K distinct CU prices, sent directly to
one leader's advertised TPU-QUIC address, in a random order that is
independent of price, with a fixed gap between sends. Arms (all recorded):
  payer   independent : K different fee payers -> no account-lock conflicts
          shared      : 1 fee payer for all K  -> every pair conflicts (payer write lock)
  timing  pre         : sent while the slot clock shows (first_slot - lead) -> buffered before the window opens
          mid         : sent while the slot clock shows first_slot + 1     -> competes with live flow mid-window
DRY-RUN (default): everything is built, signed, timed and the QUIC handshake
to the target TPU is performed, but no transaction byte is written.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import random
import time
from dataclasses import dataclass, field

from solders.hash import Hash
from solders.keypair import Keypair
from solders.pubkey import Pubkey

from . import ALPENGLOW_FIRST_SLOT
from .budget import SpendCap
from .cluster import snapshot
from .quic_sender import TpuQuicSender
from .rpc import Rpc
from .slots import SlotClock
from .txbuild import build_probe, build_transfers, fee_ladder, max_fee, memo_tag

log = logging.getLogger("itb.exp")
RENT_EXEMPT_MIN = 890_880  # 0-data system account


@dataclass
class Config:
    data_dir: str
    live: bool = False
    max_spend_sol: float = 0.05
    k: int = 8
    cu_limit: int = 20_000
    price_lo: int = 1_000
    price_hi: int = 200_000
    lead_slots: int = 2  # 2 x ~200 ms slots ahead (slot time is 200 ms since epoch 1053, SIMD-0525)
    bursts_per_validator: int = 6
    validators_per_client: int = 2
    min_clients: int = 3
    clients: list[str] = field(default_factory=lambda: [
        "Agave", "JitoLabs", "AgaveBam", "HarmonicAgave", "Firedancer", "HarmonicFiredancer", "FireBAM", "Rakurai"])
    min_stake_sol: float = 50_000
    horizon_slots: int = 20_000
    # payer:timing:gap_ms - cycled over each validator's windows
    arms: list[str] = field(default_factory=lambda: ["shared:pre:0", "independent:pre:0", "shared:mid:0",
                                                     "independent:mid:3", "shared:pre:3", "independent:mid:0"])
    seed: int | None = None
    use_memo: bool = True
    run_id: str | None = None
    localnet: bool = False  # solana-test-validator: one node, no stake/client/Alpenglow checks


def load_keypair(path_or_env: str | None) -> Keypair | None:
    raw = os.environ.get("ITB_PAYER_KEYPAIR_JSON")
    if raw:
        return Keypair.from_bytes(bytes(json.loads(raw)))
    if path_or_env and os.path.exists(path_or_env):
        return Keypair.from_bytes(bytes(json.load(open(path_or_env))))
    return None


def _arm(spec: str) -> dict:
    payer_mode, timing, gap = (spec.split(":") + ["3"])[:3]
    assert payer_mode in ("independent", "shared") and timing in ("pre", "mid")
    return {"payer_mode": payer_mode, "timing": timing, "gap_ms": float(gap)}


async def plan(rpc: Rpc, cfg: Config, snap: dict) -> list[dict]:
    tip = await rpc.call("getSlot", [{"commitment": "processed"}])
    if cfg.localnet:
        ident = next(iter(snap["nodes"]))
        n = snap["nodes"][ident]
        base = tip + 20 - (tip + 20) % 4
        return [{"burst": i, "validator": ident, "client": n["client"], "version": n["version"], "stake_sol": 0,
                 "tpu_quic": n["tpu_quic"], "window_first_slot": base + 16 * i,
                 **_arm(cfg.arms[i % len(cfg.arms)])} for i in range(cfg.bursts_per_validator)]
    if tip < ALPENGLOW_FIRST_SLOT:
        raise RuntimeError("pre-Alpenglow slot; this campaign measures post-Alpenglow only")
    start = tip + 40  # leave time for setup
    leaders = []
    s = start - (start % 4)
    while len(leaders) < cfg.horizon_slots:
        leaders += await rpc.call("getSlotLeaders", [s + len(leaders), min(5000, cfg.horizon_slots - len(leaders))])
    windows = {}
    for i in range(0, len(leaders) - 3, 4):
        if len(set(leaders[i:i + 4])) == 1:  # full 4-slot window
            windows.setdefault(leaders[i], []).append(s + i)
    nodes = snap["nodes"]
    by_client: dict[str, list[tuple[int, str]]] = {}
    for ident, wins in windows.items():
        n = nodes.get(ident)
        if not n or not n["tpu_quic"] or n["stake"] < cfg.min_stake_sol * 1e9:
            continue
        if n["client"] in cfg.clients:
            by_client.setdefault(n["client"], []).append((len(wins), ident))
    rnd = random.Random(cfg.seed)
    chosen = []
    for client in cfg.clients:
        cand = by_client.get(client, [])
        # prefer validators with enough windows in the horizon for all arms, then random
        cand = [c for c in cand if c[0] >= cfg.bursts_per_validator] or cand
        rnd.shuffle(cand)
        chosen += [(client, ident) for _, ident in cand[: cfg.validators_per_client]]
    if len({c for c, _ in chosen}) < cfg.min_clients or len(chosen) < 6:
        raise RuntimeError(f"not enough validators/clients with windows in horizon: {chosen}")
    bursts = []
    for client, ident in chosen:
        for j, w in enumerate(windows[ident][: cfg.bursts_per_validator]):
            bursts.append({**_arm(cfg.arms[j % len(cfg.arms)]), "validator": ident, "client": client, "version": nodes[ident]["version"],
                           "stake_sol": nodes[ident]["stake"] / 1e9, "tpu_quic": nodes[ident]["tpu_quic"],
                           "tpu_proxied": nodes[ident].get("tpu_proxied"),
                           "window_first_slot": w})
    bursts.sort(key=lambda b: b["window_first_slot"])
    # drop bursts whose send moments are closer than ~6 s (we serialize bursts)
    out, last = [], -10**9
    for b in bursts:
        if b["window_first_slot"] - last >= 16:
            out.append(b)
            last = b["window_first_slot"]
    for i, b in enumerate(out):
        b["burst"] = i
    return out


async def run(cfg: Config, rpc: Rpc, payer_path: str | None = None) -> str:
    run_id = cfg.run_id or time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    rdir = os.path.join(cfg.data_dir, "runs", run_id)
    os.makedirs(rdir, exist_ok=True)
    mode = "LIVE" if cfg.live else "DRY-RUN"
    seed = cfg.seed if cfg.seed is not None else int(time.time())
    rnd = random.Random(seed)
    log.info("run %s mode=%s seed=%s rpc=%s", run_id, mode, seed, rpc.redacted_url)

    snap = await snapshot(rpc)
    json.dump(snap, open(os.path.join(rdir, "cluster_snapshot.json"), "w"))
    bursts = await plan(rpc, cfg, snap)
    ladder = fee_ladder(cfg.k, cfg.price_lo, cfg.price_hi)
    worst_burst = cfg.k * max_fee(cfg.cu_limit, max(ladder))

    master = load_keypair(payer_path)
    if cfg.live and master is None:
        raise RuntimeError("live mode needs a payer keypair (volume /keys/payer.json or ITB_PAYER_KEYPAIR_JSON)")
    cap = SpendCap(cfg.max_spend_sol, os.path.join(cfg.data_dir, "spend_ledger.jsonl")) if cfg.live else None
    # campaign budget check up-front: probes + funding tx + K sweep txs
    need = len(bursts) * worst_burst + max_fee(5000, 0) + cfg.k * max_fee(1000, 0)
    meta = {"run_id": run_id, "mode": mode, "seed": seed, "config": cfg.__dict__, "ladder_micro_lamports_per_cu": ladder,
            "worst_case_fee_lamports": need, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "n_bursts": len(bursts), "rpc": rpc.redacted_url}
    if cap and need > cap.remaining:
        raise RuntimeError(f"planned worst case {need} lamports > remaining cap {cap.remaining}; reduce bursts")
    json.dump(meta, open(os.path.join(rdir, "meta.json"), "w"), indent=1, default=str)
    json.dump(bursts, open(os.path.join(rdir, "plan.json"), "w"), indent=1)
    log.info("planned %d bursts over %d validators; worst-case fees %.6f SOL", len(bursts),
             len({b['validator'] for b in bursts}), need / 1e9)

    # fee payers: K ephemeral keys (saved in the run dir so funds are recoverable after a crash)
    eph = [Keypair() for _ in range(cfg.k)]
    if cfg.live:
        json.dump([list(bytes(k)) for k in eph], open(os.path.join(rdir, "ephemeral_keys.SECRET.json"), "w"))
        per_payer = RENT_EXEMPT_MIN + 2 * max_fee(1000, 0) + len(bursts) * max_fee(cfg.cu_limit, max(ladder))
        per_payer += len(bursts) * max_fee(cfg.cu_limit, max(ladder)) * cfg.k  # shared-payer arm uses payer 0
        bh = Hash.from_string((await rpc.call("getLatestBlockhash", [{"commitment": "confirmed"}]))["value"]["blockhash"])
        fund = build_transfers(master, bh, [(k.pubkey(), per_payer) for k in eph])
        cap.reserve(max_fee(5000, 0), "fund", [str(fund.signatures[0])])
        sig = await rpc.call("sendTransaction", [__import__("base64").b64encode(bytes(fund)).decode(),
                                                 {"encoding": "base64", "skipPreflight": False, "preflightCommitment": "confirmed"}])
        log.info("funding %d payers x %d lamports: %s", cfg.k, per_payer, sig)
        await _confirm(rpc, [sig])
    else:
        log.info("dry-run: ephemeral payers generated, NOT funded; nothing will be sent")

    clock = SlotClock(rpc)
    await clock.start()
    sent_path = os.path.join(rdir, "sends.jsonl")
    try:
        for b in bursts:
            try:
                rec = await _burst(cfg, rpc, clock, b, eph, ladder, rnd, run_id, cap)
            except Exception as e:  # one bad burst must not end the campaign (and must not skip the sweep)
                log.exception("burst %d failed", b["burst"])
                rec = dict(b, status=f"error: {e!r}"[:200])
            with open(sent_path, "a") as f:
                f.write(json.dumps(rec) + "\n")
    finally:
        await clock.stop()
        if cfg.live:
            await _sweep(rpc, eph, master.pubkey(), cap, rdir)
    meta["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    json.dump(meta, open(os.path.join(rdir, "meta.json"), "w"), indent=1, default=str)
    return rdir


async def _burst(cfg, rpc, clock, b, eph, ladder, rnd, run_id, cap):
    first = b["window_first_slot"]
    trigger = first - cfg.lead_slots if b["timing"] == "pre" else first + 1
    rec = dict(b)
    rec.update({"trigger_slot": trigger, "status": "pending"})
    if clock.slot >= trigger - 6:
        rec["status"] = "missed_trigger_before_start"
        return rec
    # ~8 slots (~1.6 s) ahead: fresh blockhash, build + sign, QUIC handshake
    await clock.wait_for(trigger - 8)
    bh = Hash.from_string((await rpc.call("getLatestBlockhash", [{"commitment": "processed"}]))["value"]["blockhash"])
    prices = ladder[:]
    rnd.shuffle(prices)  # send position k gets prices[k]: independent of price rank by construction
    txs = []
    for k in range(cfg.k):
        payer = eph[k] if b["payer_mode"] == "independent" else eph[0]
        tx = build_probe(payer, bh, cfg.cu_limit, prices[k], memo_tag(run_id[-8:], b["burst"], k), cfg.use_memo)
        txs.append({"send_rank": k, "cu_price": prices[k], "sig": str(tx.signatures[0]), "payer": str(payer.pubkey()),
                    "wire": bytes(tx)})
    if cap:
        cap.reserve(sum(max_fee(cfg.cu_limit, t["cu_price"]) for t in txs), f"burst{b['burst']}", [t["sig"] for t in txs])
    host, port = b["tpu_quic"].rsplit(":", 1)
    rec["blockhash"] = str(bh)
    try:
        async with TpuQuicSender(host, int(port)) as conn:
            rec["quic_connect_ms"] = conn.connect_ms
            await clock.wait_for(trigger)
            rec["slot_at_send"] = clock.slot
            rec["ms_since_slot_update"] = (time.monotonic() - clock.t) * 1e3
            rec["slot_clock_source"] = clock.source
            latest_ok = first - 1 if b["timing"] == "pre" else first + 2
            if clock.slot > latest_ok:  # clock hiccup (e.g. websocket reconnect): never send outside the arm
                rec["status"] = f"late_trigger_skipped (clock at {clock.slot})"
                for t in txs:
                    t.pop("wire")
                rec["txs"] = txs
                log.warning("burst %d skipped: late trigger %d > %d", b["burst"], clock.slot, latest_ok)
                return rec
            for t in txs:
                if cfg.live:
                    r = conn.send(t["send_rank"], t["wire"])
                    t.update({"t_send_ns": r.t_send_ns, "send_ok": r.ok, "send_err": r.err})
                else:
                    t.update({"t_send_ns": time.time_ns(), "send_ok": None, "send_err": "dry-run"})
                if b["gap_ms"] > 0:
                    await asyncio.sleep(b["gap_ms"] / 1000)
            await asyncio.sleep(0.3)  # let QUIC flush
            rec["status"] = "sent" if cfg.live else "dry_run"
    except Exception as e:
        rec["status"] = f"connect_or_send_failed: {e!r}"[:200]
    for t in txs:
        t.pop("wire")
    rec["txs"] = txs
    rec["slot_ms_estimate"] = clock.ms_per_slot()
    log.info("burst %d %s/%s %s:%s window=%d trigger=%d at=%s %s", b["burst"], b["client"], b["version"],
             b["payer_mode"], b["timing"], first, trigger, rec.get("slot_at_send"), rec["status"])
    return rec


async def _confirm(rpc, sigs, timeout=60):
    end = time.time() + timeout
    while time.time() < end:
        st = (await rpc.call("getSignatureStatuses", [sigs]))["value"]
        if all(s and s.get("confirmationStatus") in ("confirmed", "finalized") for s in st):
            return st
        await asyncio.sleep(1)
    raise TimeoutError("not confirmed")


async def _sweep(rpc, eph, dest: Pubkey, cap, rdir):
    """Return every ephemeral payer's balance to the operator wallet.

    First wait until the last probe blockhash has expired, so no in-flight
    probe can still debit a payer after we computed its balance."""
    import base64
    last_bh = None
    sp = os.path.join(rdir, "sends.jsonl")
    if os.path.exists(sp):
        lines = open(sp).read().splitlines()
        last_bh = json.loads(lines[-1]).get("blockhash") if lines else None
    for _ in range(40):
        if not last_bh:
            break
        ok = (await rpc.call("isBlockhashValid", [last_bh, {"commitment": "processed"}]))["value"]
        if not ok:
            break
        await asyncio.sleep(5)
    out = []
    for k in eph:
        bal = await rpc.call("getBalance", [str(k.pubkey()), {"commitment": "confirmed"}])
        amt = bal["value"] - max_fee(1000, 0)
        if amt <= 0:
            continue
        bh = Hash.from_string((await rpc.call("getLatestBlockhash", [{"commitment": "confirmed"}]))["value"]["blockhash"])
        tx = build_transfers(k, bh, [(dest, amt)])
        cap.reserve(max_fee(1000, 0), "sweep", [str(tx.signatures[0])])
        try:
            sig = await rpc.call("sendTransaction", [base64.b64encode(bytes(tx)).decode(), {"encoding": "base64", "preflightCommitment": "confirmed"}])
            out.append(sig)
        except Exception as e:
            log.error("sweep failed for %s: %s (key kept in ephemeral_keys.SECRET.json)", k.pubkey(), e)
    json.dump(out, open(os.path.join(rdir, "sweep_sigs.json"), "w"))
