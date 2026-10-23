# Pooled mainnet live results (/data/runs/20261023T144945Z)

Bursts planned 82; status {'sent': 53, 'late_trigger_skipped': 17, 'missed_trigger_before_start': 10, 'error': 2}. Probes sent 424, landed 152 (36%). Usable bursts (≥3 landed, one producing leader): 19, of which 8 were produced by a leader other than the target.

## Landing by targeted client

| targeted client | bursts sent | probes sent | landed | rate |
|---|---|---|---|---|
| Agave/4.3.2 | 7 | 56 | 8 | 14% |
| AgaveBam/4.3.2 | 7 | 56 | 8 | 14% |
| FireBAM/26.10.4 | 3 | 24 | 0 | 0% |
| Firedancer/26.10.4 | 6 | 48 | 40 | 83% |
| HarmonicAgave/4.3.2 | 8 | 64 | 56 | 88% |
| HarmonicFiredancer/26.10.4 | 6 | 48 | 32 | 67% |
| JitoLabs/4.3.2 | 7 | 56 | 0 | 0% |
| Rakurai/4.3.2 | 9 | 72 | 8 | 11% |

## By producing client × arm (pooled over runs)

| producing client | arm | bursts | leaders | forwarded | τ fee (95% CI) | sign-test p (τ fee > 0) | perfectly fee-sorted | τ send (95% CI) | verdict |
|---|---|---|---|---|---|---|---|---|---|
| ALL clients | independent:* | 11 | 10 | 4 | 0.32 [0.03, 0.61] | 0.549 | 1/11 | 0.10 [-0.19, 0.39] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:mid:0 | 3 | 3 | 1 | 0.31 [-0.36, 1.00] | 1.000 | 1/3 | 0.05 [-0.36, 0.50] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:mid:3 | 5 | 5 | 3 | 0.51 [0.07, 0.89] | 0.375 | 0/5 | 0.24 [-0.23, 0.77] | no rule detected (consistent with noise at this n) |
| ALL clients | independent:pre:0 | 3 | 3 | 0 | 0.02 [-0.21, 0.50] | 1.000 | 0/3 | -0.07 [-0.64, 0.29] | no rule detected (consistent with noise at this n) |
| ALL clients | shared:* | 8 | 8 | 4 | 0.78 [0.60, 0.93] | 0.008 | 3/8 | -0.05 [-0.23, 0.12] | fee-priority (38% of bursts perfectly fee-sorted) |
| ALL clients | shared:mid:0 | 2 | 2 | 2 | 0.79 [0.79, 0.79] | 0.500 | 0/2 | -0.07 [-0.14, 0.00] | fee-priority (0% of bursts perfectly fee-sorted) |
| ALL clients | shared:pre:0 | 2 | 2 | 0 | 0.57 [0.29, 0.86] | 0.500 | 0/2 | -0.25 [-0.50, 0.00] | no rule detected (consistent with noise at this n) |
| ALL clients | shared:pre:3 | 4 | 4 | 2 | 0.87 [0.62, 1.00] | 0.125 | 3/4 | 0.05 [-0.21, 0.32] | fee-priority (75% of bursts perfectly fee-sorted) |
| Agave/4.3.2 | shared:* | 1 | 1 | 0 | 1.00 – | 1.000 | 1/1 | -0.14 – | insufficient data |
| Agave/4.3.2 | shared:pre:3 | 1 | 1 | 0 | 1.00 – | 1.000 | 1/1 | -0.14 – | insufficient data |
| AgaveBam/4.3.2 | independent:* | 1 | 1 | 1 | 0.93 – | 1.000 | 0/1 | 0.07 – | insufficient data |
| AgaveBam/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.93 – | 1.000 | 0/1 | 0.07 – | insufficient data |
| Firedancer/26.10.4 | independent:* | 3 | 2 | 0 | 0.14 [-0.36, 1.00] | 1.000 | 1/3 | 0.43 [0.00, 1.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | independent:mid:0 | 1 | 1 | 0 | 1.00 – | 1.000 | 1/1 | 0.00 – | insufficient data |
| Firedancer/26.10.4 | independent:mid:3 | 1 | 1 | 0 | -0.36 – | 1.000 | 0/1 | 1.00 – | insufficient data |
| Firedancer/26.10.4 | independent:pre:0 | 1 | 1 | 0 | -0.21 – | 1.000 | 0/1 | 0.29 – | insufficient data |
| Firedancer/26.10.4 | shared:* | 2 | 2 | 0 | 0.64 [0.29, 1.00] | 0.500 | 1/2 | -0.14 [-0.29, 0.00] | no rule detected (consistent with noise at this n) |
| Firedancer/26.10.4 | shared:pre:0 | 1 | 1 | 0 | 0.29 – | 1.000 | 0/1 | 0.00 – | insufficient data |
| Firedancer/26.10.4 | shared:pre:3 | 1 | 1 | 0 | 1.00 – | 1.000 | 1/1 | -0.29 – | insufficient data |
| HarmonicAgave/4.3.2 | independent:* | 3 | 3 | 2 | 0.10 [-0.36, 0.36] | 1.000 | 0/3 | -0.02 [-0.36, 0.50] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:0 | 2 | 2 | 1 | -0.04 [-0.36, 0.29] | 1.000 | 0/2 | 0.07 [-0.36, 0.50] | no rule detected (consistent with noise at this n) |
| HarmonicAgave/4.3.2 | independent:mid:3 | 1 | 1 | 1 | 0.36 – | 1.000 | 0/1 | -0.21 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:* | 4 | 4 | 3 | 0.73 [0.57, 0.84] | 0.125 | 0/4 | -0.07 [-0.37, 0.23] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:mid:0 | 2 | 2 | 2 | 0.79 [0.79, 0.79] | 0.500 | 0/2 | -0.07 [-0.14, 0.00] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicAgave/4.3.2 | shared:pre:0 | 1 | 1 | 0 | 0.86 – | 1.000 | 0/1 | -0.50 – | insufficient data |
| HarmonicAgave/4.3.2 | shared:pre:3 | 1 | 1 | 1 | 0.50 – | 1.000 | 0/1 | 0.36 – | insufficient data |
| HarmonicFiredancer/26.10.4 | independent:* | 3 | 3 | 1 | 0.48 [-0.21, 0.93] | 1.000 | 0/3 | 0.17 [-0.43, 0.79] | no rule detected (consistent with noise at this n) |
| HarmonicFiredancer/26.10.4 | independent:mid:3 | 2 | 2 | 1 | 0.82 [0.71, 0.93] | 0.500 | 0/2 | 0.18 [-0.43, 0.79] | fee-priority (0% of bursts perfectly fee-sorted) |
| HarmonicFiredancer/26.10.4 | independent:pre:0 | 1 | 1 | 0 | -0.21 – | 1.000 | 0/1 | 0.14 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:* | 1 | 1 | 1 | 1.00 – | 1.000 | 1/1 | 0.29 – | insufficient data |
| HarmonicFiredancer/26.10.4 | shared:pre:3 | 1 | 1 | 1 | 1.00 – | 1.000 | 1/1 | 0.29 – | insufficient data |
| Rakurai/4.3.2 | independent:* | 1 | 1 | 0 | 0.50 – | 1.000 | 0/1 | -0.64 – | insufficient data |
| Rakurai/4.3.2 | independent:pre:0 | 1 | 1 | 0 | 0.50 – | 1.000 | 0/1 | -0.64 – | insufficient data |
