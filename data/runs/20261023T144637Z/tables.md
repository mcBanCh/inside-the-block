## By producing client (leader that actually built the block) × arm

Bursts with ≥3 landed probes, all in blocks of one leader. `forwarded` = produced by a leader other than the one targeted.

| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | perfectly fee-sorted | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | shared:* | 1 | 1 | 0 | 0.07 – | 0/1 | 1.00 – | insufficient data |
| Agave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | 0.07 – | 0/1 | 1.00 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:* | 1 | 1 | 1 | 0.79 – | 0/1 | 0.36 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:pre:0 | 1 | 1 | 1 | 0.79 – | 0/1 | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:* | 1 | 1 | 0 | 0.79 – | 0/1 | 0.79 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:pre:0 | 1 | 1 | 0 | 0.79 – | 0/1 | 0.79 – | insufficient data |

## By targeted validator × arm

| client/version | validator | arm | bursts | sent→landed | τ fee (95% CI) | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | `5Us18hLZ…` | shared:pre:0.0 | 1 | 8→8 | 0.07 – | 1.00 – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | all:all | 1 | 8→8 | 0.07 – | 1.00 – | insufficient data |
| AgaveBam/4.3.2 | `BUv44cVt…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `BUv44cVt…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `BUv44cVt…` | all:all | 2 | 16→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `CQdLgwkm…` | shared:pre:0.0 | 1 | 8→8 | 0.79 – | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `CQdLgwkm…` | all:all | 1 | 8→8 | 0.79 – | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `JUPiTERr…` | shared:pre:0.0 | 1 | 8→8 | 0.79 – | 0.79 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `JUPiTERr…` | all:all | 1 | 8→8 | 0.79 – | 0.79 – | insufficient data |
| JitoLabs/4.3.2 | `EUcJwf7j…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `EUcJwf7j…` | all:all | 1 | 8→0 | – – | – – | insufficient data |

## Per burst

| burst | targeted client | arm | status | landed | slot offset | producer = target | slots | first idx / block | span | τ fee | τ send |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | JitoLabs/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 1 | AgaveBam/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 2 | AgaveBam/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 3 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 40 | False (HarmonicAgave/4.3.2) | 1 | 1/365 | 22 | 0.79 | 0.36 |
| 4 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 1 | True (HarmonicFiredancer/26.10.4) | 1 | 7/783 | 55 | 0.79 | 0.79 |
| 5 | Agave/4.3.2 | shared:pre:0.0 | sent | 8/8 | 3 | True (Agave/4.3.2) | 1 | 475/516 | 8 | 0.07 | 1.00 |
