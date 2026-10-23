| client/version | validator | arm | bursts | sent→landed | τ fee (95% CI) | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|
| Agave/4.3.0 | `6W4VZoj5…` | independent:mid:0.0 | 2 | 16→16 | 0.21 [0.14, 0.29] | -0.07 [-0.29, 0.14] | no rule detected (consistent with noise at this n) |
| Agave/4.3.0 | `6W4VZoj5…` | independent:mid:3.0 | 2 | 16→16 | 0.00 [0.00, 0.00] | 0.75 [0.64, 0.86] | arrival order / FIFO (0% of bursts perfectly send-ordered) |
| Agave/4.3.0 | `6W4VZoj5…` | independent:pre:0.0 | 2 | 16→16 | -0.07 [-0.14, 0.00] | -0.04 [-0.14, 0.07] | no rule detected (consistent with noise at this n) |
| Agave/4.3.0 | `6W4VZoj5…` | independent:pre:3.0 | 2 | 16→16 | -0.61 [-0.86, -0.36] | 0.75 [0.64, 0.86] | arrival order / FIFO (0% of bursts perfectly send-ordered) |
| Agave/4.3.0 | `6W4VZoj5…` | shared:mid:0.0 | 2 | 16→16 | 1.00 [1.00, 1.00] | -0.07 [-0.14, 0.00] | fee-priority (100% of bursts perfectly fee-sorted) |
| Agave/4.3.0 | `6W4VZoj5…` | shared:pre:0.0 | 2 | 16→16 | 1.00 [1.00, 1.00] | -0.04 [-0.21, 0.14] | fee-priority (100% of bursts perfectly fee-sorted) |
| Agave/4.3.0 | `6W4VZoj5…` | all:all | 12 | 96→96 | 0.26 [-0.08, 0.60] | 0.21 [-0.01, 0.45] | no rule detected (consistent with noise at this n) |

| burst | client | arm | status | landed | slots | first idx / block | span | τ fee | τ send |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Agave/4.3.0 | independent:pre:0.0 | sent | 8/8 | 1 | 1/9 | 8 | -0.14 | 0.07 |
| 1 | Agave/4.3.0 | independent:mid:3.0 | sent | 8/8 | 1 | 1/9 | 8 | 0.00 | 0.64 |
| 2 | Agave/4.3.0 | shared:pre:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 1.00 | 0.14 |
| 3 | Agave/4.3.0 | independent:pre:3.0 | sent | 8/8 | 1 | 1/9 | 8 | -0.86 | 0.64 |
| 4 | Agave/4.3.0 | independent:mid:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 0.29 | 0.14 |
| 5 | Agave/4.3.0 | shared:mid:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 1.00 | -0.14 |
| 6 | Agave/4.3.0 | independent:pre:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 0.00 | -0.14 |
| 7 | Agave/4.3.0 | independent:mid:3.0 | sent | 8/8 | 1 | 1/9 | 8 | 0.00 | 0.86 |
| 8 | Agave/4.3.0 | shared:pre:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 1.00 | -0.21 |
| 9 | Agave/4.3.0 | independent:pre:3.0 | sent | 8/8 | 1 | 1/9 | 8 | -0.36 | 0.86 |
| 10 | Agave/4.3.0 | independent:mid:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 0.14 | -0.29 |
| 11 | Agave/4.3.0 | shared:mid:0.0 | sent | 8/8 | 1 | 1/9 | 8 | 1.00 | 0.00 |
