"""Spend cap. Every lamport that can leave the operator's wallet as a *fee* is
reserved here BEFORE the transaction is signed for sending. The ledger is an
append-only JSONL file in the data volume, so the cap holds across restarts
and across multiple runs (the whole campaign must fit in ~0.05 SOL).
"""
from __future__ import annotations

import json
import os
import threading
import time

LAMPORTS_PER_SOL = 1_000_000_000
HARD_CEILING_SOL = 0.05  # bounty: "entire measurement process should fit within approximately 0.05 SOL"


class SpendCapExceeded(RuntimeError):
    pass


class SpendCap:
    def __init__(self, cap_sol: float, ledger_path: str):
        if cap_sol > HARD_CEILING_SOL + 1e-12:
            raise ValueError(f"cap {cap_sol} SOL exceeds hard ceiling {HARD_CEILING_SOL} SOL")
        self.cap = int(cap_sol * LAMPORTS_PER_SOL)
        self.path = ledger_path
        self._lock = threading.Lock()
        self.reserved = 0
        self.actual = {}
        if os.path.exists(ledger_path):
            for line in open(ledger_path):
                e = json.loads(line)
                if e["kind"] == "reserve":
                    self.reserved += e["lamports"]

    def _append(self, e: dict):
        e["t"] = time.time()
        with open(self.path, "a") as f:
            f.write(json.dumps(e) + "\n")
            f.flush()
            os.fsync(f.fileno())

    @property
    def remaining(self) -> int:
        return self.cap - self.reserved

    def reserve(self, lamports: int, what: str, sigs: list[str]):
        """Reserve worst-case fees for a group of transactions or raise."""
        with self._lock:
            if self.reserved + lamports > self.cap:
                raise SpendCapExceeded(f"{what}: need {lamports}, remaining {self.remaining} lamports")
            self.reserved += lamports
            self._append({"kind": "reserve", "lamports": lamports, "what": what, "sigs": sigs})

    def record_actual(self, sig: str, fee: int | None):
        self._append({"kind": "actual", "sig": sig, "fee": fee})
