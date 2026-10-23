## By producing client (leader that actually built the block) × arm

Bursts with ≥3 landed probes, all in blocks of one leader. `forwarded` = produced by a leader other than the one targeted.

| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | perfectly fee-sorted | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | shared:* | 1 | 1 | 0 | -0.07 – | 0/1 | 1.00 – | insufficient data |
| Agave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | -0.07 – | 0/1 | 1.00 – | insufficient data |
| AgaveBam/4.3.2 | independent:* | 1 | 1 | 0 | 0.79 – | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | independent:mid:0 | 1 | 1 | 0 | 0.79 – | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | shared:* | 1 | 1 | 1 | 1.00 – | 1/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | shared:pre:0 | 1 | 1 | 1 | 1.00 – | 1/1 | 0.07 – | insufficient data |
| Firedancer/26.10.4 | independent:* | 1 | 1 | 0 | -0.50 – | 0/1 | -0.21 – | insufficient data |
| Firedancer/26.10.4 | independent:mid:0 | 1 | 1 | 0 | -0.50 – | 0/1 | -0.21 – | insufficient data |
| Firedancer/26.10.4 | shared:* | 3 | 2 | 0 | 0.19 [-0.29, 1.00] | 1/3 | 0.62 [-0.14, 1.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | shared:pre:0 | 1 | 1 | 0 | -0.14 – | 0/1 | 1.00 – | insufficient data |
| Firedancer/26.10.4 | shared:pre:3 | 2 | 2 | 0 | 0.36 [-0.29, 1.00] | 1/2 | 0.43 [-0.14, 1.00] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:* | 5 | 5 | 5 | 0.27 [0.10, 0.50] | 0/5 | 0.01 [-0.13, 0.16] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:0 | 3 | 3 | 3 | 0.19 [0.07, 0.29] | 0/3 | -0.02 [-0.21, 0.29] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.71 – | 0/1 | 0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | independent:pre:0 | 1 | 1 | 1 | 0.07 – | 0/1 | 0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:* | 2 | 1 | 0 | 0.57 [0.29, 0.86] | 0/2 | 0.25 [-0.07, 0.57] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | shared:mid:0 | 1 | 1 | 0 | 0.86 – | 0/1 | -0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:pre:3 | 1 | 1 | 0 | 0.29 – | 0/1 | 0.57 – | insufficient data |
| HarmonicFiredancer/26.10.4 | independent:* | 3 | 3 | 3 | 0.55 [-0.14, 0.93] | 0/3 | -0.14 [-0.50, 0.14] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | independent:mid:0 | 1 | 1 | 1 | 0.93 – | 0/1 | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | independent:pre:0 | 2 | 2 | 2 | 0.36 [-0.14, 0.86] | 0/2 | -0.29 [-0.50, -0.07] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | shared:* | 4 | 3 | 3 | 0.93 [0.88, 0.98] | 1/4 | -0.07 [-0.45, 0.21] | fee-priority (25% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | shared:mid:0 | 1 | 1 | 1 | 0.93 – | 0/1 | -0.07 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:pre:0 | 2 | 1 | 2 | 0.93 [0.86, 1.00] | 1/2 | -0.18 [-0.64, 0.29] | fee-priority (50% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | shared:pre:3 | 1 | 1 | 0 | 0.93 – | 0/1 | 0.14 – | insufficient data |

## By targeted validator × arm

| client/version | validator | arm | bursts | sent→landed | τ fee (95% CI) | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | `5Us18hLZ…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:pre:0.0 | 1 | 8→8 | -0.07 – | 1.00 – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | all:all | 6 | 32→8 | -0.07 – | 1.00 – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | all:all | 5 | 24→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | all:all | 4 | 16→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | independent:mid:0.0 | 1 | 8→8 | 0.79 – | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `HSDTxfgr…` | all:all | 5 | 24→8 | 0.79 – | 0.07 – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | shared:pre:0.0 | 1 | 8→8 | 1.00 – | 0.07 – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9pBHfuE1…` | all:all | 6 | 40→8 | 1.00 – | 0.07 – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `SSmBEooM…` | all:all | 6 | 32→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:mid:0.0 | 1 | 8→8 | -0.50 – | -0.21 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | shared:pre:0.0 | 1 | 8→8 | -0.14 – | 1.00 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | shared:pre:3.0 | 1 | 8→8 | -0.29 – | 1.00 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | all:all | 5 | 40→24 | -0.31 [-0.50, -0.14] | 0.60 [-0.21, 1.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | `RNXnAJV1…` | independent:mid:3.0 | 1 | 8→1 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `RNXnAJV1…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `RNXnAJV1…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `RNXnAJV1…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `RNXnAJV1…` | shared:pre:3.0 | 1 | 8→8 | 1.00 – | -0.14 – | insufficient data |
| Firedancer/26.10.4 | `RNXnAJV1…` | all:all | 5 | 24→9 | 1.00 – | -0.14 – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | independent:mid:0.0 | 1 | 8→8 | 0.93 – | 0.14 – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | independent:pre:0.0 | 1 | 8→8 | 0.07 – | 0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `3psxMyr7…` | all:all | 6 | 24→16 | 0.50 [0.07, 0.93] | 0.11 [0.07, 0.14] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | independent:mid:0.0 | 1 | 8→8 | 0.29 – | -0.21 – | insufficient data |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | shared:mid:0.0 | 1 | 8→8 | 0.86 – | -0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | shared:pre:3.0 | 1 | 8→8 | 0.29 – | 0.57 – | insufficient data |
| HarmonicAgave/4.3.2 | `HTeRsa3g…` | all:all | 5 | 32→24 | 0.48 [0.29, 0.86] | 0.10 [-0.21, 0.57] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | independent:mid:0.0 | 1 | 8→8 | 0.07 – | -0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | independent:mid:3.0 | 1 | 8→8 | 0.71 – | 0.07 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | independent:pre:0.0 | 1 | 8→8 | 0.86 – | -0.50 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | shared:mid:0.0 | 1 | 8→8 | 0.93 – | -0.07 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | shared:pre:0.0 | 1 | 8→8 | 1.00 – | -0.64 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6yFGGAgY…` | all:all | 6 | 40→40 | 0.71 [0.39, 0.94] | -0.26 [-0.49, -0.03] | fee-priority (20% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | independent:mid:0.0 | 1 | 8→8 | 0.21 – | 0.29 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | independent:pre:0.0 | 1 | 8→8 | -0.14 – | -0.07 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | shared:pre:0.0 | 1 | 8→8 | 0.86 – | 0.29 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | shared:pre:3.0 | 1 | 8→8 | 0.93 – | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `grptonHn…` | all:all | 6 | 32→32 | 0.46 [0.04, 0.89] | 0.16 [0.02, 0.29] | no rule detected (consistent with noise at this n) |
| JitoLabs/4.3.2 | `C8Bey3LK…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `C8Bey3LK…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `C8Bey3LK…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `C8Bey3LK…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `C8Bey3LK…` | all:all | 4 | 32→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `FbYX2uN5…` | all:all | 6 | 32→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `E3mDbFMr…` | all:all | 6 | 24→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | all:all | 4 | 16→0 | – – | – – | insufficient data |

## Per burst

| burst | targeted client | arm | status | landed | slot offset | producer = target | slots | first idx / block | span | τ fee | τ send |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | JitoLabs/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 1 | JitoLabs/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 2 | Firedancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 1 | True (Firedancer/26.10.4) | 1 | 116/586 | 9 | -0.14 | 1.00 |
| 3 | Firedancer/26.10.4 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 4 | JitoLabs/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 5 | FireBAM/26.10.4 | shared:pre:0.0 | sent | 8/8 | 20 | False (AgaveBam/4.3.2) | 1 | 84/657 | 51 | 1.00 | 0.07 |
| 6 | HarmonicAgave/4.3.2 | shared:pre:0.0 | late_trigger_skipped (clock at 460501212 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 7 | AgaveBam/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 8 | Firedancer/26.10.4 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 9 | HarmonicAgave/4.3.2 | independent:pre:0.0 | sent | 8/8 | 128 | False (HarmonicAgave/4.3.2) | 1 | 0/462 | 16 | 0.07 | 0.07 |
| 10 | AgaveBam/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460501581 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 11 | AgaveBam/4.3.2 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 12 | Firedancer/26.10.4 | shared:pre:3.0 | sent | 8/8 | 0 | True (Firedancer/26.10.4) | 1 | 228/1014 | 26 | -0.29 | 1.00 |
| 13 | Agave/4.3.2 | shared:pre:0.0 | sent | 8/8 | 2 | True (Agave/4.3.2) | 1 | 222/422 | 8 | -0.07 | 1.00 |
| 14 | JitoLabs/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 15 | JitoLabs/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 16 | Firedancer/26.10.4 | independent:mid:0.0 | sent | 8/8 | 40 | True (Firedancer/26.10.4) | 1 | 25/599 | 20 | -0.50 | -0.21 |
| 17 | Rakurai/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460502127 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 18 | AgaveBam/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 19 | AgaveBam/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 20 | AgaveBam/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 21 | HarmonicAgave/4.3.2 | shared:mid:0.0 | late_trigger_skipped (clock at 460502454 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 22 | FireBAM/26.10.4 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 23 | JitoLabs/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460502532 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 24 | Rakurai/4.3.2 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 25 | FireBAM/26.10.4 | shared:pre:0.0 | late_trigger_skipped (clock at 460502722 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 26 | AgaveBam/4.3.2 | shared:pre:3.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 27 | JitoLabs/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 28 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 21 | False (HarmonicFiredancer/26.10.4) | 1 | 107/397 | 16 | 0.86 | 0.29 |
| 29 | HarmonicAgave/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460502980 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 30 | HarmonicAgave/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 31 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 76 | False (HarmonicFiredancer/26.10.4) | 1 | 7/835 | 8 | 1.00 | -0.64 |
| 32 | Agave/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460503134 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 33 | HarmonicAgave/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460503247 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 34 | Agave/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 35 | Firedancer/26.10.4 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 36 | AgaveBam/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460503489 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 37 | HarmonicAgave/4.3.2 | shared:mid:0.0 | sent | 8/8 | 32 | True (HarmonicAgave/4.3.2) | 1 | 5/739 | 66 | 0.86 | -0.07 |
| 38 | HarmonicAgave/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 39 | JitoLabs/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 40 | Rakurai/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 41 | Rakurai/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 42 | Agave/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460504156 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 43 | HarmonicAgave/4.3.2 | independent:mid:0.0 | sent | 8/8 | 28 | False (HarmonicFiredancer/26.10.4) | 1 | 112/1244 | 72 | 0.93 | 0.14 |
| 44 | Rakurai/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460504262 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 45 | AgaveBam/4.3.2 | independent:mid:0.0 | sent | 8/8 | 2 | True (AgaveBam/4.3.2) | 1 | 280/411 | 9 | 0.79 | 0.07 |
| 46 | HarmonicAgave/4.3.2 | shared:pre:3.0 | sent | 8/8 | 2 | True (HarmonicAgave/4.3.2) | 1 | 400/906 | 142 | 0.29 | 0.57 |
| 47 | HarmonicFiredancer/26.10.4 | independent:pre:0.0 | sent | 8/8 | 24 | False (HarmonicFiredancer/26.10.4) | 1 | 2/559 | 17 | 0.86 | -0.50 |
| 48 | HarmonicAgave/4.3.2 | independent:mid:0.0 | sent | 8/8 | 64 | False (HarmonicAgave/4.3.2) | 1 | 1/744 | 20 | 0.29 | -0.21 |
| 49 | Agave/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 50 | HarmonicFiredancer/26.10.4 | independent:pre:0.0 | sent | 8/8 | 15 | False (HarmonicFiredancer/26.10.4) | 1 | 190/710 | 46 | -0.14 | -0.07 |
| 51 | Agave/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 52 | HarmonicFiredancer/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460505590 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 53 | Agave/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 54 | Agave/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 55 | JitoLabs/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 56 | JitoLabs/4.3.2 | independent:mid:0.0 | late_trigger_skipped (clock at 460506235 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 57 | Rakurai/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 58 | Agave/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460506880 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 59 | Agave/4.3.2 | independent:mid:0.0 | late_trigger_skipped (clock at 460507051 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 60 | FireBAM/26.10.4 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 61 | Rakurai/4.3.2 | shared:mid:0.0 | late_trigger_skipped (clock at 460507658 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 62 | Agave/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 63 | Firedancer/26.10.4 | independent:pre:0.0 | late_trigger_skipped (clock at 460509055 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 64 | Firedancer/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460509198 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 65 | Rakurai/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 66 | FireBAM/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460510360 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 67 | HarmonicFiredancer/26.10.4 | shared:mid:0.0 | sent | 8/8 | 40 | False (HarmonicFiredancer/26.10.4) | 1 | 131/995 | 54 | 0.93 | -0.07 |
| 68 | Rakurai/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 69 | HarmonicFiredancer/26.10.4 | independent:mid:3.0 | sent | 8/8 | 32 | False (HarmonicAgave/4.3.2) | 1 | 0/246 | 11 | 0.71 | 0.07 |
| 70 | Firedancer/26.10.4 | independent:mid:3.0 | sent | 1/8 | 3 | True (Firedancer/26.10.4) | 1 | 313/316 | 1 | – | – |
| 71 | Firedancer/26.10.4 | shared:pre:3.0 | sent | 8/8 | 1 | True (Firedancer/26.10.4) | 2 | 263/622 | 356 | 1.00 | -0.14 |
| 72 | HarmonicFiredancer/26.10.4 | independent:mid:3.0 | late_trigger_skipped (clock at 460512477 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 73 | HarmonicFiredancer/26.10.4 | shared:pre:3.0 | late_trigger_skipped (clock at 460512737 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 74 | FireBAM/26.10.4 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 75 | FireBAM/26.10.4 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 76 | FireBAM/26.10.4 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 77 | FireBAM/26.10.4 | independent:mid:3.0 | late_trigger_skipped (clock at 460514308 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 78 | Rakurai/4.3.2 | independent:mid:0.0 | late_trigger_skipped (clock at 460515274 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 79 | FireBAM/26.10.4 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 80 | HarmonicFiredancer/26.10.4 | independent:mid:0.0 | sent | 8/8 | 36 | False (HarmonicAgave/4.3.2) | 1 | 0/331 | 12 | 0.07 | -0.14 |
| 81 | HarmonicFiredancer/26.10.4 | shared:pre:3.0 | sent | 8/8 | 2 | True (HarmonicFiredancer/26.10.4) | 1 | 109/334 | 80 | 0.93 | 0.14 |
| 82 | HarmonicFiredancer/26.10.4 | independent:mid:0.0 | sent | 8/8 | 52 | False (HarmonicAgave/4.3.2) | 1 | 5/618 | 55 | 0.21 | 0.29 |
| 83 | FireBAM/26.10.4 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 84 | FireBAM/26.10.4 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
