"""Validator inventory: identity -> client / version / stake / TPU address.

Client identification uses the `clientId` field that gossip ContactInfo now
carries and `getClusterNodes` exposes (e.g. Agave, JitoLabs, AgaveBam,
HarmonicAgave, Firedancer, HarmonicFiredancer, FireBAM, Rakurai, Raiku) plus
the `version` string. Both are self-reported by the node; see README
"What this does NOT separate".
"""
from __future__ import annotations

import collections
import time
from dataclasses import asdict, dataclass

from .rpc import Rpc


@dataclass
class Node:
    identity: str
    client: str
    version: str
    stake: int
    tpu_quic: str | None
    tpu_udp: str | None
    vote_account: str | None
    gossip: str | None = None
    tpu_proxied: bool | None = None  # TPU IP != gossip IP: ingress fronted by a relayer/BAM/remote TPU (heuristic)

    @property
    def client_version(self) -> str:
        return f"{self.client}/{self.version}"


def _proxied(tpu: str | None, gossip: str | None) -> bool | None:
    if not tpu or not gossip:
        return None
    return tpu.rsplit(":", 1)[0] != gossip.rsplit(":", 1)[0]


async def snapshot(rpc: Rpc) -> dict:
    nodes = await rpc.call("getClusterNodes")
    votes = await rpc.call("getVoteAccounts")
    epoch = await rpc.call("getEpochInfo", [{"commitment": "confirmed"}])
    stake = {v["nodePubkey"]: (v["activatedStake"], v["votePubkey"]) for v in votes["current"] + votes["delinquent"]}
    out = {}
    for n in nodes:
        st, va = stake.get(n["pubkey"], (0, None))
        out[n["pubkey"]] = asdict(Node(n["pubkey"], n.get("clientId") or "unknown", n.get("version") or "unknown",
                                       st, n.get("tpuQuic"), n.get("tpu"), va, n.get("gossip"),
                                       _proxied(n.get("tpuQuic"), n.get("gossip"))))
    return {"taken_at_unix": time.time(), "epoch": epoch, "rpc": rpc.redacted_url, "nodes": out}


def client_breakdown(snap: dict) -> list[tuple[str, int, float]]:
    tot = sum(n["stake"] for n in snap["nodes"].values()) or 1
    s, c = collections.Counter(), collections.Counter()
    for n in snap["nodes"].values():
        k = f'{n["client"]}/{n["version"]}'
        s[k] += n["stake"]
        c[k] += 1
    return [(k, c[k], 100 * v / tot) for k, v in s.most_common()]
