"""Independent check of a run's claims, using only public RPC data.

For every landed probe in landed.jsonl:
  * getBlock(slot, transactionDetails=signatures) and confirm the signature sits at the recorded index;
  * getSlotLeaders(slot, 1) and confirm the slot's leader is the validator we targeted.
Writes verify.json in the run dir and prints a summary. It sends nothing and needs no keys.
"""
import json
import logging
import os

from .rpc import Rpc, RpcError

log = logging.getLogger("itb.verify")


async def verify(rpc: Rpc, rdir: str) -> dict:
    bursts = [json.loads(l) for l in open(os.path.join(rdir, "landed.jsonl"))]
    blocks, leaders, rows = {}, {}, []
    for b in bursts:
        for t in b.get("txs", []):
            slot = t.get("landed_slot")
            if slot is None:
                continue
            if slot not in blocks:
                try:
                    blk = await rpc.call("getBlock", [slot, {"encoding": "json", "transactionDetails": "signatures",
                                                             "rewards": False, "maxSupportedTransactionVersion": 1,
                                                             "commitment": "confirmed"}])
                    blocks[slot] = blk.get("signatures", []) if blk else None
                    ld = await rpc.call("getSlotLeaders", [slot, 1])
                    leaders[slot] = ld[0] if ld else None
                except RpcError as e:  # e.g. pruned on a non-archival node
                    log.warning("slot %s unavailable: %s", slot, e)
                    blocks[slot], leaders[slot] = None, None
            sigs = blocks[slot]
            if sigs is None:
                rows.append({"burst": b["burst"], "sig": t["sig"], "slot": slot, "unavailable": True,
                             "index_ok": False, "leader_ok": False})
                continue
            idx = sigs.index(t["sig"]) if t["sig"] in sigs else None
            rows.append({"burst": b["burst"], "sig": t["sig"], "slot": slot,
                         "index_claimed": t.get("index_in_block"), "index_onchain": idx,
                         "index_ok": idx == t.get("index_in_block"),
                         "leader_onchain": leaders[slot], "leader_ok": leaders[slot] == b["validator"],
                         "leader_recorded_ok": leaders[slot] == t.get("landed_leader", b["validator"])})
    out = {"n": len(rows), "index_ok": sum(r["index_ok"] for r in rows),
           "leader_ok": sum(r["leader_ok"] for r in rows),
           "leader_recorded_ok": sum(bool(r.get("leader_recorded_ok")) for r in rows),
           "unavailable": sum(bool(r.get("unavailable")) for r in rows), "rows": rows}
    with open(os.path.join(rdir, "verify.json"), "w") as f:
        json.dump(out, f, indent=1)
    log.info("verified %d landed probes: index matches %d, produced by the targeted leader %d, "
             "producer matches the recorded landed_leader %d, block unavailable %d",
             out["n"], out["index_ok"], out["leader_ok"], out["leader_recorded_ok"], out["unavailable"])
    return out
