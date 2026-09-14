# Conditional BCRD Coherent-Recoupling Paper — pre-result staging package

Paper ID: `PAPER-BCRD-COHERENT-RECOUPLING-001`

Formal author name: **Tobias Croydon-McRae**

Status: **V3 DESIGN/REVIEW EXIST; RECONCILIATION PENDING / NOT RELEASED / NOT CITEABLE AS A FINAL RESULT**

This directory is a release-engineering staging area for the next conditional BCRD paper. It contains only material that can be frozen before DESIGN_V3 reconciliation and native N=6 execution resolve. It does not create a DOI, GitHub release, archive deposit, arXiv submission, journal submission, or scientific result.

## Scientific firewall

The current programme ceiling remains the frozen L2 ceiling. No file in this directory may be read as predicting, inferring, or filling the future native N=6 result.

The evidential progression captured by the paper is:

1. N=4 phase sensitivity is operationally established at the reconciled L2 scope.
2. Mechanism attribution remains underdetermined at that scope.
3. A closed unitary 2x2 mixing map has no nontrivial continuous phase invariant after independent endpoint rephasings.
4. N=6 supplies a richer multipath architecture.
5. DESIGN_V2 is not execution-ready: its HELD-R1 relation is exact but non-identifying, Gate D is structurally inconsistent with the proposed Racah class, and the numerical exactness gate requires redesign.
6. The next scientific direction is algebraic identifiability under a separately frozen prospective design.
7. DESIGN_V3 authoring exists at PR #276 and an independent blind hostile design review exists at PR #277, but these are provisional custody facts only until design reconciliation freezes.
8. `[V3-PENDING: final reconciled DESIGN_V3 disposition, governance/execution authorities, native N=6 execution, scientific review/reconciliation, and final conditional disposition]`.

No stronger claim is encoded here.

## Current authority state

The machine-readable ledger is `AUTHORITY-MANIFEST.json`. The current canonical pre-result scientific ceiling remains:

```text
canonical pre-V3 programme state:
physics-lane PR #270 @ beb7370e5cf2cf990cfbdda0a13fc9f9c41e756a

DESIGN_V2 reconciliation custody:
physics-lane PR #275 @ f30ce29373dba21febf8d8106ea87e800852b09c

DESIGN_V3_AUTHOR_DESIGN_EXISTS = YES
DESIGN_V3_HOSTILE_REVIEW_EXISTS = YES
DESIGN_V3_RECONCILIATION_FROZEN = NO
DESIGN_V3_CANONICAL_AUTHORITY = PENDING

native_N6_target_outcome_inspected = NO
native_N6_execution_completed = NO
execution_authorized = NO
maximum_programme_claim = L2
```

Provisional noncanonical V3 custody:

```text
DESIGN_V3 author design:
PR #276
scientific terminal = 1104eebd9724cbaa44cce886e5c6968b558932ec
metadata head = 030eff9cffc9353c0604f3632e2c39e70cb15810
canonical disposition = [V3-RECONCILIATION-PENDING: final canonical design disposition]

Independent blind hostile design review:
PR #277
review contract = bff8c7d7fcb613dd0138528a25a6bcc8c927311a
scientific review terminal = 52b7bd5f72927d1fc76be16b14f1542a00a1372d
blind_review_integrity = CLEAN
canonical disposition = [V3-RECONCILIATION-PENDING: final canonical design disposition]
```

Neither PR #276 nor PR #277 is promoted into the canonical scientific claim ledger by this staging patch.

## Literature authority state

The independent general pre-result literature/novelty audit is complete:

```text
PRE_RESULT_LITERATURE_AUDIT = COMPLETED
verified_bibliography_entries = 34
priority_claim_established = NO
```

It supplies literature grounding for standard Racah/Wigner/6j recoupling; endpoint rephasing and the isolated 2x2 obstruction; structural/algebraic identifiability; elimination/model-variety methods; parameter-free polynomial model discrimination; quantum-system identification; rigorous numerical certification; and prior operational F/R extraction and Racah-as-quantum-operation work.

Broad novelty claims remain unsupported. The completed general audit does not replace the later result-specific slot:

`[V3-PENDING: design/result-specific targeted novelty addendum after reconciliation]`.

## Required release chain

The final release must preserve this provenance direction:

```text
final scientific authority
  -> frozen final manuscript source
  -> exact-copy verification
  -> public frozen commit A
  -> frozen non-moving release tag on commit A by project policy
  -> archive deposit of that exact target
  -> archive DOI
  -> DOI recorded back into metadata-only commit B
```

The DOI may point back to the frozen GitHub target, but commit A must not be rewritten after the archive snapshot and the project release tag must remain on commit A. See `REPRODUCIBILITY.md` and `RELEASE-CHECKLIST.md`.

## Tag and release naming convention

Until the final authority chain resolves, **no tag is to be created**.

Proposed final convention:

```text
Git tag:      paper/coherent-recoupling/vMAJOR.MINOR.PATCH
Release name: PAPER-BCRD-COHERENT-RECOUPLING-001 vMAJOR.MINOR.PATCH
Archive title: [V3-PENDING: final paper title] — reproducibility release vMAJOR.MINOR.PATCH
```

Recommended first frozen public version, if and only if the final publication gate passes:

```text
paper/coherent-recoupling/v1.0.0
```

By project policy, a release tag is non-moving after creation. This is a project custody rule, not a claim that Git technically prevents tag mutation. Use a new semantic version for every scientific or reproducibility change; never intentionally retarget an existing release tag.

## Package files

- `CITATION.cff` — non-release citation metadata with no DOI.
- `PUBLICATION-RELEASE.json` — release record template; all final fields remain pending.
- `AUTHORITY-MANIFEST.json` — frozen pre-result authorities, provisional V3 custody, completed general literature authority, and reserved downstream slots.
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

Do not authorize governance or execution, create a DOI, tag, GitHub Release, Figshare item, arXiv submission, journal submission, or final public-paper entry while the required reconciliation/execution/review/readiness fields remain unresolved.
