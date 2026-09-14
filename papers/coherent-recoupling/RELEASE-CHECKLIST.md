# Release checklist — conditional coherent-recoupling paper

Status: **PRE-V3 / RELEASE BLOCKED**

A checked item means the stated condition is evidenced by an immutable authority, not merely intended.

## Pre-V3 staging checks

- [x] Paper ID assigned: `PAPER-BCRD-COHERENT-RECOUPLING-001`.
- [x] Formal author name fixed: Tobias Croydon-McRae.
- [x] Current pre-V3 terminal authority recorded: PR #275 @ `f30ce29373dba21febf8d8106ea87e800852b09c`.
- [x] Current pre-V3 programme ceiling retained at L2.
- [x] No native N=6 result imported.
- [x] No DESIGN_V3 result inferred.
- [x] No DOI created.
- [x] No release tag created.
- [x] No GitHub Release created.
- [x] No Figshare item created by this lane.
- [x] No arXiv submission made by this lane.
- [x] No journal submission made by this lane.

## V3 authority gates

- [ ] `[V3-PENDING: DESIGN_V3 frozen prospectively with exact contract and terminal SHA]`.
- [ ] `[V3-PENDING: independent hostile design review completed]`.
- [ ] `[V3-PENDING: design reconciliation completed if review disagreements require it]`.
- [ ] `[V3-PENDING: execution/interface governance frozen before native outcome inspection]`.
- [ ] `[V3-PENDING: native N=6 author execution completed under frozen design]`.
- [ ] `[V3-PENDING: raw result and controls banked with custody evidence]`.
- [ ] `[V3-PENDING: independent hostile scientific review completed]`.
- [ ] `[V3-PENDING: second independent review completed if required by the programme governance]`.
- [ ] `[V3-PENDING: final V3 scientific reconciliation completed]`.
- [ ] `[V3-PENDING: final strongest claim level explicitly frozen]`.

## Manuscript gates

- [ ] `[V3-PENDING: V3 result incorporated without changing pre-V3 claims]`.
- [ ] All scientific assertions map to `AUTHORITY-MANIFEST.json`.
- [ ] `CLAIM-LEDGER.md` agrees with the final manuscript.
- [ ] Literature/novelty wording agrees with the final independent literature audit.
- [ ] No unsupported priority wording remains.
- [ ] No quantum-gravity shorthand is used for ordinary Racah/6j mathematics.
- [ ] Every figure is either supported by frozen evidence or explicitly conceptual/not-to-scale.
- [ ] Every table value is traceable to a frozen authority.
- [ ] Every equation/result copied from an authority is exact and source-located.
- [ ] Search entire release tree for `V3-PENDING`; required result: zero matches.
- [ ] Search entire release tree for stale placeholders such as `TODO`, `TBD`, `FIXME`, and adjudicate every match.

## Final hostile claim audit

The hostile auditor must work from the exact frozen manuscript head and must not silently repair claims while reviewing.

- [ ] Abstract ceiling checked.
- [ ] Title ceiling checked.
- [ ] Introduction/novelty positioning checked.
- [ ] N=4 L2 scope checked.
- [ ] Mechanism-underdetermination wording checked.
- [ ] 2x2 rephasing theorem scope checked.
- [ ] N=6 architecture/minimality wording checked.
- [ ] HELD-R1 exact-but-nonidentifying wording checked.
- [ ] Gate-D structural inconsistency wording checked.
- [ ] Exact-vs-numerical certification wording checked.
- [ ] `[V3-PENDING: V3 positive/negative/null findings checked against reconciliation]`.
- [ ] F-move/pentagon/Pachner/Regge/QG nonclaim boundary checked.
- [ ] Figures/captions checked.
- [ ] Supplementary/reproducibility prose checked.
- [ ] README/CITATION/archive metadata checked.
- [ ] arXiv metadata checked.
- [ ] journal metadata and cover letter checked.
- [ ] Final audit disposition frozen: `[V3-PENDING: PASS + terminal hostile-claim-audit SHA]`.

