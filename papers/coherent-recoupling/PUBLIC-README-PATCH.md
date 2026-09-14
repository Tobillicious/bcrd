# Proposed public README patch — DO NOT APPLY PRE-V3

This file contains a proposed future addition to the repository root `README.md`. It is deliberately stored as a patch proposal rather than applied, because the paper is not yet releasable.

Apply only after `[V3-PENDING: final V3 scientific reconciliation]`, `[V3-PENDING: final hostile claim audit]`, and `[V3-PENDING: publication-readiness closure]` all pass.

## Proposed insertion

```markdown
### Conditional coherent recoupling / structural identifiability

**[V3-PENDING: final paper title]**  
Author: Tobias Croydon-McRae  
Paper ID: `PAPER-BCRD-COHERENT-RECOUPLING-001`  
Status: `[V3-PENDING: released preprint / submitted article / published article]`  
DOI: `[V3-PENDING: archive DOI]`  
Frozen source: `[V3-PENDING: immutable GitHub tag and commit]`

This paper develops the BCRD coherent-recoupling line from the reviewed N=4 phase-sensitive L2 result through the 2x2 endpoint-rephasing obstruction and the N=6 multipath identifiability programme. The pre-V3 record includes the independently reviewed failure of DESIGN_V2 as a Racah-identifying test: HELD-R1 is exact but non-identifying, Gate D is structurally inconsistent with the proposed Racah class, and finite numerical tolerance does not certify exact equality.

[V3-PENDING: one publication-safe sentence stating the final reconciled V3 result and strongest claim ceiling.]

Reproducibility, frozen authorities, claim ledger, checksum manifest, and release metadata are in [`papers/coherent-recoupling/`](papers/coherent-recoupling/).
```

## Application rules

When this patch is eventually applied:

1. replace every `[V3-PENDING: ...]` field from frozen authority only;
2. do not rewrite the pre-V3 failure history to make the final result look inevitable;
3. do not use "quantum gravity" unless the final authority actually establishes it;
4. link the DOI only after it exists;
5. link the immutable tag/commit, not a moving branch;
6. include the root-README change in the metadata-only DOI-backlink commit if the scientific frozen target has already been archived.
