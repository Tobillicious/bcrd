# Conditional BCRD Coherent-Recoupling Paper — pre-V3 staging package

Paper ID: `PAPER-BCRD-COHERENT-RECOUPLING-001`

Formal author name: **Tobias Croydon-McRae**

Status: **PRE-V3 / NOT RELEASED / NOT CITEABLE AS A FINAL RESULT**

This directory is a release-engineering staging area for the next conditional BCRD paper. It contains only material that can be frozen before DESIGN_V3 resolves. It does not create a DOI, GitHub release, archive deposit, arXiv submission, journal submission, or scientific result.

## Scientific firewall

The current programme ceiling is the frozen pre-V3 ceiling. No file in this directory may be read as predicting, inferring, or filling the future native N=6 result.

The evidential progression captured by the paper is:

1. N=4 phase sensitivity is operationally established at the reconciled L2 scope.
2. Mechanism attribution remains underdetermined at that scope.
3. A closed unitary 2x2 mixing map has no nontrivial continuous phase invariant after independent endpoint rephasings.
4. N=6 supplies a richer multipath architecture.
5. DESIGN_V2 is not execution-ready: its HELD-R1 relation is exact but non-identifying, Gate D is structurally inconsistent with the proposed Racah class, and the numerical exactness gate requires redesign.
6. The next scientific direction is algebraic identifiability under a separately frozen prospective design.
7. `[V3-PENDING: DESIGN_V3 design, execution, independent review, reconciliation, and final conditional disposition]`.

No stronger claim is encoded here.

## Frozen pre-V3 authority spine

The machine-readable ledger is `AUTHORITY-MANIFEST.json`. The current terminal pre-V3 authority is:

```text
physics-lane PR #275
terminal reconciliation head:
f30ce29373dba21febf8d8106ea87e800852b09c

maximum programme claim after reconciliation = L2
native N=6 target outcome inspected = NO
new N=6 physics executed = NO
DESIGN_V3 authored = NO
```

## Required release chain

The final release must preserve this provenance direction:

```text
frozen scientific authorities
  -> frozen final manuscript source
  -> exact public-repository frozen target commit/tag
  -> archive deposit of that exact target
  -> archive DOI
  -> DOI recorded back into a metadata-only repository commit
```

The DOI may point back to the frozen GitHub target, but the GitHub target must not be rewritten after the archive snapshot. See `REPRODUCIBILITY.md` and `RELEASE-CHECKLIST.md`.

## Tag and release naming convention

Until V3 resolves, **no tag is to be created**.

Proposed final convention:

```text
Git tag:      paper/coherent-recoupling/vMAJOR.MINOR.PATCH
Release name: PAPER-BCRD-COHERENT-RECOUPLING-001 vMAJOR.MINOR.PATCH
Archive title: [V3-PENDING: final paper title] — reproducibility release vMAJOR.MINOR.PATCH
```

Recommended first immutable public version, if and only if the final publication gate passes:

```text
paper/coherent-recoupling/v1.0.0
```

Use a new semantic version for every scientific or reproducibility change. Never retarget an existing tag.

## Package files

- `CITATION.cff` — non-release citation metadata with no DOI.
- `PUBLICATION-RELEASE.json` — release record template; all final fields remain pending.
- `AUTHORITY-MANIFEST.json` — frozen pre-V3 authorities plus reserved V3 slots.
- `REPRODUCIBILITY.md` — exact-copy, hashing, build, and provenance procedures.
- `CLAIM-LEDGER.md` — publication-safe claims, nonclaims, and V3-dependent claims.
- `ARTIFACT-MANIFEST.sha256` — checksum-manifest template only.
- `RELEASE-CHECKLIST.md` — mechanical pre-publication and release gates.
- `FIGSHARE-METADATA.md` — archive-deposit template; no item/DOI created.
- `ARXIV-METADATA.md` — arXiv metadata template; no submission performed.
- `JOURNAL-SUBMISSION-METADATA.md` — conditional venue fit and submission fields.
- `COVER-LETTER-DRAFT.md` — conditional, non-submitted cover-letter scaffold.
- `PUBLIC-README-PATCH.md` — proposed root-README patch, deliberately not applied.

## Stop rule

Do not create a DOI, tag, GitHub Release, Figshare item, arXiv submission, journal submission, or final public-paper entry while any `[V3-PENDING: ...]` field remains unresolved.
