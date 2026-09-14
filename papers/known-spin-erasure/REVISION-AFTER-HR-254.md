# PAPER-BCRD-KNOWN-SPIN-ERASURE-001 — bounded revision after hostile review PR #254

Date: 2026-09-14

Revision branch: `sol/revise-paper-known-spin-erasure-after-review-2026-09-14-r1`

Frozen manuscript authority: PR #252 at `39cadaa06eb359f8d6f0b58b43f42210e39e2058`.

Governing manuscript-review authority: PR #254, contract `44ef1f7509dcedf2731ed97daf5f6502e4995f2f`, terminal `7622473f21276f014224954a21ae8f26b22a2fbf`.

## Old versus revised contribution statement

**Old centre:** exact autonomous closure *from known-spin erasure*, with the novelty status of the complete singlet erasure theorem left unresolved.

**Revised centre:** one-particle-loss immunity of collective-symmetry DFS/singlet encodings is treated as direct known prior art; the paper uses a channel-level recasting of that mechanism to derive and classify **exact reconstructive autonomous closure**, explicitly distinguishing it from genuinely lossy autonomous coarse-graining.

## Title

Old:

> Exact Autonomous Closure from Known-Spin Erasure in Finite Singlet Quantum Systems

Revised:

> Exact Reconstructive Autonomous Closure in Finite Singlet Quantum Systems

## Direct prior-art finding

Migdał & Banaszek, *Physical Review A* 84, 052318 (2011), DOI `10.1103/PhysRevA.84.052318`, arXiv:1107.3786:

- code family: collective-`SU(d)` decoherence-free subspace;
- loss model: removal of one particle;
- qubit specialization: explicit complete even-`n` singlet / total-spin-zero DFS;
- recovery: explicit four-qubit recovery plus general `SU(d)` proof of immunity;
- representation theory: Clebsch–Gordan multiplicity structure for qubits and general `SU(d)` representation structure;
- manuscript implication: underlying one-particle-loss immunity is known prior art and is no longer a novelty candidate.

The located paper does not organize the result in the same `P_0 sigma_i P_0` / `W_i` / full-algebra-completion / autonomous-record language used here. This difference is **not** treated as evidence of novelty.

## Revision ledger

| hostile-review finding | manuscript change | file / section | scientific content changed? |
|---|---|---|---|
| Direct matching prior art located | Added Migdał–Banaszek 2011 prominently and closed the old search-status ambiguity | `references.bib`, `LITERATURE-NOTES.md`, `AUTHORITIES.md`, Introduction, QEC relation | NO — publication framing only |
| Title over-centred known erasure mechanism | Retitled around reconstructive autonomous closure | `main.tex`, `README.md` | NO — publication framing only |
| Abstract novelty positioning too ambiguous | Abstract now opens with reconstructive-autonomy question, explicitly treats particle-loss immunity as known, and withholds priority claims for packaging/synthesis | `main.tex` | NO — publication framing only |
| Introduction needed recentering | Rewritten around reconstructive vs genuinely lossy closure; BCRD chronology moved out of the conceptual opening | `sections/introduction.tex` | NO — publication framing only |
| Erasure theorem survived but required honest attribution | Retitled theorem as known particle-loss immunity recast in channel form; preserved proof and scope | `sections/erasure.tex` | NO — theorem unchanged |
| `W_i` language needed scope hardening | Explicitly limited `W_i` to an isometric tensor structure on the reachable physical support | `main.tex`, Introduction, `sections/erasure.tex` | NO — presentation/scope only |
| Full-algebra completion could imply uniqueness | Explicitly stated that exact action is fixed on-image and off-image completion is nonunique | `sections/erasure.tex`, `CLAIMS.md` | NO — clarification only |
| Autonomous closure should be conceptual centre | Abstract/Introduction/Conclusion now foreground `recoverability => exact closure` | `main.tex`, Introduction, Conclusion | NO — publication framing only |
| Reconstructive vs lossy distinction needed strengthening | Promoted the distinction to the paper’s central conceptual classification and blocked irreversibility/Markovianity inferences | Abstract, Introduction, Conclusion, `CLAIMS.md` | NO — interpretation only |
| Literature classification needed explicit categories | Added STANDARD QEC/DFS, DIRECT PRIOR ART, MANUSCRIPT REFORMULATION, BCRD-SPECIFIC APPLICATION, NOVELTY STILL UNDER AUDIT | `sections/qec-relation.tex`, `LITERATURE-NOTES.md`, `CLAIMS.md` | NO — publication framing only |
| Author publication name incorrect | Replaced metadata author with `Tobias Croydon-McRae` | `main.tex` | NO — metadata only |
| PR #254 needed authority separation | Added as manuscript/publication authority without changing scientific SHAs | `AUTHORITIES.md`, `README.md` | NO — provenance only |

## Preserved finite-construction scope

```text
N = 8  -> J2
N = 10 -> J4
N = 12 -> J6
```

Still explicitly excluded: common cross-`N` map, strict minimality, minimum-support-growth theorem, asymptotic theorem, and genuinely lossy closure.

## Novelty ceiling after revision

```text
ONE_PARTICLE_LOSS_IMMUNITY = KNOWN PRIOR ART
W_i_PACKAGING_NOVELTY = UNRESOLVED
FULL_ALGEBRA_COMPLETION_NOVELTY = UNRESOLVED
RECONSTRUCTIVE_AUTONOMY_SYNTHESIS_NOVELTY = UNRESOLVED
```

No “first”, “new”, “novel”, “previously unknown”, or “unprecedented” wording is authorized for those unresolved items.

## Science firewall

```text
NEW_PHYSICS_PERFORMED = NO
NEW_SCIENTIFIC_WORK_REQUIRED = NO
```

This revision changes attribution, manuscript centre, literature positioning, and presentation only. The reviewed mathematics and scientific SHAs are preserved.
