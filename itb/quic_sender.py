"""Minimal Solana TPU-over-QUIC sender (no Agave dependency).

Protocol (as implemented by Agave's streamer and Firedancer's quic tile):
  * QUIC v1, ALPN "solana-tpu", TLS 1.3, client presents a self-signed
    Ed25519 certificate (its public key is the client "identity"; an
    identity with no stake is treated as unstaked by stake-weighted QoS).
  * one transaction per unidirectional stream, stream is FIN-ed right after
    the wire bytes.
We deliberately use an *unstaked* identity: that is the path any ordinary
user has, and it is documented as a limitation in the README.
"""
from __future__ import annotations

import asyncio
import datetime as dt
import ssl
import time
from dataclasses import dataclass

from aioquic.asyncio import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.x509.oid import NameOID

ALPN = "solana-tpu"


def _self_signed_cert(tmpdir: str) -> tuple[str, str]:
    key = ed25519.Ed25519PrivateKey.generate()
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Solana node")])
    now = dt.datetime.now(dt.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - dt.timedelta(days=1))
        .not_valid_after(now + dt.timedelta(days=365))
        .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
        .sign(key, None)
    )
    cp, kp = f"{tmpdir}/client.crt", f"{tmpdir}/client.key"
    with open(cp, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open(kp, "wb") as f:
        f.write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                  serialization.NoEncryption()))
    return cp, kp


@dataclass
class SendRecord:
    idx: int
    t_send_ns: int  # wall clock (time.time_ns) when the stream was written
    ok: bool
    err: str | None = None


class TpuQuicSender:
    """One QUIC connection to one TPU address. Use as async context manager."""

    def __init__(self, host: str, port: int, tmpdir: str = "/tmp", timeout: float = 3.0):
        self.host, self.port, self.timeout = host, port, timeout
        cfg = QuicConfiguration(is_client=True, alpn_protocols=[ALPN], verify_mode=ssl.CERT_NONE,
                                server_name="connect", idle_timeout=10.0)
        cfg.load_cert_chain(*_self_signed_cert(tmpdir))
        self._cfg = cfg
        self._cm = None
        self.proto: QuicConnectionProtocol | None = None
        self.connect_ms: float | None = None

    async def __aenter__(self):
        t0 = time.perf_counter()
        self._cm = connect(self.host, self.port, configuration=self._cfg, wait_connected=True)
        self.proto = await asyncio.wait_for(self._cm.__aenter__(), self.timeout)
        self.connect_ms = (time.perf_counter() - t0) * 1e3
        return self

    async def __aexit__(self, *exc):
        if self._cm is not None:
            try:
                await asyncio.wait_for(self._cm.__aexit__(None, None, None), 2.0)
            except Exception:
                pass

    def send(self, idx: int, wire: bytes) -> SendRecord:
        """Write one transaction on a fresh uni stream (non-blocking)."""
        q = self.proto._quic
        try:
            sid = q.get_next_available_stream_id(is_unidirectional=True)
            t = time.time_ns()
            q.send_stream_data(sid, wire, end_stream=True)
            self.proto.transmit()
            return SendRecord(idx, t, True)
        except Exception as e:  # stream limit etc.
            return SendRecord(idx, time.time_ns(), False, repr(e))
