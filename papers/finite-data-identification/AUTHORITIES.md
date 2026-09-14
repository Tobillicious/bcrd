# AUTHORITIES — PAPER-BCRD-FINITE-DATA-IDENTIFICATION-001

## Manuscript and revision custody

```text
scientific_cutoff_pr            = #223
scientific_cutoff_sha           = 0a598dceefff780ccb1e1a25caceda4d30643997
frozen_manuscript_pr            = #251
frozen_manuscript_sha           = 3433b889a301beb41a55a694337fb75f9b9994f6
governing_manuscript_review_pr  = #253
governing_manuscript_review_sha = 846267c2abb15c8e659aeeec08efc2ed4dd9ce58
governing_review_contract       = f09b7dd42775750068e6e0466d037009dbb86969
revision_branch                 = sol/revise-paper-finite-data-identification-after-review-2026-09-14
new_physics_authorized          = NO
```

PR #253 is the governing **manuscript-review authority**. It is not a new scientific authority. The scientific result remains frozen to reviewed results available at PR #223. Post-cutoff material used in this revision is restricted to custody/representation, methodology, typesetting, provenance, or the governing manuscript review itself.

The revision contract is repository-root `REVISION-CONTRACT-AFTER-HR-253.md`, committed alone before substantive manuscript edits.

## Scientific authority ledger

| scientific statement | author PR / terminal SHA | hostile review / reconciliation | exact status | manuscript use |
|---|---|---|---|---|
| Two-transition common physical CPTP existence on TRAIN0/TRAIN1 | #201 / `cfbf110fc8b5844c2714a7ab116d74e93d2b8071` | #202 / `2f4b4f8f1f2f8f31f74caa002cd5492ed461fe68` | Scientific certificate survives; preregistered per-solve runtime ceiling fails literally | Historical context only |
| Four-transition common-CPTP existence | #213 / `1ad514541a6c8977db80a6ab7ac1a2bda3257107` | #214 / `683e83807df926664268fd6600d8900972485fd5` | `R2_07_N8_FOUR_TRANSITION_COMMON_CPTP_EXISTENCE_PASS_SURVIVES_WITH_SCOPE_HARDENING` | Load-bearing K=4 result |
| Four-transition author contract | #213 contract `d870d08dc6d4b9a9f9605653aeffcc9f2985f79c` | #214 audited chronology | Frozen before optimization | Provenance |
| Frozen K=4 witness | #213 `candidate-map-dyadic.npz`, SHA-256 `48abd5f52812ef7503cfdde92fe630b99ded9c10c4ef35d2c4edc8d934028125` | #214 hash/schema/custody verified | One physical whole-algebra source-independent time-independent CPTP map; 49 transfers, 5184 Kraus operators | `Phi_4` |
| K=4 rigorous existence upper | #213 multiple routes | #214 independent exact U1 worst `0.006670414972746646... < 0.01` | Load-bearing existence PASS | `Phi_4 in F_4(0.01)` |
| Outcome-blind forward-schedule design | #215 / `29b7407d711f8b36c5887b486187194e56d07baf` | provenance chain culminating #218 | No future physics opened in design lane | Prospective custody |
| Pristine forward schedule | #216/#217 | #218 / `e31c4380d1111d0cb9cec9040da59971288dff14` | `FORWARD_SCHEDULE_EARNED_PROVEN_PRISTINE`; `t_exposed_max=24`; selector `b=0,k=234` | Genuine F1/F2 prospectivity |
| Prospective failure of exact frozen `Phi_4` | #219 / `4de999a05a0173b5f82c4b572dad1479bc5bb33c` | #220 / `069b9edba77358bcedc9fffe256ecf006c846bc0` | `R2_07_N8_PRISTINE_FORWARD_FROZEN_MAP_FAILURE_SURVIVES_WITH_SCOPE_HARDENING` | Load-bearing frozen-witness failure |
| Independent recomputation of prospective failure | reviewer workflow from #220 | #221 / `dc782001d75247ab1c56d9ee52aac430c12333cc` | Executed and agrees; fresh classification FAIL | Closes execution-status caveat |
| Six-transition common-CPTP existence | #222 / `bdf8597aa427abb789805fb331c32932bf97de28`; contract `2cfc7ecb82ccd73470e0019b8a2b8455928286c5` | #223 / `0a598dceefff780ccb1e1a25caceda4d30643997`; hostile contract `df93533a7ca9252c11e03f495295e01b7c6207e4` | `R2_07_N8_SIX_TRANSITION_COMMON_CPTP_EXISTENCE_PASS_SURVIVES_WITH_SCOPE_HARDENING` | Load-bearing K=6 result |
| Frozen K=6 witness | #222 `C-S2-frob-pr213.npz`, SHA-256 `c674e471c6bbad2e3376e53315d8e1e5cb83dbbb85f4120c7b5b8602b78f7e0a` | #223 exact hash, CP/TP, whole-algebra and one-map checks | One physical whole-algebra map common to all six transitions | `Phi_6` |
| K=6 rigorous upper | #222 | #223 reviewer-owned exact-plus-enclosure recomputation | `U_6=0.004582638648933954... < 0.01` | Load-bearing PASS |
| K=6 universal lower | #222 subset TRAIN0+F1+F2 | #223 independent hostile audit | `L_6=0.002306082156934015...` | Load-bearing bracket |
| P/Q computational reduction | inherited author chain | #223 scope hardening | Exact minimax-equivalent through CPTP extension/retraction; not literal equality of reduced/global map sets | Appendix wording |
| Canonical K=6 custody serialization | #226 / `7bf62758f8b4fd6da9ceb939e6ae07a4c90240e5` | methodology-only; no new physics | Records already-authorized metadata including shared double `0.9323881824729999` | `CUSTODY_REPRESENTATION_ONLY` |

