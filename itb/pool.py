"""Pool the per-burst results of several live runs and write pooled tables + plot.

python -m itb.pool <out_dir> <run_dir> [<run_dir> ...]   (offline; reads each run's results.json)
"""
from __future__ import annotations

import collections
import json
import os
import sys

import numpy as np

from .analyze import _fmt, _plot, verdict
from .stats import bootstrap_ci, sign_test_p


def pool(out: str, runs: list[str]) -> dict:
    os.makedirs(out, exist_ok=True)
    bs = []
    for r in runs:
        for b in json.load(open(os.path.join(r, "results.json")))["bursts"]:
            bs.append(dict(b, run=os.path.basename(r.rstrip("/"))))
    status = collections.Counter(("sent" if b["status"] == "sent" else b["status"].split(" ")[0].split(":")[0]) for b in bs)
    sent = sum(b["n_sent"] for b in bs)
    landed = sum(b["n_landed"] for b in bs)
    usable = [b for b in bs if b.get("tau_fee") is not None and b.get("n_producers") == 1]
    groups = collections.defaultdict(list)
    for b in usable:
        arm = f"{b['payer_mode']}:{b['timing']}:{b['gap_ms']:g}"
        for key in ((b["producer_client"], arm), (b["producer_client"], b["payer_mode"] + ":*"),
                    ("ALL clients", b["payer_mode"] + ":*"), ("ALL clients", arm)):
            groups[key].append(b)
    rows = []
    for (c, arm), g in sorted(groups.items()):
        tf = [x["tau_fee"] for x in g]
        ts = [x["tau_send"] for x in g if x.get("tau_send") is not None]
        rows.append({"producer_client": c, "arm": arm, "bursts": len(g), "leaders": len({x["producer"] for x in g}),
                     "forwarded": sum(1 for x in g if not x.get("producer_is_target")),
                     "mean_tau_fee": float(np.mean(tf)), "ci_tau_fee": bootstrap_ci(tf),
                     "mean_tau_send": float(np.mean(ts)) if ts else None, "ci_tau_send": bootstrap_ci(ts),
                     "fee_sign_p": sign_test_p(sum(x > 0 for x in tf), sum(x != 0 for x in tf)),
                     "perfect_fee": int(sum(x >= 0.999 for x in tf)), "verdict": verdict(g)})
    tgt = collections.defaultdict(lambda: [0, 0, 0])
    for b in bs:
        t = tgt[f"{b['client']}/{b['version']}"]
        t[0] += 1 if b["status"] == "sent" else 0
        t[1] += b["n_sent"]
        t[2] += b["n_landed"]
    res = {"runs": runs, "n_bursts": len(bs), "status": dict(status), "sent": sent, "landed": landed,
           "usable_bursts": len(usable), "forwarded_usable": sum(1 for b in usable if not b.get("producer_is_target")),
           "by_target": {k: {"bursts_sent": v[0], "probes_sent": v[1], "landed": v[2]} for k, v in tgt.items()},
           "pooled": rows}
    json.dump(res, open(os.path.join(out, "pooled_results.json"), "w"), indent=1)
    L = [f"# Pooled mainnet live results ({', '.join(res['runs'])})", "",
         f"Bursts planned {len(bs)}; status {dict(status)}. Probes sent {sent}, landed {landed} ({landed / max(sent, 1):.0%}). "
         f"Usable bursts (≥3 landed, one producing leader): {len(usable)}, of which {res['forwarded_usable']} were produced by a leader other than the target.", "",
         "## Landing by targeted client", "", "| targeted client | bursts sent | probes sent | landed | rate |", "|---|---|---|---|---|"]
    for k, v in sorted(res["by_target"].items()):
        L.append(f"| {k} | {v['bursts_sent']} | {v['probes_sent']} | {v['landed']} | {v['landed'] / max(v['probes_sent'], 1):.0%} |")
    L += ["", "## By producing client × arm (pooled over runs)", "",
          "| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | sign-test p (τ fee > 0) | perfectly fee-sorted | τ send (95% CI) | verdict |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['producer_client']} | {r['arm']} | {r['bursts']} | {r['leaders']} | {r['forwarded']} | "
                 f"{_fmt(r['mean_tau_fee'])} {_fmt(r['ci_tau_fee'])} | {_fmt(r['fee_sign_p'], 3)} | {r['perfect_fee']}/{r['bursts']} | "
                 f"{_fmt(r['mean_tau_send'])} {_fmt(r['ci_tau_send'])} | {r['verdict']} |")
    open(os.path.join(out, "tables.md"), "w").write("\n".join(L) + "\n")
    _plot(out, usable)
    return res


if __name__ == "__main__":
    pool(sys.argv[1], sys.argv[2:])
