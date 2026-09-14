# PAPER-BCRD-KNOWN-SPIN-ERASURE-001 — reconciled literature / novelty notes

Status: **DIRECT PRIOR ART LOCATED / A–E CLASSIFICATION SETTLED BY PR #258**

Frozen novelty authority: PR #258 at `9d67e480ea2278ad8781a269e39e904c41fe9a3d`.

No new literature search was performed in this reconciliation lane. This file records the settled result of the frozen audit.

## Standard QEC / DFS background

- Knill–Laflamme exact quantum-error-correction criteria and state-independent recovery.
- Located / known-position erasure as a standard QEC model.
- Decoherence-free and noiseless-subsystem structure under collective symmetries.
- The complete even-`N` qubit singlet / total-spin-zero DFS and its standard representation-theoretic multiplicity structure.
- Standard reversible-channel / sufficiency concepts.

## Direct prior art — Migdał & Banaszek 2011

Piotr Migdał and Konrad Banaszek, “Immunity of information encoded in decoherence-free subspaces to particle loss,” Physical Review A 84, 052318 (2011), DOI `10.1103/PhysRevA.84.052318`, arXiv:1107.3786.

The frozen novelty audit adjudicates their general Eqs. (9), (10), and (13) as mathematically equivalent, under routine basis/isometry packaging, to the manuscript's retained-support form

```text
E_i(rho) = W_i[(I_d/d) tensor rho]W_i^dagger.
```

For qubits, `d=2`. Therefore both one-particle-loss immunity and the `W_i` syndrome/logical support structure are direct prior art in substance. Different notation does not create a novelty claim.

## Settled A–E classification

```text
A_Wi_factorization = DIRECT_PRIOR_ART
B_full_algebra_recovery = STANDARD_COROLLARY_OR_REFORMULATION
C_recoverability_to_autonomy = STANDARD_COROLLARY_OR_REFORMULATION
D_reconstructive_vs_lossy = DISTINCT_SYNTHESIS_OR_APPLICATION
E_BCRD_finite_application = DISTINCT_SYNTHESIS_OR_APPLICATION
```

### A — retained-support factorization

Retain the explicit `W_i` formula because it is useful for the record dynamics, but identify it as an explicit recasting of prior structure.

### B — full-algebra CPTP recovery completion

The on-image decoder and measure/prepare completion on the orthogonal complement are standard channel constructions. The off-image action remains nonunique and carries no independent physical significance.

### C — recoverability-induced update

For `R o Lambda = id`, the formula

```text
Phi = Lambda o Ad_U o R
Phi o Lambda = Lambda o Ad_U
```

is an immediate standard consequence of transporting dynamics through a reversible channel representation.

### D — reconstructive versus genuinely lossy

The distinction is used as a publication-relevant synthesis for classifying the present BCRD records. No priority is claimed for a new general classification or terminology.

### E — finite BCRD realization

The reviewed finite application is `J2/J4/J6` at `N=8,10,12`, with a fixed update separately at each `N`. No arbitrary-`N` BCRD theorem, strict minimality, common cross-`N` map, or support-growth law follows.

## Publication-safe language

> One-particle-loss immunity and its syndrome-factor structure are established QEC/DFS results. In the present finite BCRD constructions, we place that reversible channel structure in a common record-dynamics formulation and obtain exact fixed per-N CPTP updates because the reviewed records remain reconstructive. The finite application thereby distinguishes autonomy inherited from reversible encoding from the separate problem of autonomous closure after genuine information loss.

## Priority controls

`first/new/novel/previously unknown/unprecedented` wording is not authorized for A–E. The manuscript does not claim new QEC/DFS mathematics, a new syndrome factorization, a new recovery principle, a new general autonomy theorem, or quantum gravity.
