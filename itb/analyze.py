"""Burst- and validator-level ordering statistics + plots + markdown tables."""
from __future__ import annotations

import collections
import json
import os

import numpy as np

from .stats import bootstrap_ci, concordant_fraction, kendall, sign_test_p


def burst_stats(r: dict) -> dict:
    land = [t for t in r.get("txs", []) if t.get("index_in_block") is not None]
    out = {"burst": r["burst"], "validator": r["validator"], "client": r["client"], "version": r["version"],
           "payer_mode": r["payer_mode"], "timing": r["timing"], "gap_ms": r.get("gap_ms"), "status": r["status"],
           "n_sent": sum(1 for t in r.get("txs", []) if t.get("send_ok")), "n_landed": len(land)}
    if not land:
        return out
    win = set(range(r["window_first_slot"], r["window_first_slot"] + 4))
    out["landed_in_target_window"] = sum(1 for t in land if t["landed_slot"] in win)
    first_t = min(land, key=lambda t: (t["landed_slot"], t["index_in_block"]))
    out["landed_offset_slots"] = first_t["landed_slot"] - r["window_first_slot"]
    out["producer"] = first_t.get("landed_leader")
    out["producer_is_target"] = out["producer"] == r["validator"] if out["producer"] else None
    out["n_producers"] = len({t.get("landed_leader") for t in land})
    out["n_slots_used"] = len({t["landed_slot"] for t in land})
    # global position across slots: (slot, index)
    order = sorted(land, key=lambda t: (t["landed_slot"], t["index_in_block"]))
    pos = {t["sig"]: i for i, t in enumerate(order)}
    p = [pos[t["sig"]] for t in land]
    price = [t["cu_price"] for t in land]
    send = [t["send_rank"] for t in land]
    out["tau_fee"] = kendall(p, [-x for x in price])  # +1: strictly highest fee first
    out["tau_send"] = kendall(p, send)  # +1: strictly first-sent first
    out["conc_fee"] = concordant_fraction(p, price)
    out["conc_send"] = concordant_fraction(p, [-x for x in send])
    same = [t for t in land if t["landed_slot"] == order[0]["landed_slot"]]
    idx = sorted(t["index_in_block"] for t in same)
    out["span_in_block"] = idx[-1] - idx[0] + 1 if idx else None  # 8 => contiguous
    out["foreign_between"] = (idx[-1] - idx[0] + 1 - len(idx)) if idx else None
    out["first_index"] = idx[0] if idx else None
    out["block_n_tx"] = same[0]["block_n_tx"] if same else None
    return out


def verdict(rows: list[dict]) -> str:
    tf = [r["tau_fee"] for r in rows if r.get("tau_fee") is not None]
    ts = [r["tau_send"] for r in rows if r.get("tau_send") is not None]
    if len(tf) < 2:
        return "insufficient data"
    cf, cs = bootstrap_ci(tf), bootstrap_ci(ts)
    if cf and cf[0] > 0.3 and (not cs or cs[0] <= 0.3):
        strict = np.mean([x >= 0.999 for x in tf])
        return f"fee-priority ({strict:.0%} of bursts perfectly fee-sorted)"
    if cs and cs[0] > 0.3 and (not cf or cf[0] <= 0.3):
        strict = np.mean([x >= 0.999 for x in ts])
        return f"arrival order / FIFO ({strict:.0%} of bursts perfectly send-ordered)"
    if cf and cs and cf[0] > 0.3 and cs[0] > 0.3:
        return "mixed (both fee and arrival matter)"
    return "no rule detected (consistent with noise at this n)"


