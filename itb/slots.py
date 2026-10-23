"""Live slot clock from `slotSubscribe` (WebSocket), with an RPC-poll fallback."""
from __future__ import annotations

import asyncio
import json
import logging
import time

import websockets

from .rpc import Rpc

log = logging.getLogger("itb.slots")


def ws_url(http_url: str) -> str:
    return http_url.replace("https://", "wss://").replace("http://", "ws://").replace(":8899", ":8900")


class SlotClock:
    def __init__(self, rpc: Rpc, ws: str | None = None):
        self.rpc = rpc
        self.ws = ws or ws_url(rpc.url)
        self.slot = 0
        self.t = 0.0  # monotonic time of last update
        self.source = None
        self._task = None
        self._event = asyncio.Event()
        self.history: list[tuple[float, int]] = []

    def _update(self, slot: int, src: str):
        if slot > self.slot:
            self.slot, self.t, self.source = slot, time.monotonic(), src
            self.history.append((time.time(), slot))
            self.history = self.history[-2000:]
            self._event.set()
            self._event = asyncio.Event()

    async def _ws_loop(self):
        while True:
            try:
                async with websockets.connect(self.ws, ping_interval=20, max_size=2**20) as ws:
                    await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "slotSubscribe"}))
                    async for raw in ws:
                        m = json.loads(raw)
                        if m.get("method") == "slotNotification":
                            self._update(m["params"]["result"]["slot"], "ws")
            except Exception as e:  # reconnect, meanwhile poll
                log.warning("slot ws error %s; polling", e)
                for _ in range(2):
                    try:
                        self._update(await self.rpc.call("getSlot", [{"commitment": "processed"}]), "poll")
                    except Exception:
                        pass
                    await asyncio.sleep(0.4)

    async def start(self):
        self._task = asyncio.create_task(self._ws_loop())
        for _ in range(100):
            if self.slot:
                return
            await asyncio.sleep(0.1)
        raise RuntimeError("no slot updates")

    async def stop(self):
        if self._task:
            self._task.cancel()

    def ms_per_slot(self) -> float:
        h = [x for x in self.history if x[0] > time.time() - 30]
        if len(h) < 5:
            return 400.0
        return 1000 * (h[-1][0] - h[0][0]) / max(h[-1][1] - h[0][1], 1)

    async def wait_for(self, slot: int, timeout: float | None = None) -> int:
        if timeout is None:  # generous: distance at 0.3 s/slot + 60 s
            timeout = max(slot - self.slot, 0) * 0.3 + 60
        end = time.monotonic() + timeout
        while self.slot < slot:
            if time.monotonic() > end:
                raise TimeoutError(f"slot {slot} not reached (at {self.slot})")
            try:
                await asyncio.wait_for(self._event.wait(), 1.0)
            except asyncio.TimeoutError:
                pass
        return self.slot
