# PAPER-BCRD-KNOWN-SPIN-ERASURE-001 — authority ledger after hostile manuscript review

This ledger distinguishes scientific theorem authority from publication/prior-art review authority. Scientific SHAs are unchanged by this revision.

## Frozen manuscript and review authorities

- Frozen author manuscript: PR #252, branch `gpt/paper-known-spin-erasure-reconstructive-closure-2026-09-14`, frozen head `39cadaa06eb359f8d6f0b58b43f42210e39e2058`.
- Governing hostile manuscript review: PR #254, review branch `sol/review-paper-known-spin-erasure-2026-09-14`, review contract `44ef1f7509dcedf2731ed97daf5f6502e4995f2f`, review terminal `7622473f21276f014224954a21ae8f26b22a2fbf`.
- Review disposition: `MANUSCRIPT_REQUIRES_MATERIAL_REVISION`, with mathematics surviving and prior-art/novelty framing requiring hardening.

PR #254 is a **publication/prior-art review authority**, not a replacement for scientific theorem authorities.

## Scientific theorem authorities

| result used | PR / artifact | terminal SHA | exact status | role in paper |
|---|---|---|---|---|
| Frozen microscopic finite-system provenance | predecessor frozen state | `cb715a13254c4ff9cdc4594767e1f5cf5f52d954` | frozen model authority | Defines the finite physical Hilbert space, singlet matter sector, and SU(2)-scalar matter couplings. |
| Exact one-known-matter-spin erasure theorem | PR #196 ancestry | `76dde863ab0433907a527229acb04e23b8c5c396` | exact structural CPTP recoverability | Supplies `P_0 sigma_i^a P_0=0`, located-erasure recovery, and arbitrary-reference recovery. |
| Independent proof-first one-spin review | PR #195 | `2f328e7d9d72a454467ddbd27ebd2fb53e5d66c4` | theorem survives with scope hardening | Supplies independent proofs, `W_i` factorization, explicit recovery, and reconstructive-vs-lossy classification. |
| Finite interaction-closed record construction | PR #196 | `0bbe6d7d6fceb35c429e38758eaeff1231bc06a3` | finite autonomous reconstructive record found | Supplies `J2/J4/J6` at `N=8,10,12`. |
| Hostile review of finite record construction | PR #198 | scientific `a1904d70b46df79d903134089e3263742e2d0954`; handoff `becbc82e77b5c4fe8c595ae7d77008b1bd202582` | survives with scope hardening | Confirms exact finite reconstructive autonomy and off-image nonuniqueness. |
| Dynamical-record reconciliation | PR #199 | `bb17394b8ae71f547db29801e0f56c36042d3ad5` | frontier reconciled with scope hardening | Canonicalizes reconstructive closure and nonclaims. |

## Direct prior-art authority

**Piotr Migdał and Konrad Banaszek, “Immunity of information encoded in decoherence-free subspaces to particle loss,” Physical Review A 84, 052318 (2011), DOI `10.1103/PhysRevA.84.052318`, arXiv:1107.3786.**

Publication status fixed by PR #254 and direct rereading in this revision:

- the paper treats collective-`SU(d)` decoherence-free subspaces;
- it proves immunity of encoded information to removal of one particle;
- its qubit specialization explicitly treats the complete even-`N` singlet / total-spin-zero DFS;
- it gives an explicit four-qubit recovery procedure and a general `SU(d)` proof;
- therefore one-particle-loss immunity of the singlet DFS is **known prior art** for manuscript purposes.

This direct prior art does not weaken the reviewed mathematics. It changes attribution and publication positioning.

## Exact mathematical content preserved

The manuscript may still use as exact:

1. `P_0 sigma_i^alpha P_0 = 0` for every fixed site and Pauli component on the complete even-`N` singlet sector.
2. `P_0 |s><t|_i P_0 = (delta_st/2) P_0` and exact known-site erasure recovery.
3. arbitrary-reference stability of the recovery.
4. the physical-support isometry `W_i : C^2_v tensor C_0 -> H_bar_i` with `E_i(rho)=W_i[(I_2/2) tensor rho]W_i^dagger`.
5. existence of a full-algebra CPTP recovery whose off-image completion is nonunique.
6. the closure lemma `Phi = Lambda o Ad_U o R` with `Phi o Lambda = Lambda o Ad_U` on the physical domain.
7. exact fixed per-`N` reconstructive record dynamics for `J2/J4/J6` at `N=8,10,12`.

## Scope ceilings

The manuscript must not claim unknown-location erasure, multi-spin erasure, strict minimality, minimum-support growth, a common cross-`N` map, genuinely lossy closure, semigroup/Markovianity, thermodynamic irreversibility, continuum physics, geometry, gravity, or quantum gravity.

## Novelty ceiling after PR #254

`ONE_PARTICLE_LOSS_IMMUNITY = KNOWN_PRIOR_ART`.

`NOVELTY_UNRESOLVED` remains only for the precise `W_i` channel packaging, full-algebra completion formulation, reconstructive-autonomy synthesis, and their BCRD-specific conjunction.

No use of “first”, “new”, “novel”, “previously unknown”, or “unprecedented” is authorized before the dedicated novelty audit.