def analyze(rdir: str) -> dict:
    recs = [json.loads(l) for l in open(os.path.join(rdir, "landed.jsonl"))]
    bs = [burst_stats(r) for r in recs]
    groups = collections.defaultdict(list)
    for b in bs:
        groups[(b["client"], b["version"], b["validator"])].append(b)
    per_val = []
    for (c, v, ident), rows in sorted(groups.items()):
        for arm in sorted({(r["payer_mode"], r["timing"], str(r["gap_ms"])) for r in rows}) + [("all", "all", "")]:
            sub = rows if arm[0] == "all" else [r for r in rows if (r["payer_mode"], r["timing"], str(r["gap_ms"])) == arm]
            tf = [r["tau_fee"] for r in sub if r.get("tau_fee") is not None]
            ts = [r["tau_send"] for r in sub if r.get("tau_send") is not None]
            # pooled pair sign test (pairs within a burst are not independent: reported as indicative only)
            c_f = [r["conc_fee"] for r in sub if r.get("conc_fee") is not None]
            per_val.append({"client": c, "version": v, "validator": ident, "arm": ":".join(x for x in arm if x),
                            "bursts": len(sub), "bursts_with_>=3_landed": len(tf),
                            "landed": sum(r["n_landed"] for r in sub), "sent": sum(r["n_sent"] for r in sub),
                            "mean_tau_fee": float(np.mean(tf)) if tf else None, "ci_tau_fee": bootstrap_ci(tf),
                            "mean_tau_send": float(np.mean(ts)) if ts else None, "ci_tau_send": bootstrap_ci(ts),
                            "burst_sign_p_fee": sign_test_p(sum(x > 0 for x in tf), sum(x != 0 for x in tf)),
                            "mean_conc_fee": float(np.mean(c_f)) if c_f else None,
                            "verdict": verdict(sub)})
    # attribute each burst to the leader that actually produced the block (forwarded probes land elsewhere)
    snap_p = os.path.join(rdir, "cluster_snapshot.json")
    nodes = json.load(open(snap_p)).get("nodes", {}) if os.path.exists(snap_p) else {}
    for b in bs:
        n = nodes.get(b.get("producer") or "", {})
        b["producer_client"] = f"{n['client']}/{n['version']}" if n else ("unknown" if b.get("producer") else None)
    per_client = []
    pg = collections.defaultdict(list)
    for b in bs:
        if b.get("tau_fee") is None or b.get("n_producers") != 1:
            continue
        pg[(b["producer_client"], f"{b['payer_mode']}:{b['timing']}:{b['gap_ms']:g}")].append(b)
        pg[(b["producer_client"], f"{b['payer_mode']}:*")].append(b)
    for (c, arm), rows in sorted(pg.items()):
        tf = [r["tau_fee"] for r in rows]
        ts = [r["tau_send"] for r in rows if r.get("tau_send") is not None]
        per_client.append({"producer_client": c, "arm": arm, "bursts": len(rows),
                           "producers": len({r["producer"] for r in rows}),
                           "forwarded": sum(1 for r in rows if not r.get("producer_is_target")),
                           "mean_tau_fee": float(np.mean(tf)), "ci_tau_fee": bootstrap_ci(tf),
                           "mean_tau_send": float(np.mean(ts)) if ts else None, "ci_tau_send": bootstrap_ci(ts),
                           "perfect_fee": sum(x >= 0.999 for x in tf), "verdict": verdict(rows)})
    res = {"bursts": bs, "per_validator": per_val, "per_producer_client": per_client}
    json.dump(res, open(os.path.join(rdir, "results.json"), "w"), indent=1)
    _tables(rdir, res)
    _plot(rdir, bs)
    return res


