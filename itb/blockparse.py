"""Turn a getBlock(json) response into a compact, verifiable per-transaction table."""
from __future__ import annotations

import base58

COMPUTE_BUDGET = "ComputeBudget111111111111111111111111111111"
VOTE_PROGRAM = "Vote111111111111111111111111111111111111111"
DEFAULT_CU_PER_IX = 200_000
MAX_CU = 1_400_000
LAMPORTS_PER_SIG = 5_000


def parse_compute_budget(msg: dict) -> tuple[int | None, int | None, int]:
    """Return (cu_limit or None, cu_price_microlamports or None, n_non_cb_ix)."""
    keys = msg["accountKeys"]
    limit = price = None
    non_cb = 0
    for ix in msg["instructions"]:
        prog = keys[ix["programIdIndex"]] if ix["programIdIndex"] < len(keys) else None
        if prog != COMPUTE_BUDGET:
            non_cb += 1
            continue
        d = base58.b58decode(ix["data"])
        if not d:
            continue
        if d[0] == 2 and len(d) >= 5:
            limit = int.from_bytes(d[1:5], "little")
        elif d[0] == 3 and len(d) >= 9:
            price = int.from_bytes(d[1:9], "little")
    return limit, price, non_cb


def block_table(block: dict) -> list[dict]:
    rows = []
    for i, t in enumerate(block.get("transactions") or []):
        tx, meta = t["transaction"], t.get("meta") or {}
        msg = tx["message"]
        keys = msg["accountKeys"]
        limit, price, non_cb = parse_compute_budget(msg)
        cfg = msg.get("transactionConfig")  # v1 transactions carry the budget in the message itself
        prio_cfg = None
        if cfg:
            limit = cfg.get("computeUnitLimit", limit)
            prio_cfg = cfg.get("priorityFee")  # total lamports, not per-CU
            if prio_cfg is not None and limit:
                price = prio_cfg * 1_000_000 // limit  # express as micro-lamports per CU for comparability
        nsig = len(tx["signatures"])
        eff_limit = limit if limit is not None else min(MAX_CU, DEFAULT_CU_PER_IX * max(non_cb, 1))
        fee = meta.get("fee")
        prio_lamports = None if fee is None else max(fee - LAMPORTS_PER_SIG * nsig, 0)
        progs = {keys[ix["programIdIndex"]] for ix in msg["instructions"] if ix["programIdIndex"] < len(keys)}
        cost = meta.get("costUnits")
        # Agave scheduler priority ~= reward * 1e6 / (cost + 1), reward = priority fee + 50% of signature fee
        # (core/src/banking_stage/transaction_priority.rs). costUnits is reported by the RPC for each tx.
        reward = None if prio_lamports is None else prio_lamports + (LAMPORTS_PER_SIG // 2) * nsig
        agave_prio = None if (reward is None or cost is None) else reward * 1_000_000 // (cost + 1)
        rows.append({
            "i": i,
            "version": t.get("version"),
            "cost_units": cost,
            "agave_priority": agave_prio,
            "v1_priority_fee": prio_cfg,
            "sig": tx["signatures"][0],
            "payer": keys[0],
            "nsig": nsig,
            "fee": fee,
            "prio_lamports": prio_lamports,
            "cu_limit": limit,
            "cu_price": price,
            "eff_cu_limit": eff_limit,
            "cu_used": meta.get("computeUnitsConsumed"),
            "err": meta.get("err") is not None,
            "vote": VOTE_PROGRAM in progs,
            # Jito tip accounts are not decoded on purpose: bundles/tips are out of scope.
        })
    return rows
