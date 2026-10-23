import json
import os

import pytest
from solders.hash import Hash
from solders.keypair import Keypair

from itb.analyze import burst_stats, verdict
from itb.blockparse import block_table, parse_compute_budget
from itb.budget import HARD_CEILING_SOL, SpendCap, SpendCapExceeded
from itb.stats import concordant_fraction, kendall
from itb.txbuild import build_probe, fee_ladder, max_fee, memo_tag


def test_ladder_distinct_sorted():
    l = fee_ladder(8, 1_000, 200_000)
    assert len(l) == 8 and l == sorted(l) and len(set(l)) == 8


def test_probes_same_shape():
    kp, bh = Keypair(), Hash.default()
    a = build_probe(kp, bh, 20_000, 1_000, memo_tag("r", 1, 0))
    b = build_probe(kp, bh, 20_000, 200_000, memo_tag("r", 1, 7))
    assert len(bytes(a)) == len(bytes(b))  # identical size -> identical cost model inputs


def test_max_fee():
    assert max_fee(20_000, 200_000) == 5_000 + 4_000
    assert max_fee(20_000, 1) == 5_001  # ceil


def test_spend_cap(tmp_path):
    with pytest.raises(ValueError):
        SpendCap(HARD_CEILING_SOL * 2, str(tmp_path / "l.jsonl"))
    cap = SpendCap(0.00001, str(tmp_path / "l.jsonl"))  # 10_000 lamports
    cap.reserve(9_000, "a", [])
    with pytest.raises(SpendCapExceeded):
        cap.reserve(2_000, "b", [])
    # persisted: a new process sees what was already reserved
    assert SpendCap(0.00001, str(tmp_path / "l.jsonl")).remaining == 1_000


def test_parse_compute_budget_legacy_and_v1():
    import base58
    cb = "ComputeBudget111111111111111111111111111111"
    msg = {"accountKeys": ["payer", cb, "Memo"], "instructions": [
        {"programIdIndex": 1, "data": base58.b58encode(bytes([2]) + (30_000).to_bytes(4, "little")).decode()},
        {"programIdIndex": 1, "data": base58.b58encode(bytes([3]) + (5_000).to_bytes(8, "little")).decode()},
        {"programIdIndex": 2, "data": ""}]}
    assert parse_compute_budget(msg) == (30_000, 5_000, 1)
    blk = {"transactions": [{"version": 1, "transaction": {"signatures": ["s"], "message": {
        "accountKeys": ["p", "prog"], "instructions": [{"programIdIndex": 1, "data": ""}],
        "transactionConfig": {"computeUnitLimit": 1000, "priorityFee": 500}}},
        "meta": {"fee": 5_500, "costUnits": 2_000, "computeUnitsConsumed": 900, "err": None}}]}
    r = block_table(blk)[0]
    assert r["cu_limit"] == 1000 and r["cu_price"] == 500_000 and r["prio_lamports"] == 500
    assert r["agave_priority"] == (500 + 2_500) * 1_000_000 // 2_001


def test_rank_stats():
    assert kendall([0, 1, 2, 3], [0, 1, 2, 3]) == pytest.approx(1)
    # position 0 holds the highest fee -> fully concordant
    assert concordant_fraction([0, 1, 2], [30, 20, 10]) == 1.0


def _burst(prices_by_pos, sends_by_pos):
    txs = [{"sig": f"s{i}", "cu_price": p, "send_rank": s, "landed_slot": 100, "index_in_block": 10 + i,
            "block_n_tx": 50, "send_ok": True} for i, (p, s) in enumerate(zip(prices_by_pos, sends_by_pos))]
    return {"burst": 0, "validator": "v", "client": "c", "version": "1", "payer_mode": "shared", "timing": "pre",
            "gap_ms": 0, "status": "sent", "window_first_slot": 100, "txs": txs}


def test_burst_stats_fee_sorted():
    b = burst_stats(_burst([800, 700, 600, 500, 400], [3, 0, 4, 1, 2]))
    assert b["tau_fee"] == pytest.approx(1) and b["span_in_block"] == 5 and b["foreign_between"] == 0


def test_burst_stats_fifo():
    b = burst_stats(_burst([500, 800, 400, 700, 600], [0, 1, 2, 3, 4]))
    assert b["tau_send"] == pytest.approx(1)


def test_verdict_noise():
    rows = [{"tau_fee": x, "tau_send": -x} for x in (0.1, -0.2, 0.0, 0.15, -0.1)]
    assert verdict(rows).startswith("no rule")
