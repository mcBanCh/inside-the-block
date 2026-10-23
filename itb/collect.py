"""After a run: find where every probe landed and save verifiable raw data."""
from __future__ import annotations

import asyncio
import gzip
import json
import logging
import os

from .blockparse import block_table
from .rpc import Rpc, RpcError

log = logging.getLogger("itb.collect")
GETBLOCK = {"encoding": "json", "maxSupportedTransactionVersion": 1, "transactionDetails": "full",
            "rewards": False, "commitment": "confirmed"}


async def collect(rpc: Rpc, rdir: str):
    recs = [json.loads(l) for l in open(os.path.join(rdir, "sends.jsonl"))]
    live = any(t.get("send_ok") for r in recs for t in r.get("txs", []))
    # 1) window liveness: which of the 4 slots produced a block (cheap, both modes)
    for r in recs:
        f = r["window_first_slot"]
        try:
            r["window_blocks_produced"] = await rpc.call("getBlocks", [f, f + 3, {"commitment": "confirmed"}])
        except RpcError as e:
            r["window_blocks_produced"] = f"error: {e}"[:100]
    # 2) where did probes land
    slots_needed = set()
    if live:
        sigs = [t["sig"] for r in recs for t in r.get("txs", [])]
        status = {}
        for i in range(0, len(sigs), 200):
            v = (await rpc.call("getSignatureStatuses", [sigs[i:i + 200], {"searchTransactionHistory": True}]))["value"]
            status.update(dict(zip(sigs[i:i + 200], v)))
        for r in recs:
            for t in r.get("txs", []):
                s = status.get(t["sig"])
                t["landed_slot"] = s["slot"] if s else None
                t["tx_err"] = s["err"] if s else None
                if s:
                    slots_needed.add(s["slot"])
    # 2b) who actually produced each landing slot (probes can be forwarded to a later leader)
    leader_of = {}
    if slots_needed:
        lo, hi = min(slots_needed), max(slots_needed)
        for a in range(lo, hi + 1, 4000):
            try:
                ls = await rpc.call("getSlotLeaders", [a, min(4000, hi + 1 - a)])
                leader_of.update({a + i: x for i, x in enumerate(ls)})
            except RpcError as e:
                log.warning("getSlotLeaders %s: %s", a, e)
    for r in recs:
        for t in r.get("txs", []):
            if t.get("landed_slot") is not None:
                t["landed_leader"] = leader_of.get(t["landed_slot"])
    # 3) full blocks for every slot holding a probe -> compact per-tx table (all txs, not only ours)
    tables = {}
    gz = gzip.open(os.path.join(rdir, "blocks.jsonl.gz"), "wt")
    for slot in sorted(slots_needed):
        try:
            b = await rpc.call("getBlock", [slot, GETBLOCK])
        except RpcError as e:
            log.warning("getBlock %s: %s", slot, e)
            continue
        rows = block_table(b)
        tables[slot] = {x["sig"]: x for x in rows}
        gz.write(json.dumps({"slot": slot, "blockhash": b["blockhash"], "parentSlot": b["parentSlot"],
                             "blockTime": b.get("blockTime"), "rows": rows}) + "\n")
    gz.close()
    for r in recs:
        for t in r.get("txs", []):
            row = tables.get(t.get("landed_slot"), {}).get(t["sig"])
            if row:
                t.update({"index_in_block": row["i"], "block_n_tx": len(tables[t["landed_slot"]]),
                          "fee": row["fee"], "cu_used": row["cu_used"], "cost_units": row["cost_units"],
                          "agave_priority": row["agave_priority"]})
    with open(os.path.join(rdir, "landed.jsonl"), "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    log.info("collected %d bursts, %d blocks", len(recs), len(tables))
    return recs
