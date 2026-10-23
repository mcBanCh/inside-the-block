# Pooled mainnet live results (/data/runs/20261023T144945Z, /data/runs/20261023T155226Z)

Bursts planned 167; status {'sent': 111, 'late_trigger_skipped': 41, 'missed_trigger_before_start': 13, 'error': 2}. Probes sent 888, landed 321 (36%). Usable bursts (≥3 landed, one producing leader): 40, of which 20 were produced by a leader other than the target.

## Landing by targeted client

| targeted client | bursts sent | probes sent | landed | rate |
|---|---|---|---|---|
| Agave/4.3.2 | 14 | 112 | 16 | 14% |
| AgaveBam/4.3.2 | 12 | 96 | 16 | 17% |
| FireBAM/26.10.4 | 12 | 96 | 8 | 8% |
| Firedancer/26.10.4 | 14 | 112 | 73 | 65% |
| HarmonicAgave/4.3.2 | 15 | 120 | 96 | 80% |
| HarmonicFiredancer/26.10.4 | 15 | 120 | 104 | 87% |
| JitoLabs/4.3.2 | 15 | 120 | 0 | 0% |
| Rakurai/4.3.2 | 14 | 112 | 8 | 7% |

## By producing client × arm (pooled over runs)

| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | sign-test p (τ fee > 0) | perfectly fee-sorted | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|---|---|
| ALL clients | independent:* | 21 | 19 | 12 | 0.33 [0.12, 0.53] | 0.078 | 1/21 | 0.03 [-0.13, 0.21] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:mid:0 | 9 | 9 | 5 | 0.30 [-0.02, 0.63] | 0.180 | 1/9 | 0.01 [-0.14, 0.18] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:mid:3 | 6 | 6 | 4 | 0.55 [0.15, 0.86] | 0.219 | 0/6 | 0.21 [-0.19, 0.64] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:pre:0 | 6 | 6 | 3 | 0.14 [-0.15, 0.49] | 1.000 | 0/6 | -0.12 [-0.40, 0.13] | no rule detected (consistent with noise at this n) |
| ALL clients | shared:* | 19 | 15 | 8 | 0.66 [0.46, 0.84] | 0.004 | 6/19 | 0.14 [-0.06, 0.36] | fee-priority (32% of bursts perfectly fee-sorted) |
| ALL clients | shared:mid:0 | 4 | 4 | 3 | 0.84 [0.79, 0.89] | 0.125 | 0/4 | -0.07 [-0.12, -0.02] | fee-priority (0% of bursts perfectly fee-sorted) |
| ALL clients | shared:pre:0 | 7 | 5 | 3 | 0.54 [0.17, 0.86] | 0.453 | 2/7 | 0.17 [-0.26, 0.63] | no rule detected (consistent with noise at this n) |
| ALL clients | shared:pre:3 | 8 | 8 | 2 | 0.68 [0.35, 0.94] | 0.070 | 4/8 | 0.22 [-0.04, 0.50] | fee-priority (50% of bursts perfectly fee-sorted) |
| Agave/4.3.2 | shared:* | 2 | 2 | 0 | 0.46 [-0.07, 1.00] | 1.000 | 1/2 | 0.43 [-0.14, 1.00] | no rule detected (consistent with noise at this n) |
| Agave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | -0.07 – | 1.000 | 0/1 | 1.00 – | insufficient data |
| Agave/4.3.2 | shared:pre:3 | 1 | 1 | 0 | 1.00 – | 1.000 | 1/1 | -0.14 – | insufficient data |
| AgaveBam/4.3.2 | independent:* | 2 | 2 | 1 | 0.86 [0.79, 0.93] | 0.500 | 0/2 | 0.07 [0.07, 0.07] | fee-priority (0% of bursts perfectly fee-sorted) |
| AgaveBam/4.3.2 | independent:mid:0 | 1 | 1 | 0 | 0.79 – | 1.000 | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.93 – | 1.000 | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | shared:* | 1 | 1 | 1 | 1.00 – | 1.000 | 1/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | shared:pre:0 | 1 | 1 | 1 | 1.00 – | 1.000 | 1/1 | 0.07 – | insufficient data |
| Firedancer/26.10.4 | independent:* | 4 | 2 | 0 | -0.02 [-0.43, 0.66] | 0.625 | 1/4 | 0.27 [-0.11, 0.75] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | independent:mid:0 | 2 | 2 | 0 | 0.25 [-0.50, 1.00] | 1.000 | 1/2 | -0.11 [-0.21, 0.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | independent:mid:3 | 1 | 1 | 0 | -0.36 – | 1.000 | 0/1 | 1.00 – | insufficient data |
| Firedancer/26.10.4 | independent:pre:0 | 1 | 1 | 0 | -0.21 – | 1.000 | 0/1 | 0.29 – | insufficient data |
| Firedancer/26.10.4 | shared:* | 5 | 3 | 0 | 0.37 [-0.11, 0.86] | 1.000 | 2/5 | 0.31 [-0.14, 0.80] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | shared:pre:0 | 2 | 1 | 0 | 0.07 [-0.14, 0.29] | 1.000 | 0/2 | 0.50 [0.00, 1.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | shared:pre:3 | 3 | 3 | 0 | 0.57 [-0.29, 1.00] | 1.000 | 2/3 | 0.19 [-0.29, 1.00] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:* | 8 | 8 | 7 | 0.21 [0.01, 0.40] | 0.070 | 0/8 | -0.00 [-0.18, 0.20] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:0 | 5 | 5 | 4 | 0.10 [-0.14, 0.27] | 0.375 | 0/5 | 0.01 [-0.26, 0.33] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:3 | 2 | 2 | 2 | 0.54 [0.36, 0.71] | 0.500 | 0/2 | -0.07 [-0.21, 0.07] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | independent:pre:0 | 1 | 1 | 1 | 0.07 – | 1.000 | 0/1 | 0.07 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:* | 6 | 5 | 3 | 0.68 [0.50, 0.83] | 0.031 | 0/6 | 0.04 [-0.23, 0.31] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:mid:0 | 3 | 3 | 2 | 0.81 [0.79, 0.86] | 0.250 | 0/3 | -0.07 [-0.14, 0.00] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | 0.86 – | 1.000 | 0/1 | -0.50 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:pre:3 | 2 | 2 | 1 | 0.39 [0.29, 0.50] | 0.500 | 0/2 | 0.46 [0.36, 0.57] | arrival order / FIFO (0% of bursts perfectly send-ordered) |
| HarmonicFiredancer/26.10.4 | independent:* | 6 | 6 | 4 | 0.51 [0.14, 0.88] | 0.688 | 0/6 | 0.01 [-0.31, 0.36] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | independent:mid:0 | 1 | 1 | 1 | 0.93 – | 1.000 | 0/1 | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | independent:mid:3 | 2 | 2 | 1 | 0.82 [0.71, 0.93] | 0.500 | 0/2 | 0.18 [-0.43, 0.79] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | independent:pre:0 | 3 | 3 | 2 | 0.17 [-0.21, 0.86] | 1.000 | 0/3 | -0.14 [-0.50, 0.14] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | shared:* | 5 | 4 | 4 | 0.94 [0.90, 0.99] | 0.062 | 2/5 | 0.00 [-0.34, 0.26] | fee-priority (40% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | shared:mid:0 | 1 | 1 | 1 | 0.93 – | 1.000 | 0/1 | -0.07 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:pre:0 | 2 | 1 | 2 | 0.93 [0.86, 1.00] | 0.500 | 1/2 | -0.18 [-0.64, 0.29] | fee-priority (50% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | shared:pre:3 | 2 | 2 | 1 | 0.96 [0.93, 1.00] | 0.500 | 1/2 | 0.21 [0.14, 0.29] | fee-priority (50% of bursts perfectly fee-sorted) |
| Rakurai/4.3.2 | independent:* | 1 | 1 | 0 | 0.50 – | 1.000 | 0/1 | -0.64 – | insufficient data |
| Rakurai/4.3.2 | independent:pre:0 | 1 | 1 | 0 | 0.50 – | 1.000 | 0/1 | -0.64 – | insufficient data |