**Hard stop:** any failed or unresolved item above blocks release.

## Reproducibility gates

- [ ] `[V3-PENDING: final manuscript source SHA frozen]`.
- [ ] Final source exported from exact SHA, not moving branch.
- [ ] Exact-copy ledger records source Git blobs and destination paths.
- [ ] SHA-256 equality verified for every custody-copied artifact.
- [ ] Public reproducibility packet is self-contained for all load-bearing calculations required by the final paper.
- [ ] Clean-environment reproduction succeeds without private-repository archaeology.
- [ ] Failure-sensitivity/mutation controls exist where needed to show the verifier is not vacuous.
- [ ] Build toolchain versions recorded.
- [ ] LaTeX build passes.
- [ ] Undefined references = 0.
- [ ] Undefined citations = 0.
- [ ] Material overfull/underfull boxes = 0.
- [ ] Every rendered page inspected.
- [ ] Final PDF SHA-256 recorded.
- [ ] `ARTIFACT-MANIFEST.sha256` mechanically generated from final release tree.
- [ ] Checksum manifest verifies cleanly from a fresh export.
- [ ] Manifest's own SHA-256 recorded separately in `PUBLICATION-RELEASE.json`.

## Freeze and tag gates

- [ ] `[V3-PENDING: public frozen target commit A created]`.
- [ ] Working tree clean at commit A.
- [ ] Commit A contains no release-inconsistent placeholders.
- [ ] Immutable tag created only after all pre-tag checks pass: `paper/coherent-recoupling/vMAJOR.MINOR.PATCH`.
- [ ] Tag points exactly to commit A.
- [ ] Tag has never existed previously.
- [ ] No force-move or tag replacement permitted.

## Archive / DOI gates

- [ ] Archive metadata finalized from `FIGSHARE-METADATA.md` or deliberately selected alternative.
- [ ] Archive payload exported from commit A/tag, not mutable working tree.
- [ ] Uploaded artifact hashes verified against manifest before archive publication where platform workflow permits.
- [ ] Archive description records commit A and immutable tag.
- [ ] Archive publication intentionally authorized.
- [ ] `[V3-PENDING: archive DOI created]`.
- [ ] DOI resolves to correct version and files.
- [ ] DOI recorded in `PUBLICATION-RELEASE.json` only after assignment.
- [ ] Metadata-only GitHub commit B records DOI and points back to commit A/tag.
- [ ] Commit B changes no scientific/reproducibility artifact.
- [ ] Tag remains on commit A.

## arXiv gates

- [ ] Venue/preprint timing checked against selected journal policy.
- [ ] arXiv category chosen deliberately.
- [ ] arXiv title/abstract identical in claim strength to final manuscript.
- [ ] Source package builds under arXiv-compatible TeX environment or incompatibilities are resolved without changing science.
- [ ] `[V3-PENDING: arXiv submission authorization]`.
- [ ] `[V3-PENDING: arXiv identifier recorded after submission]`.

## Journal submission gates

- [ ] Final venue selected only after V3 result strength and novelty are known.
- [ ] Journal scope rechecked on submission date.
- [ ] Journal article type selected.
- [ ] Cover letter updated from scaffold without claim inflation.
- [ ] Data/code availability statement matches actual public packet.
- [ ] Conflicts/funding/author declarations completed accurately.
- [ ] `[V3-PENDING: journal submission authorization]`.
- [ ] `[V3-PENDING: manuscript identifier recorded after submission]`.

## Terminal release disposition

```text
release_ready = [V3-PENDING: YES/NO]
release_authority = [V3-PENDING: terminal publication-readiness SHA]
public_frozen_target_sha = [V3-PENDING: commit A]
git_tag = [V3-PENDING: immutable version tag]
archive_doi = [V3-PENDING: DOI]
release_executed = NO
```
