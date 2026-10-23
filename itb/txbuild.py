"""Probe transactions: ComputeBudget(limit, price) + fixed-length SPL Memo.

Every probe in a burst has the *same* shape (same instruction list, same CU
limit, same byte length, same number of signatures, one writable account =
its own fee payer). The only thing that differs is the CU price, so under any
fee-density rule (Agave reward/cost, Firedancer rewards/compute_est, BAM "fee
density") their priority order equals their CU-price order.
"""
from __future__ import annotations

import math

from solders.compute_budget import set_compute_unit_limit, set_compute_unit_price
from solders.hash import Hash
from solders.instruction import Instruction
from solders.keypair import Keypair
from solders.message import MessageV0
from solders.pubkey import Pubkey
from solders.system_program import TransferParams, transfer
from solders.transaction import VersionedTransaction

# SPL Memo v1. On 2026-10-23 getAccountInfo(MemoSq4gqABAXKb96qnH8TysNne8xFEBLFbuNgYsJu1) returned null on mainnet
# and every probe failed load with ProgramAccountNotFound (REPORT §6.10), so the probes use Memo v1, which is live.
MEMO_V2 = Pubkey.from_string("Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo")
LAMPORTS_PER_SIG = 5_000
MEMO_LEN = 40


def memo_tag(run_id: str, burst: int, k: int) -> bytes:
    tag = f"itb|{run_id}|{burst}|{k}".encode()
    if len(tag) > MEMO_LEN:
        raise ValueError("tag too long")
    return tag.ljust(MEMO_LEN, b".")


def max_fee(cu_limit: int, cu_price: int, nsig: int = 1) -> int:
    return LAMPORTS_PER_SIG * nsig + math.ceil(cu_limit * cu_price / 1_000_000)


def build_probe(payer: Keypair, blockhash: Hash, cu_limit: int, cu_price: int, tag: bytes,
                use_memo: bool = True) -> VersionedTransaction:
    ixs = [set_compute_unit_limit(cu_limit), set_compute_unit_price(cu_price)]
    if use_memo:
        ixs.append(Instruction(MEMO_V2, tag, []))
    else:  # localnet without the memo program: 0-lamport self transfer keeps the shape fixed
        ixs.append(transfer(TransferParams(from_pubkey=payer.pubkey(), to_pubkey=payer.pubkey(), lamports=0)))
    msg = MessageV0.try_compile(payer.pubkey(), ixs, [], blockhash)
    return VersionedTransaction(msg, [payer])


def build_transfers(payer: Keypair, blockhash: Hash, dests: list[tuple[Pubkey, int]],
                    cu_price: int = 0) -> VersionedTransaction:
    ixs = [set_compute_unit_limit(450 * len(dests) + 300)]
    if cu_price:
        ixs.append(set_compute_unit_price(cu_price))
    ixs += [transfer(TransferParams(from_pubkey=payer.pubkey(), to_pubkey=d, lamports=l)) for d, l in dests]
    return VersionedTransaction(MessageV0.try_compile(payer.pubkey(), ixs, [], blockhash), [payer])


def fee_ladder(k: int, lo: int, hi: int) -> list[int]:
    """k distinct, geometrically spaced CU prices (micro-lamports/CU)."""
    if k == 1:
        return [lo]
    r = (hi / lo) ** (1 / (k - 1))
    out = sorted({int(round(lo * r ** i, -2)) for i in range(k)})
    if len(out) != k:
        raise ValueError("ladder collapsed; widen lo/hi")
    return out
