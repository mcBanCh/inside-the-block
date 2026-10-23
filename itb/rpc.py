"""Tiny async JSON-RPC client with retry/backoff (public endpoints rate-limit hard)."""
from __future__ import annotations

import asyncio
import logging
import os

import httpx

log = logging.getLogger("itb.rpc")
DEFAULT_RPC = "https://api.mainnet-beta.solana.com"


class RpcError(RuntimeError):
    pass


class Rpc:
    def __init__(self, url: str | None = None, timeout: float = 30.0, min_interval: float | None = None):
        self.url = url or os.environ.get("ITB_RPC_URL") or DEFAULT_RPC
        self._c = httpx.AsyncClient(timeout=timeout, http2=False)
        # public mainnet RPC: ~100 req / 10 s per IP -> stay well below
        self.min_interval = min_interval if min_interval is not None else (
            0.25 if "api.mainnet-beta.solana.com" in self.url else 0.0)
        self._lock = asyncio.Lock()
        self._last = 0.0
        self.calls = 0

    @property
    def redacted_url(self) -> str:
        """URL safe for logs (drops query string, which often carries API keys)."""
        return self.url.split("?")[0]

    async def call(self, method: str, params=None, retries: int = 6):
        params = [] if params is None else params
        delay = 0.5
        for attempt in range(retries):
            async with self._lock:
                wait = self._last + self.min_interval - asyncio.get_running_loop().time()
                if wait > 0:
                    await asyncio.sleep(wait)
                self._last = asyncio.get_running_loop().time()
            try:
                self.calls += 1
                r = await self._c.post(self.url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
                if r.status_code == 429 or r.status_code >= 500:
                    raise RpcError(f"HTTP {r.status_code}")
                j = r.json()
                if "error" in j:
                    err = j["error"]
                    # -32004 / -32007 / -32009: block not available (yet) / skipped / missing in storage
                    if err.get("code") in (-32004, -32014) and attempt < retries - 1:
                        raise RpcError(str(err))
                    e = RpcError(f"{method}: {err}")
                    e.fatal = True
                    raise e
                return j["result"]
            except (httpx.HTTPError, RpcError) as e:
                msg = str(e)
                if getattr(e, "fatal", False) or ("skipped" in msg or "-32007" in msg or "-32009" in msg) or attempt == retries - 1:
                    raise RpcError(msg) from e
                log.debug("rpc %s retry %d: %s", method, attempt, msg)
                await asyncio.sleep(delay)
                delay = min(delay * 2, 8)

    async def close(self):
        await self._c.aclose()
