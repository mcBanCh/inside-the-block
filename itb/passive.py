"""Passive (free, zero-spend) survey: how do *other people's* transactions sit in
blocks produced by each client? Supplementary evidence only - we cannot know
their arrival times, so this can show "order correlates with fee", never "why".
"""
from __future__ import annotations

import asyncio
import collections
import gzip
import json
import logging
import os
import random
import time

import numpy as np

from . import ALPENGLOW_FIRST_SLOT
from .blockparse import block_table
from .cluster import snapshot
from .rpc import Rpc, RpcError
from .stats import spearman

log = logging.getLogger("itb.passive")


def block_metrics(rows: list[dict]) -> dict:
    """Ordering metrics over non-vote, fee-paying transactions of one block."""
    r = [x for x in rows if not x["vote"] and x["prio_lamports"] is not None]
    n = len(r)
    m = {"n_tx": len(rows), "n_nonvote": n}
    if n < 10:
        return m
    pos = np.arange(n)
    # Priority proxy 1: micro-lamports per requested CU (what wallets set)
    price = np.array([x["cu_price"] or 0 for x in r], float)
    # Priority proxy 2: priority lamports / effective CU limit (close to Agave reward/cost)
    dens = np.array([x["agave_priority"] if x["agave_priority"] is not None
                     else x["prio_lamports"] / max(x["eff_cu_limit"], 1) for x in r], float)
    m["rho_pos_price"] = spearman(pos, price)
    m["rho_pos_density"] = spearman(pos, dens)
    # local sortedness: mean Spearman inside 32-tx windows (detects batch-wise sorting)
    loc = [spearman(pos[i:i + 32], dens[i:i + 32]) for i in range(0, n - 31, 32)]
    loc = [x for x in loc if x is not None]
    m["rho_local32_density"] = float(np.mean(loc)) if loc else None
    m["share_zero_price"] = float(np.mean(price == 0))
    # where do the top-decile fee-density txs sit? (0 = block start, 1 = end)
    k = max(1, n // 10)
    top = np.argsort(-dens)[:k]
    m["top_decile_mean_relpos"] = float(np.mean(top / (n - 1)))
    return m


async def survey(rpc: Rpc, out_dir: str, per_client: int = 6, lookback: int = 6000, seed: int = 1):
    os.makedirs(out_dir, exist_ok=True)
    snap = await snapshot(rpc)
    json.dump(snap, open(f"{out_dir}/cluster_snapshot.json", "w"))
    tip = await rpc.call("getSlot", [{"commitment": "confirmed"}])
    start = max(tip - lookback, ALPENGLOW_FIRST_SLOT)
    leaders = []
    s = start
    while s < tip - 64:
        lim = min(5000, tip - 64 - s)
        leaders += [(s + i, l) for i, l in enumerate(await rpc.call("getSlotLeaders", [s, lim]))]
        s += lim
    # group windows (4 consecutive slots) by client/version of leader
    by_cv = collections.defaultdict(list)
    for slot, leader in leaders:
        if slot % 4 == 0:
            n = snap["nodes"].get(leader)
            cv = f'{n["client"]}/{n["version"]}' if n else "not-in-gossip"
            by_cv[cv].append((slot, leader))
    rnd = random.Random(seed)
    picked = []
    for cv, wins in by_cv.items():
        if cv.startswith("Agave/") and len(wins) < 2:
            continue
        rnd.shuffle(wins)
        seen = set()
        for slot, leader in wins:
            if leader in seen:  # spread across distinct validators
                continue
            seen.add(leader)
            picked.append((cv, leader, slot + rnd.randrange(4)))
            if len(seen) >= per_client:
                break
    results = []
    raw = gzip.open(f"{out_dir}/passive_blocks.jsonl.gz", "wt")
    for cv, leader, slot in sorted(picked, key=lambda x: x[2]):
        try:
            b = await rpc.call("getBlock", [slot, {"encoding": "json", "maxSupportedTransactionVersion": 1,
                                                   "transactionDetails": "full", "rewards": False,
                                                   "commitment": "confirmed"}])
        except RpcError as e:
            log.info("slot %s (%s): %s", slot, cv, e)
            results.append({"slot": slot, "leader": leader, "client_version": cv, "skipped_or_missing": str(e)[:120]})
            continue
        rows = block_table(b)
        raw.write(json.dumps({"slot": slot, "leader": leader, "client_version": cv, "blockhash": b["blockhash"],
                              "rows": rows}) + "\n")
        met = block_metrics(rows)
        met.update({"slot": slot, "leader": leader, "client_version": cv})
        results.append(met)
        log.info("slot %s %-28s n=%s rho_price=%s", slot, cv, met.get("n_nonvote"), met.get("rho_pos_price"))
    raw.close()
    meta = {"measured_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "slot_range": [start, tip],
            "rpc": rpc.redacted_url}
    json.dump({"meta": meta, "blocks": results}, open(f"{out_dir}/passive_metrics.json", "w"), indent=1)
    return results
