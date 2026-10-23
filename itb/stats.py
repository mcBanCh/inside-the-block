"""Rank statistics used everywhere (pure numpy/scipy, no fitting)."""
from __future__ import annotations

import numpy as np
from scipy import stats


def kendall(a, b) -> float | None:
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) < 3 or np.all(a == a[0]) or np.all(b == b[0]):
        return None
    t = stats.kendalltau(a, b).statistic
    return None if np.isnan(t) else float(t)


def spearman(a, b) -> float | None:
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) < 3 or np.all(a == a[0]) or np.all(b == b[0]):
        return None
    r = stats.spearmanr(a, b).statistic
    return None if np.isnan(r) else float(r)


def concordant_fraction(pos, key) -> float | None:
    """Share of pairs (with distinct key) where higher key sits EARLIER in the block."""
    n = len(pos)
    c = d = 0
    for i in range(n):
        for j in range(i + 1, n):
            if key[i] == key[j]:
                continue
            hi, lo = (i, j) if key[i] > key[j] else (j, i)
            if pos[hi] < pos[lo]:
                c += 1
            else:
                d += 1
    return None if c + d == 0 else c / (c + d)


def sign_test_p(successes: int, n: int) -> float | None:
    if n == 0:
        return None
    return float(stats.binomtest(successes, n, 0.5).pvalue)


def bootstrap_ci(values, n=2000, seed=0, q=(2.5, 97.5)):
    v = np.asarray([x for x in values if x is not None], float)
    if len(v) < 2:
        return None
    rng = np.random.default_rng(seed)
    means = rng.choice(v, (n, len(v)), replace=True).mean(axis=1)
    lo, hi = np.percentile(means, q)
    return float(lo), float(hi)
