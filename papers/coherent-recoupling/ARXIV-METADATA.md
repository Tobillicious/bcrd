# arXiv metadata template

Status: **TEMPLATE ONLY — NO arXiv SUBMISSION AUTHORIZED**

## Core metadata

- Title: `[V3-PENDING: final reconciled paper title]`
- Authors: `Tobias Croydon-McRae`
- Abstract: `[V3-PENDING: final abstract copied from the exact frozen manuscript without claim strengthening]`
- Comments: `[V3-PENDING: page count, figure count, reproducibility/DOI note, and journal-submission status if appropriate]`
- Journal reference: `[V3-PENDING: only after a journal reference exists]`
- DOI: `[V3-PENDING: archive DOI and/or journal DOI when actually assigned]`
- Report number: leave blank unless a real institutional/report number is created.

## Category selection

Do not freeze a category before the final scientific disposition.

Candidate logic:

- `quant-ph` is the natural primary candidate if the final paper centres operational quantum dynamics, quantum measurement/process identification, coherent-control structure, or quantum-information-theoretic identifiability.
- `math-ph` is a plausible primary or cross-list if the final paper is principally an exact mathematical-physics result about recoupling, representation-theoretic constraints, rephasing quotients, and structural identifiability.
- A high-energy/gravity category is **not** justified merely by Racah/6j, Ponzano-Regge background, or spin-network language.

Final choice: `[V3-PENDING: primary arXiv category and any justified cross-list]`.

## Submission-source package

The arXiv source must be exported from the same frozen manuscript authority used for the public release. Any arXiv-specific TeX compatibility edit must be publication-only, scientifically inert, mechanically recorded, and followed by a rebuilt PDF comparison.

Required checks:

- `[V3-PENDING: frozen final manuscript SHA recorded]`
- source compiles in an arXiv-compatible environment;
- bibliography is included in accepted source form;
- all figures are included with compatible formats;
- no private/local absolute paths;
- no missing generated files;
- no `[V3-PENDING: ...]` tokens;
- abstract/title match the final claim ceiling;
- checksum of submitted source archive recorded if practical.

## Data/code statement for comments or abstract page

Suggested structure, only after the public packet exists:

> Reproducibility materials and frozen provenance: `[V3-PENDING: public repository/tag and archive DOI]`.

Do not insert a DOI or repository tag before it exists.

## Versioning

- arXiv v1 should correspond to `[V3-PENDING: exact frozen public/manuscript version]`.
- Any later scientific change requires an arXiv version update and a matching repository/archive version record.
- Editorial journal-format changes that do not alter science should still be documented if they change the arXiv source.

## Submission gate

```text
arxiv_submission_authorized = [V3-PENDING: YES/NO]
final_claim_audit = [V3-PENDING: PASS + SHA]
public_reproducibility_ready = [V3-PENDING: YES/NO]
arxiv_identifier = [V3-PENDING: identifier assigned after submission]
```