def _fmt(x, nd=2):
    if x is None:
        return "–"
    if isinstance(x, (tuple, list)):
        return "[" + ", ".join(_fmt(v, nd) for v in x) + "]"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def _tables(rdir, res):
    L = ["| client/version | validator | arm | bursts | sent→landed | τ fee (95% CI) | τ send (95% CI) | verdict |",
         "|---|---|---|---|---|---|---|---|"]
    for r in res["per_validator"]:
        L.append(f"| {r['client']}/{r['version']} | `{r['validator'][:8]}…` | {r['arm']} | {r['bursts']} | "
                 f"{r['sent']}→{r['landed']} | {_fmt(r['mean_tau_fee'])} {_fmt(r['ci_tau_fee'])} | "
                 f"{_fmt(r['mean_tau_send'])} {_fmt(r['ci_tau_send'])} | {r['verdict']} |")
    L = ["## By producing client (leader that actually built the block) × arm", "",
         "Bursts with ≥3 landed probes, all in blocks of one leader. `forwarded` = produced by a leader other than the one targeted.", "",
         "| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | perfectly fee-sorted | τ send (95% CI) | verdict |",
         "|---|---|---|---|---|---|---|---|---|"] + [
        f"| {r['producer_client']} | {r['arm']} | {r['bursts']} | {r['producers']} | {r['forwarded']} | "
        f"{_fmt(r['mean_tau_fee'])} {_fmt(r['ci_tau_fee'])} | {r['perfect_fee']}/{r['bursts']} | "
        f"{_fmt(r['mean_tau_send'])} {_fmt(r['ci_tau_send'])} | {r['verdict']} |" for r in res.get("per_producer_client", [])
    ] + ["", "## By targeted validator × arm", ""] + L
    L += ["", "## Per burst", "",
          "| burst | targeted client | arm | status | landed | slot offset | producer = target | slots | first idx / block | span | τ fee | τ send |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for b in res["bursts"]:
        L.append(f"| {b['burst']} | {b['client']}/{b['version']} | {b['payer_mode']}:{b['timing']}:{b['gap_ms']} | {b['status'][:40]} | "
                 f"{b['n_landed']}/{b['n_sent']} | {_fmt(b.get('landed_offset_slots'))} | {_fmt(b.get('producer_is_target'))} ({_fmt(b.get('producer_client'))}) | "
                 f"{_fmt(b.get('n_slots_used'))} | {_fmt(b.get('first_index'))}/"
                 f"{_fmt(b.get('block_n_tx'))} | {_fmt(b.get('span_in_block'))} | {_fmt(b.get('tau_fee'))} | "
                 f"{_fmt(b.get('tau_send'))} |")
    open(os.path.join(rdir, "tables.md"), "w").write("\n".join(L) + "\n")


def _plot(rdir, bs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    pts = [b for b in bs if b.get("tau_fee") is not None]
    if not pts:
        return
    lab = lambda b: b.get("producer_client") or f"{b['client']}/{b['version']}"
    clients = sorted({lab(b) for b in pts})
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for i, c in enumerate(clients):
        sub = [b for b in pts if lab(b) == c]
        for dx, mode, mk, cf, cs in ((-0.09, "shared", "o", "tab:red", "tab:blue"), (0.09, "independent", "^", "tab:orange", "tab:cyan")):
            g = [b for b in sub if b["payer_mode"] == mode]
            ax.scatter([i + dx - 0.04] * len(g), [b["tau_fee"] for b in g], c=cf, marker=mk, alpha=0.8,
                       label=f"τ fee, {mode} payer" if i == 0 else None)
            g = [b for b in g if b.get("tau_send") is not None]
            ax.scatter([i + dx + 0.04] * len(g), [b["tau_send"] for b in g], c=cs, marker=mk, alpha=0.8,
                       label=f"τ send, {mode} payer" if i == 0 else None)
    ax.axhline(0, c="grey", lw=0.8)
    ax.set_xticks(range(len(clients)), clients, rotation=25, ha="right")
    ax.set_ylabel("Kendall τ (position vs rule)")
    ax.set_ylim(-1.05, 1.05)
    ax.legend()
    ax.set_xlabel("client of the leader that produced the block")
    ax.set_title("Per burst: does block position follow fee (red/orange) or send order (blue/cyan)?")
    fig.tight_layout()
    fig.savefig(os.path.join(rdir, "tau_by_client.png"), dpi=130)
