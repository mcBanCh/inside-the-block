## By producing client (leader that actually built the block) × arm

Bursts with ≥3 landed probes, all in blocks of one leader. `forwarded` = produced by a leader other than the one targeted.

| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | perfectly fee-sorted | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | shared:* | 1 | 1 | 0 | 1.00 – | 1/1 | -0.14 – | insufficient data |
| Agave/4.3.2 | shared:pre:3 | 1 | 1 | 0 | 1.00 – | 1/1 | -0.14 – | insufficient data |
| AgaveBam/4.3.2 | independent:* | 1 | 1 | 1 | 0.93 – | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.93 – | 0/1 | 0.07 – | insufficient data |
| Firedancer/26.10.4 | independent:* | 3 | 2 | 0 | 0.14 [-0.36, 1.00] | 1/3 | 0.43 [0.00, 1.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | independent:mid:0 | 1 | 1 | 0 | 1.00 – | 1/1 | 0.00 – | insufficient data |
| Firedancer/26.10.4 | independent:mid:3 | 1 | 1 | 0 | -0.36 – | 0/1 | 1.00 – | insufficient data |
| Firedancer/26.10.4 | independent:pre:0 | 1 | 1 | 0 | -0.21 – | 0/1 | 0.29 – | insufficient data |
| Firedancer/26.10.4 | shared:* | 2 | 2 | 0 | 0.64 [0.29, 1.00] | 1/2 | -0.14 [-0.29, 0.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | shared:pre:0 | 1 | 1 | 0 | 0.29 – | 0/1 | 0.00 – | insufficient data |
| Firedancer/26.10.4 | shared:pre:3 | 1 | 1 | 0 | 1.00 – | 1/1 | -0.29 – | insufficient data |
| HarmonicAgave/4.3.2 | independent:* | 3 | 3 | 2 | 0.10 [-0.36, 0.36] | 0/3 | -0.02 [-0.36, 0.50] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:0 | 2 | 2 | 1 | -0.04 [-0.36, 0.29] | 0/2 | 0.07 [-0.36, 0.50] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.36 – | 0/1 | -0.21 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:* | 4 | 4 | 3 | 0.73 [0.57, 0.84] | 0/4 | -0.07 [-0.37, 0.23] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:mid:0 | 2 | 2 | 2 | 0.79 [0.79, 0.79] | 0/2 | -0.07 [-0.14, 0.00] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | 0.86 – | 0/1 | -0.50 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:pre:3 | 1 | 1 | 1 | 0.50 – | 0/1 | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | independent:* | 3 | 3 | 1 | 0.48 [-0.21, 0.93] | 0/3 | 0.17 [-0.43, 0.79] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | independent:mid:3 | 2 | 2 | 1 | 0.82 [0.71, 0.93] | 0/2 | 0.18 [-0.43, 0.79] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | independent:pre:0 | 1 | 1 | 0 | -0.21 – | 0/1 | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:* | 1 | 1 | 1 | 1.00 – | 1/1 | 0.29 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:pre:3 | 1 | 1 | 1 | 1.00 – | 1/1 | 0.29 – | insufficient data |
| Rakurai/4.3.2 | independent:* | 1 | 1 | 0 | 0.50 – | 0/1 | -0.64 – | insufficient data |
| Rakurai/4.3.2 | independent:pre:0 | 1 | 1 | 0 | 0.50 – | 0/1 | -0.64 – | insufficient data |

## By targeted validator × arm

| client/version | validator | arm | bursts | sent→landed | τ fee (95% CI) | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|
| Agave/4.3.2 | `5Us18hLZ…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `5Us18hLZ…` | all:all | 6 | 24→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | shared:pre:3.0 | 1 | 8→8 | 1.00 – | -0.14 – | insufficient data |
| Agave/4.3.2 | `7QQGNm3p…` | all:all | 6 | 32→8 | 1.00 – | -0.14 – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `6TkKqq15…` | all:all | 5 | 32→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | independent:mid:3.0 | 1 | 8→8 | 0.93 – | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| AgaveBam/4.3.2 | `Aw5wEMXh…` | all:all | 6 | 24→8 | 0.93 – | 0.07 – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | independent:mid:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| FireBAM/26.10.4 | `9jxgosAf…` | all:all | 6 | 24→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `EvnRmnMr…` | independent:mid:0.0 | 1 | 8→8 | 1.00 – | 0.00 – | insufficient data |
| Firedancer/26.10.4 | `EvnRmnMr…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `EvnRmnMr…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `EvnRmnMr…` | shared:pre:3.0 | 1 | 8→8 | 1.00 – | -0.29 – | insufficient data |
| Firedancer/26.10.4 | `EvnRmnMr…` | all:all | 4 | 24→16 | 1.00 [1.00, 1.00] | -0.14 [-0.29, 0.00] | fee-priority (100% of bursts perfectly fee-sorted) |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:mid:3.0 | 1 | 8→8 | -0.36 – | 1.00 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | independent:pre:0.0 | 1 | 8→8 | -0.21 – | 0.29 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | shared:pre:0.0 | 1 | 8→8 | 0.29 – | 0.00 – | insufficient data |
| Firedancer/26.10.4 | `JD549Hsb…` | all:all | 5 | 24→24 | -0.10 [-0.36, 0.29] | 0.43 [0.00, 1.00] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | independent:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | independent:mid:3.0 | 1 | 8→8 | 0.36 – | -0.21 – | insufficient data |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | shared:mid:0.0 | 1 | 8→8 | 0.79 – | 0.00 – | insufficient data |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | shared:pre:0.0 | 1 | 8→8 | 0.86 – | -0.50 – | insufficient data |
| HarmonicAgave/4.3.2 | `CAo1dCGY…` | all:all | 5 | 32→24 | 0.67 [0.36, 0.86] | -0.24 [-0.50, 0.00] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | independent:mid:0.0 | 1 | 8→8 | -0.36 – | 0.50 – | insufficient data |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | independent:mid:3.0 | 1 | 8→8 | 0.93 – | -0.43 – | insufficient data |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | shared:mid:0.0 | 1 | 8→8 | 0.79 – | -0.14 – | insufficient data |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | shared:pre:3.0 | 1 | 8→8 | 1.00 – | 0.29 – | insufficient data |
| HarmonicAgave/4.3.2 | `G3a3iYZK…` | all:all | 5 | 32→32 | 0.59 [-0.04, 0.96] | 0.05 [-0.29, 0.39] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | independent:mid:0.0 | 1 | 8→8 | 0.29 – | -0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | independent:mid:3.0 | 1 | 8→8 | 0.71 – | 0.79 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | shared:pre:3.0 | 1 | 8→8 | 0.50 – | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `6ptuwW4r…` | all:all | 6 | 24→24 | 0.50 [0.29, 0.71] | 0.26 [-0.36, 0.79] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | independent:pre:0.0 | 1 | 8→8 | -0.21 – | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | shared:mid:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | shared:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| HarmonicFiredancer/26.10.4 | `HW4zorvt…` | all:all | 6 | 24→8 | -0.21 – | 0.14 – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | shared:pre:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `LeDbQ99Q…` | all:all | 5 | 24→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | independent:pre:0.0 | 1 | 0→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| JitoLabs/4.3.2 | `siidBVew…` | all:all | 6 | 32→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | independent:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `7PdKhpKz…` | all:all | 5 | 32→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | independent:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | independent:mid:3.0 | 1 | 0→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | independent:pre:0.0 | 1 | 8→8 | 0.50 – | -0.64 – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | shared:mid:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | shared:pre:0.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | shared:pre:3.0 | 1 | 8→0 | – – | – – | insufficient data |
| Rakurai/4.3.2 | `ana2y2Yv…` | all:all | 6 | 40→8 | 0.50 – | -0.64 – | insufficient data |

## Per burst

| burst | targeted client | arm | status | landed | slot offset | producer = target | slots | first idx / block | span | τ fee | τ send |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | HarmonicAgave/4.3.2 | shared:pre:0.0 | sent | 8/8 | 64 | True (HarmonicAgave/4.3.2) | 1 | 16/604 | 43 | 0.86 | -0.50 |
| 1 | HarmonicAgave/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 2 | Rakurai/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 3 | Firedancer/26.10.4 | shared:pre:0.0 | sent | 8/8 | 0 | True (Firedancer/26.10.4) | 1 | 23/533 | 40 | 0.29 | 0.00 |
| 4 | Rakurai/4.3.2 | independent:pre:0.0 | sent | 8/8 | 0 | True (Rakurai/4.3.2) | 1 | 8/109 | 42 | 0.50 | -0.64 |
| 5 | HarmonicAgave/4.3.2 | shared:mid:0.0 | sent | 8/8 | 64 | False (HarmonicAgave/4.3.2) | 1 | 22/555 | 100 | 0.79 | 0.00 |
| 6 | Firedancer/26.10.4 | independent:pre:0.0 | sent | 8/8 | 32 | True (Firedancer/26.10.4) | 1 | 35/587 | 33 | -0.21 | 0.29 |
| 7 | Firedancer/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460483587 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 8 | FireBAM/26.10.4 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 9 | Firedancer/26.10.4 | independent:mid:3.0 | sent | 8/8 | 2 | True (Firedancer/26.10.4) | 1 | 105/373 | 21 | -0.36 | 1.00 |
| 10 | JitoLabs/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 11 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | late_trigger_skipped (clock at 460483867 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 12 | Firedancer/26.10.4 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 13 | HarmonicAgave/4.3.2 | independent:mid:3.0 | sent | 8/8 | 140 | False (HarmonicAgave/4.3.2) | 1 | 3/543 | 25 | 0.36 | -0.21 |
| 14 | FireBAM/26.10.4 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 15 | Agave/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 16 | Rakurai/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 17 | Firedancer/26.10.4 | independent:mid:0.0 | late_trigger_skipped (clock at 460484153 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 18 | HarmonicAgave/4.3.2 | independent:mid:0.0 | late_trigger_skipped (clock at 460484242 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 19 | Firedancer/26.10.4 | independent:mid:3.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 20 | Firedancer/26.10.4 | shared:pre:3.0 | sent | 8/8 | 92 | True (Firedancer/26.10.4) | 1 | 188/637 | 28 | 1.00 | -0.29 |
| 21 | Firedancer/26.10.4 | independent:mid:0.0 | sent | 8/8 | 80 | True (Firedancer/26.10.4) | 1 | 212/1049 | 69 | 1.00 | 0.00 |
| 22 | FireBAM/26.10.4 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 23 | FireBAM/26.10.4 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 24 | HarmonicAgave/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460484827 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 25 | Rakurai/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 26 | Rakurai/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 27 | FireBAM/26.10.4 | shared:pre:3.0 | error: TimeoutError('slot 460485230 not  | 0/0 | – | – (–) | – | –/– | – | – | – |
| 28 | AgaveBam/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460486103 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 29 | AgaveBam/4.3.2 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 30 | FireBAM/26.10.4 | independent:mid:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 31 | JitoLabs/4.3.2 | independent:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 32 | Rakurai/4.3.2 | independent:mid:3.0 | late_trigger_skipped (clock at 460486634 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 33 | HarmonicFiredancer/26.10.4 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 34 | Agave/4.3.2 | shared:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 35 | AgaveBam/4.3.2 | independent:pre:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 36 | AgaveBam/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 37 | JitoLabs/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 38 | Agave/4.3.2 | independent:pre:0.0 | late_trigger_skipped (clock at 460486808 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 39 | JitoLabs/4.3.2 | independent:mid:3.0 | late_trigger_skipped (clock at 460486862 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 40 | HarmonicFiredancer/26.10.4 | independent:pre:0.0 | late_trigger_skipped (clock at 460486900 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 41 | AgaveBam/4.3.2 | shared:mid:0.0 | late_trigger_skipped (clock at 460487226 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 42 | Agave/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 43 | HarmonicAgave/4.3.2 | shared:mid:0.0 | sent | 8/8 | 16 | False (HarmonicAgave/4.3.2) | 1 | 10/1076 | 163 | 0.79 | -0.14 |
| 44 | AgaveBam/4.3.2 | independent:mid:3.0 | sent | 8/8 | 12 | False (AgaveBam/4.3.2) | 1 | 122/702 | 43 | 0.93 | 0.07 |
| 45 | Agave/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 46 | Agave/4.3.2 | independent:mid:3.0 | late_trigger_skipped (clock at 460487929 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 47 | Rakurai/4.3.2 | independent:mid:3.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 48 | Agave/4.3.2 | shared:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 49 | HarmonicAgave/4.3.2 | independent:mid:3.0 | sent | 8/8 | 24 | False (HarmonicFiredancer/26.10.4) | 1 | 48/772 | 108 | 0.93 | -0.43 |
| 50 | Agave/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 51 | HarmonicFiredancer/26.10.4 | independent:pre:0.0 | sent | 8/8 | 16 | True (HarmonicFiredancer/26.10.4) | 1 | 313/587 | 24 | -0.21 | 0.14 |
| 52 | HarmonicFiredancer/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460488215 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 53 | AgaveBam/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 54 | HarmonicAgave/4.3.2 | shared:pre:3.0 | sent | 8/8 | 24 | False (HarmonicFiredancer/26.10.4) | 1 | 4/455 | 8 | 1.00 | 0.29 |
| 55 | JitoLabs/4.3.2 | shared:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 56 | AgaveBam/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 57 | Rakurai/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 58 | JitoLabs/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 59 | Agave/4.3.2 | shared:pre:3.0 | sent | 8/8 | 24 | True (Agave/4.3.2) | 1 | 79/620 | 27 | 1.00 | -0.14 |
| 60 | Agave/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 61 | Rakurai/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 62 | AgaveBam/4.3.2 | independent:mid:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 63 | Rakurai/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 64 | HarmonicAgave/4.3.2 | independent:mid:0.0 | sent | 8/8 | 2 | True (HarmonicAgave/4.3.2) | 1 | 213/299 | 23 | -0.36 | 0.50 |
| 65 | HarmonicFiredancer/26.10.4 | independent:mid:3.0 | late_trigger_skipped (clock at 460489670 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 66 | HarmonicFiredancer/26.10.4 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 67 | JitoLabs/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 68 | Rakurai/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 69 | HarmonicFiredancer/26.10.4 | shared:mid:0.0 | late_trigger_skipped (clock at 460490646 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 70 | AgaveBam/4.3.2 | shared:pre:3.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 71 | JitoLabs/4.3.2 | independent:pre:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 72 | AgaveBam/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 73 | JitoLabs/4.3.2 | independent:mid:3.0 | error: TimeoutError('slot 460493833 not  | 0/0 | – | – (–) | – | –/– | – | – | – |
| 74 | Agave/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460494892 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 75 | Agave/4.3.2 | independent:mid:0.0 | missed_trigger_before_start | 0/0 | – | – (–) | – | –/– | – | – | – |
| 76 | HarmonicFiredancer/26.10.4 | independent:mid:3.0 | sent | 8/8 | 3 | True (HarmonicFiredancer/26.10.4) | 1 | 269/637 | 99 | 0.71 | 0.79 |
| 77 | JitoLabs/4.3.2 | shared:pre:3.0 | late_trigger_skipped (clock at 460496050 | 0/0 | – | – (–) | – | –/– | – | – | – |
| 78 | HarmonicFiredancer/26.10.4 | shared:pre:3.0 | sent | 8/8 | -1 | False (HarmonicAgave/4.3.2) | 1 | 260/394 | 39 | 0.50 | 0.36 |
| 79 | JitoLabs/4.3.2 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 80 | HarmonicFiredancer/26.10.4 | independent:mid:0.0 | sent | 0/8 | – | – (–) | – | –/– | – | – | – |
| 81 | HarmonicFiredancer/26.10.4 | independent:mid:0.0 | sent | 8/8 | 52 | False (HarmonicAgave/4.3.2) | 1 | 0/384 | 10 | 0.29 | -0.36 |