## Frozen physical setting

```text
N                  = 8
candidate          = E
cursor             = none
isotropic coupling = J = 1
record             = R2_07
source             = complete source qubit (E00,E01,E10,E11)
delta              = 0.1
tolerance epsilon  = 0.01
```

The matter algebra is `alg*(D12,D34,D56,D67)`. In reviewed sector order

```text
(j12,j34,2j567) =
(0,0,1), (0,1,1), (0,1,3), (1,0,1), (1,0,3), (1,1,1), (1,1,3)

n = (2,2,1,2,1,2,1)
m = (1,1,1,1,1,2,2)
d = (64,64,32,64,32,64,32)
```

the abstract record algebra is the direct sum `A_R2_07 ~= direct_sum_a M_{d_a}`, represented concretely as `x_a tensor I_{m_a}`. The physical trace is

```text
tau(x) = sum_a m_a Tr(x_a).
```

The admissible class `C` is **one** physical CPTP map on the whole record algebra, source-independent, time-independent, and common to every transition. All 49 central transfers are allowed. No dictionary, low-rank, nearby-map, fixed Kraus-family, optimizer-basin, hidden-state, or transition-labelled restriction is part of `C`.

## Exact transition dataset

| label | current time | next time | evidential role |
|---|---:|---:|---|
| TRAIN0 | 0.832388182473 | 0.9323881824729999 | original exposed fit data |
| TRAIN1 | 0.9323881824729999 | 1.032388182473 | original exposed fit data |
| H1 | 1.232388182473 | 1.332388182473 | exposed K=4 fit data |
| H2 | 1.382388182473 | 1.482388182473 | exposed K=4 fit data |
| F1 | 24.232388182473 | 24.332388182473 | prospectively selected pristine transition |
| F2 | 24.532388182473 | 24.632388182473 | prospectively selected pristine transition |

The TRAIN0/TRAIN1 shared endpoint is the banked binary64 rendering `0.9323881824729999`, not an independently retyped decimal.

## Error definition and reviewed values

```text
e_j(Phi) = (1/2) || Lambda_j^next - Phi o Lambda_j^cur ||_diamond
```

Hostile-reviewed prospective lower bounds for exact frozen `Phi_4`:

```text
e_F1(Phi4) >= 0.6246936110454476
e_F2(Phi4) >= 0.6217658417777687
```

Hostile-reviewed K=6 witness upper bounds:

```text
TRAIN0 <= 0.0017360413721420206
TRAIN1 <= 0.0017902995810885707
H1     <= 0.0017010819506354795
H2     <= 0.0022602480754981130
F1     <= 0.0045826386489339540
F2     <= 0.0044800043819739690
```

and

```text
0.002306082156934015...
<= epsilon_*^(6)
<= 0.004582638648933954...
< 0.01.
```

## Reviewed set-membership deduction

At tolerance `0.01`:

```text
F_6 subseteq F_4
Phi_6 in F_6, hence Phi_6 in F_4
Phi_4 in F_4
Phi_4 notin F_6
therefore Phi_4 != Phi_6
```

Thus `F_4(0.01)` contains at least two distinct physical tolerance-feasible maps with sharply different certified prospective errors. Publication terminology: **finite-data non-identification**, **set-membership ambiguity**, or **non-uniqueness of the tolerance-feasible model set**.

This does not establish universal estimator failure or information-theoretic insufficiency under every possible prior/selection rule.

## Public reproducibility packet prepared in revision

`reproducibility/` contains:

- exact existing Git blob for frozen `Phi_4`;
- exact existing Git blob for accepted `Phi_6`;
- exact reviewer-owned PR #220 prospective lower-certificate JSON;
- exact reviewer-owned PR #223 K=6 recomputation summary JSON;
- exact PR #223 K=6 universal-lower audit;
- exact transition CSV;
- physical-map-class definition;
- certificate summary;
- source PR/SHA/path/Git-blob manifest;
- SHA-256 manifest and mechanical packaging verifier.

The packet is **prepared but not promoted** to `Tobillicious/bcrd` in this lane.

## Scope ceiling

Not established: arbitrary-time autonomy, universal autonomy/non-autonomy, prospective validity of `Phi_6`, semigroup, generator/Lindbladian, memory or absence of memory, hidden-state necessity, minimal augmentation, Markov order, uniqueness/minimality, cross-N persistence, large-N/continuum behavior, geometry, spacetime, gravity, or quantum gravity.

The N=4 coherent-Racah lane was not inspected or used in this revision.
