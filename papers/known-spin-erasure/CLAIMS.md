# PAPER-BCRD-KNOWN-SPIN-ERASURE-001 — reconciled claim ledger

Frozen reconciliation authorities:
- hostile review PR #254: `7622473f21276f014224954a21ae8f26b22a2fbf`
- manuscript base PR #256: `78584848a1051f8eb963ddbc1dd7f2bb1a42def0`
- novelty audit PR #258: `9d67e480ea2278ad8781a269e39e904c41fe9a3d`

## Settled contribution classification

### A — `W_i` support / syndrome factorization
`DIRECT_PRIOR_ART`

Migdał & Banaszek (2011) give the equivalent retained-component orthogonality and equal-mixture structure. The `W_i` notation remains useful here but carries no novelty claim.

### B — full-algebra recovery
`STANDARD_COROLLARY_OR_REFORMULATION`

The decoder on the reachable support and a nonunique CPTP completion off that support are standard consequences/reformulations.

### C — recoverability -> exact autonomous update
`STANDARD_COROLLARY_OR_REFORMULATION`

For `R o Lambda = id`, the update `Phi = Lambda o Ad_U o R` and the intertwining relation follow by composition. This is not claimed as a new general autonomy theorem.

### D — reconstructive-versus-lossy framing
`DISTINCT_SYNTHESIS_OR_APPLICATION`

The manuscript uses this distinction to classify and interpret the present records. It does not claim priority for a new general classification.

### E — finite BCRD `J2/J4/J6` realization
`DISTINCT_SYNTHESIS_OR_APPLICATION`

| N | certified record | retained support count q | status |
|---:|---|---:|---|
| 8 | `J2[#196]` | 12 | exact reconstructive autonomous closure |
| 10 | `J4[#196]` | 16 | exact reconstructive autonomous closure |
| 12 | `J6[#196]` | 20 | exact reconstructive autonomous closure |

These are fixed per-`N` constructions only.

## General theorem / finite application boundary

The general even-`N` singlet/DFS recovery structure remains general where mathematically supported. The finite BCRD realization remains restricted to `N=8,10,12`. No arbitrary-`N` BCRD result, common cross-`N` update, strict minimality theorem, or support-growth theorem is inferred.

## Nonclaims

The paper does not establish unknown-location erasure correction, two-spin erasure correction, arbitrary-subsystem erasure correction, genuinely lossy autonomous closure, a Markov semigroup or Lindblad generator, thermodynamic irreversibility, asymptotic/continuum closure, geometry, gravity, or quantum gravity. It does not claim new QEC/DFS mathematics, a new syndrome factorization, a new recovery theorem, or a new general CPTP-autonomy theorem.

## Publication-safe centre

One-particle-loss immunity and its syndrome-factor structure are known QEC/DFS results. In the present finite BCRD constructions, we place that reversible channel structure in a common record-dynamics formulation and show that the reviewed `J2/J4/J6` records admit exact fixed per-`N` CPTP updates because they remain reconstructive. This yields a finite synthesis separating exact autonomy inherited from reversible encoding from the distinct problem of autonomous closure after genuine information loss.
