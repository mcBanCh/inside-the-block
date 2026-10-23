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
    res = {"bursts": bs, "per_validator": per_val}
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
    L += ["", "| burst | client | arm | status | landed | slots | first idx / block | span | τ fee | τ send |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for b in res["bursts"]:
        L.append(f"| {b['burst']} | {b['client']}/{b['version']} | {b['payer_mode']}:{b['timing']}:{b['gap_ms']} | {b['status']} | "
                 f"{b['n_landed']}/{b['n_sent']} | {_fmt(b.get('n_slots_used'))} | {_fmt(b.get('first_index'))}/"
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
    clients = sorted({f"{b['client']}/{b['version']}" for b in pts})
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for i, c in enumerate(clients):
        sub = [b for b in pts if f"{b['client']}/{b['version']}" == c]
        ax.scatter([i - 0.12] * len(sub), [b["tau_fee"] for b in sub], c="tab:orange", label="τ fee" if i == 0 else None)
        ax.scatter([i + 0.12] * len(sub), [b["tau_send"] for b in sub], c="tab:blue", label="τ send" if i == 0 else None)
    ax.axhline(0, c="grey", lw=0.8)
    ax.set_xticks(range(len(clients)), clients, rotation=25, ha="right")
    ax.set_ylabel("Kendall τ (position vs rule)")
    ax.set_ylim(-1.05, 1.05)
    ax.legend()
    ax.set_title("Per burst: does block position follow fee (orange) or send order (blue)?")
    fig.tight_layout()
    fig.savefig(os.path.join(rdir, "tau_by_client.png"), dpi=130)
