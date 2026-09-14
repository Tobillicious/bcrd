# Figshare metadata template

Status: **TEMPLATE ONLY — DO NOT CREATE OR PUBLISH AN ITEM FROM THIS FILE YET**

## Record type

- Item type: `Preprint` or the closest supported scholarly-paper type.
- Title: `[V3-PENDING: final reconciled paper title]`
- Authors: `Tobias Croydon-McRae`
- Publication date: `[V3-PENDING: archive publication date]`
- Licence: `[V3-PENDING: final release licence, chosen consistently with manuscript and repository]`
- DOI: `[V3-PENDING: assigned by Figshare only after final release authorization]`

## Description template

`[V3-PENDING: final publication-safe abstract/description copied from the reconciled manuscript claim ceiling]`

Mandatory provenance paragraph to append after the scientific description:

> This archive is the frozen reproducibility release for `PAPER-BCRD-COHERENT-RECOUPLING-001` by Tobias Croydon-McRae. The deposited files are bound to the frozen public repository target `[V3-PENDING: Tobillicious/bcrd full commit SHA A]` and frozen non-moving release tag by project policy `[V3-PENDING: paper/coherent-recoupling/vMAJOR.MINOR.PATCH]`. SHA-256 checksums are provided in `ARTIFACT-MANIFEST.sha256`. The archive contains no scientific change relative to that frozen target. The project treats the release tag as non-moving; this metadata does not claim technical immutability unless repository protection is independently verified.

## Keywords

Pre-result stable candidates:

- Boundary-Complete Relational Dynamics
- BCRD
- quantum dynamics
- quantum information
- Racah recoupling
- Wigner 6j symbols
- coherent recoupling
- structural identifiability
- quantum measurements
- rephasing invariants

Add or remove result-specific keywords only after `[V3-PENDING: final scientific reconciliation]`.

## Categories / subjects

`[V3-PENDING: final Figshare subject categories selected after final result and venue positioning are known]`

Do not classify the record as quantum gravity merely because Racah/6j mathematics appears in the paper.

## Related material

- Code repository: `https://github.com/Tobillicious/bcrd`
- Frozen GitHub target: `[V3-PENDING: exact commit A URL]`
- Frozen non-moving release tag by project policy: `[V3-PENDING: exact tag URL]`
- Source scientific repository: `Tobillicious/physics-lane`
- Final manuscript authority: `[V3-PENDING: physics-lane SHA]`
- Final scientific reconciliation: `[V3-PENDING: physics-lane PR/SHA]`
- Final hostile claim audit: `[V3-PENDING: physics-lane PR/SHA]`

## Files to deposit

The exact file list must be generated from the frozen public target and checksum manifest. Expected classes are:

- `[V3-PENDING: final paper PDF]`
- `[V3-PENDING: manuscript source bundle]`
- `[V3-PENDING: figures/tables required for source reproduction]`
- `[V3-PENDING: public reproducibility packet]`
- `AUTHORITY-MANIFEST.json`
- `CLAIM-LEDGER.md`
- `REPRODUCIBILITY.md`
- `ARTIFACT-MANIFEST.sha256`
- `PUBLICATION-RELEASE.json`

Do not manually rebuild or reserialize frozen scientific artifacts for upload.

## Finalization gate

Before clicking any control that publicly finalizes the Figshare record:

```text
V3 scientific reconciliation = [V3-PENDING: PASS]
final hostile claim audit = [V3-PENDING: PASS]
publication readiness = [V3-PENDING: PASS]
public frozen target commit A = [V3-PENDING: SHA]
frozen non-moving release tag by project policy = [V3-PENDING: tag]
manifest verification = [V3-PENDING: PASS]
uploaded-byte verification = [V3-PENDING: PASS]
```

If any field remains pending, do not publish the archive record.
