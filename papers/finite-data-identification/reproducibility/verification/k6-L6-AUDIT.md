# UNIVERSAL LOWER CERTIFICATE HOSTILE AUDIT

Review: `HR-BCRD-R207-N8-SIX-TRANSITION-COMMON-CPTP-001`

The universal lower certificate is secondary bracket information only. It is not needed for the constructive PASS, and it was deliberately audited only after the reviewer-owned six-transition upper classification had crossed below `1/100`.

## Strongest claimed lower

Author strongest certified subset lower:

```text
subset = TRAIN0 + F1 + F2
raw lower before model padding = 0.002306906985934015
padding                          = 824829/10^12
certified universal lower L6     = 0.002306082156934015...
L6 > 0.01                        = FALSE
```

The exact rational value is preserved in the author record `results/lower/TRAIN0+F1+F2.json`.

## Dual sign / normalization audit

The ambient minimax primal uses one shared epigraph variable `e` with

```text
Z_kb >= +/- J_kb,
sum_b Tr_out Z_kb <= 2 e I_2,
```

so `e` is the half-diamond minimax error. The corresponding dual has

```text
R_k >= 0,
-R_k tensor I <= F_kb <= R_k tensor I,
L_a tensor I - A*F >= 0,
2 sum_k Tr R_k = 1,
```

with objective

```text
sum_{k,b} Tr(F_kb J(Y_kb)) - sum_a Tr L_a.
```

The signs and factor of two follow from the Lagrangian and are consistent with the same half-diamond normalization used by the constructive certificate.

`int_cert.py` does not assume the repaired point remains normalized after Weyl shifts. It computes

```text
norm = 2 sum_k Tr R_k
raw  = objective / norm
```

which is valid because all dual cone constraints and the ambient lift are positively homogeneous. Dividing the entire repaired dual point by `norm` restores the canonical normalization.

## Exact-arithmetic hygiene

The six-transition lower route does **not** import PR #213 `exact_cert.psd_margin`.

Its replacement `psd_margin_int`:

1. treats a floating eigendecomposition only as a proposal;
2. explicitly converts rounded entries to genuine Python `int` values;
3. computes the proposal Gram defect in exact integer/rational arithmetic;
4. reconstructs the proposal matrix exactly;
5. computes an exact residual operator-norm upper bound;
6. applies the correct one-sided eigenvalue bound, including the sign change required when the proposed minimum eigenvalue is negative.

The resulting lower bound on `lambda_min` is rigorous even if the floating eigensystem is poor; a poor proposal merely increases the exact residual correction.

Negative certified cone margins are repaired only by upward dyadic Weyl shifts. The shifted normalization/objective is recomputed; values are not edited by hand.

## Ambient lift audit

The lower is genuinely universal over the full physical whole-algebra class rather than a bound on the reduced search ansatz.

For dyadic support matrices `Pt,Qt`, the repaired compressed dual point is lifted as

```text
F_amb = (I tensor Qt) F (I tensor Qt)^dag / (1+dQ_b)
L_amb = conj(Pt) L conj(Pt)^dag + t_a I.
```

This is sound because:

- `Qt Qt^dag <= (1+dQ_b) I`, so the `R +/- F` cones remain feasible after the `F` scaling;
- the compressed transfer cone is carried into the ambient supported part by congruence;
- `Delta = X_amb - Pt X_cmp Pt^dag` is kept explicitly rather than assumed zero;
- `t_a` bounds the unsupported remainder using exact operator-norm bounds and the maximum relevant `F` block norm;
- `L_a >= 0` is separately certified before the congruence inequality is used.

No B2/B3 equality of reduced and global optima is needed for this lower route.

## Objective and padding audit

The positive objective term is evaluated against exact compressed target channels and divided by the exact `1+dQ_b` factors. The trace of the lifted `L_amb` is computed exactly, including the `t_a d_a` completion cost.

For the model-to-physical conversion, the lower direction correctly subtracts the largest applicable half-diamond channel-model padding over the chosen transition subset. For `TRAIN0+F1+F2` the largest pad is the F2 value `824829/10^12`.

## Independent ambient cross-check

The author's materially separate float verifier reconstructs the ambient lifted point and checks the ambient cones directly. For `TRAIN0+F1+F2` it reports:

```text
min eig R                   3.075012058531985e-3
min eig (R +/- F_amb)       2.205647299453469e-13
min eig transfer cones      6.653333752825453e-12
worst transfer cone         (a,b) = (6,1)
ambient objective           0.0023069069860854998
certified raw lower         0.002306906985934015
absolute objective diff     1.5148472753967468e-13
```

All ambient cones are feasible within the diagnostic tolerance and the independently reconstructed objective agrees to far better than `1e-9`.

## Hostile disposition of L6

```text
universal_lower_scope_survives    = YES
exact_arithmetic_route_survives   = YES
ambient_lift_survives             = YES
half_diamond_normalisation        = YES
strongest_L6                      = 0.002306082156934015...
L6 > 0.01                         = NO
universal_FAIL_established        = NO
```

Combined with the reviewer-owned constructive upper:

```text
0.002306082156934015... <= epsilon_*^(6) <= 0.004582638648933954...
```

This bracket is only for the exact six spent N=8 `R2_07` transitions and the frozen full physical common-CPTP class.
