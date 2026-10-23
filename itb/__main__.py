"""CLI.  python -m itb <command>   (see README)"""
from __future__ import annotations

import argparse
import asyncio
import glob
import json
import logging
import os
import sys

from .rpc import Rpc


def main(argv=None):
    ap = argparse.ArgumentParser(prog="itb")
    ap.add_argument("--data", default=os.environ.get("ITB_DATA", "data"))
    ap.add_argument("--rpc", default=None, help="RPC URL (or env ITB_RPC_URL); default public mainnet")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("snapshot", help="client/version/stake breakdown of the cluster")
    p = sub.add_parser("passive", help="zero-spend survey of existing blocks per client")
    p.add_argument("--per-client", type=int, default=4)
    r = sub.add_parser("run", help="plan + execute bursts (DRY-RUN unless --live)")
    r.add_argument("--live", action="store_true", help="really send transactions (needs payer key + spend cap)")
    r.add_argument("--max-spend-sol", type=float, default=float(os.environ.get("ITB_MAX_SPEND_SOL", 0.05)))
    r.add_argument("--payer", default=os.environ.get("ITB_PAYER_KEYPAIR", "/keys/payer.json"))
    r.add_argument("--k", type=int, default=8)
    r.add_argument("--bursts-per-validator", type=int, default=int(os.environ.get("ITB_BURSTS_PER_VALIDATOR", 6)))
    r.add_argument("--validators-per-client", type=int, default=int(os.environ.get("ITB_VALIDATORS_PER_CLIENT", 2)))
    r.add_argument("--horizon-slots", type=int, default=int(os.environ.get("ITB_HORIZON_SLOTS", 20000)), help="how far ahead to look for leader windows")
    r.add_argument("--clients", default=None, help="comma list of clientIds to target")
    r.add_argument("--seed", type=int, default=None)
    r.add_argument("--no-memo", action="store_true")
    r.add_argument("--localnet", action="store_true", help="target solana-test-validator (pipeline test)")
    r.add_argument("--arms", default=None, help="comma list payer:timing:gap_ms, e.g. independent:pre:0,shared:mid:3")
    c = sub.add_parser("collect", help="locate probes in blocks for a run")
    c.add_argument("run_dir", nargs="?")
    a = sub.add_parser("analyze", help="statistics, tables, plots for a run")
    a.add_argument("run_dir", nargs="?")
    v = sub.add_parser("verify", help="re-check every landed probe's slot/index/leader against RPC (no keys)")
    v.add_argument("run_dir", nargs="?")
    sub.add_parser("all", help="run (dry by default) -> collect -> analyze; honours ITB_LIVE=1")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return asyncio.run(_dispatch(args))


def _latest(data):
    runs = sorted(glob.glob(os.path.join(data, "runs", "*")))
    if not runs:
        sys.exit("no runs yet")
    return runs[-1]


async def _dispatch(args):
    rpc = Rpc(args.rpc)
    try:
        if args.cmd == "snapshot":
            from .cluster import client_breakdown, snapshot
            s = await snapshot(rpc)
            for k, n, pct in client_breakdown(s)[:25]:
                print(f"{k:34} nodes={n:5} stake={pct:6.2f}%")
        elif args.cmd == "passive":
            from .passive import survey
            import time
            await survey(rpc, os.path.join(args.data, "passive-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())),
                         per_client=args.per_client)
        elif args.cmd in ("run", "all"):
            from .experiment import Config, run
            live = getattr(args, "live", False) or os.environ.get("ITB_LIVE") == "1"
            cfg = Config(data_dir=args.data, live=live,
                         max_spend_sol=getattr(args, "max_spend_sol", float(os.environ.get("ITB_MAX_SPEND_SOL", 0.05))),
                         k=getattr(args, "k", 8), bursts_per_validator=getattr(args, "bursts_per_validator", int(os.environ.get("ITB_BURSTS_PER_VALIDATOR", 6))),
                         validators_per_client=getattr(args, "validators_per_client", int(os.environ.get("ITB_VALIDATORS_PER_CLIENT", 2))),
                         seed=getattr(args, "seed", None) if getattr(args, "seed", None) is not None else (int(os.environ["ITB_SEED"]) if os.environ.get("ITB_SEED") else None), use_memo=not getattr(args, "no_memo", False),
                         localnet=getattr(args, "localnet", False))
            cfg.horizon_slots = getattr(args, "horizon_slots", int(os.environ.get("ITB_HORIZON_SLOTS", 20000)))
            if getattr(args, "arms", None):
                cfg.arms = args.arms.split(",")
            if getattr(args, "clients", None):
                cfg.clients = args.clients.split(",")
            rdir = await run(cfg, rpc, getattr(args, "payer", os.environ.get("ITB_PAYER_KEYPAIR", "/keys/payer.json")))
            print(rdir)
            if args.cmd == "all":
                from .analyze import analyze
                from .collect import collect
                if live:
                    await __import__("asyncio").sleep(20)  # let blocks confirm
                await collect(rpc, rdir)
                analyze(rdir)
        elif args.cmd == "collect":
            from .collect import collect
            await collect(rpc, args.run_dir or _latest(args.data))
        elif args.cmd == "verify":
            from .verify import verify
            await verify(rpc, args.run_dir or _latest(args.data))
        elif args.cmd == "analyze":
            from .analyze import analyze
            res = analyze(args.run_dir or _latest(args.data))
            print(json.dumps(res["per_validator"], indent=1, default=str)[:4000])
    finally:
        await rpc.close()


if __name__ == "__main__":
    main()
