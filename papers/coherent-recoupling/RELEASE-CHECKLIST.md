# Release checklist — conditional coherent-recoupling paper

Status: **V3 RECONCILIATION PENDING / RELEASE BLOCKED**

A checked item means the stated condition is evidenced by a frozen authority or a directly verified custody fact, not merely intended.

## Current staging checks

- [x] Paper ID assigned: `PAPER-BCRD-COHERENT-RECOUPLING-001`.
- [x] Formal author name fixed: Tobias Croydon-McRae.
- [x] DESIGN_V2 reconciliation custody recorded: PR #275 @ `f30ce29373dba21febf8d8106ea87e800852b09c`.
- [x] Current programme ceiling retained at L2.
- [x] No native N=6 result imported.
- [x] DESIGN_V3 author design existence recorded as provisional custody only: PR #276.
- [x] DESIGN_V3 independent blind hostile design review existence recorded as provisional custody only: PR #277.
- [x] DESIGN_V3 reconciliation remains unfrozen in this staging authority state.
- [x] PR #276/#277 scientific content is not promoted into the canonical claim ledger.
- [x] General pre-result literature/novelty audit recorded as completed with 34 verified bibliography entries.
- [x] Priority claim remains unestablished.
- [x] Result-specific targeted novelty addendum remains pending after reconciliation.
- [x] No DOI created.
- [x] No release tag created.
- [x] No GitHub Release created.
- [x] No Figshare item created by this lane.
- [x] No arXiv submission made by this lane.
- [x] No journal submission made by this lane.

## V3 authority gates

- [x] DESIGN_V3 author design exists: PR #276 — **custody only, noncanonical pending reconciliation**.
- [x] Independent blind hostile design review exists: PR #277 — **custody only, noncanonical pending reconciliation**.
- [ ] `[V3-RECONCILIATION-PENDING: DESIGN_V3 author/review reconciliation frozen with final canonical design disposition]`.
- [ ] `[V3-PENDING: execution/interface governance frozen before native outcome inspection]`.
- [ ] `[V3-PENDING: native N=6 author execution completed under frozen design/governance]`.
- [ ] `[V3-PENDING: raw result and controls banked with custody evidence]`.
- [ ] `[V3-PENDING: independent hostile scientific review completed]`.
- [ ] `[V3-PENDING: second independent review completed if required by programme governance]`.
- [ ] `[V3-PENDING: final V3 scientific reconciliation completed]`.
- [ ] `[V3-PENDING: final strongest claim level explicitly frozen]`.

## Literature / novelty gates

- [x] General pre-result literature/novelty audit completed.
- [x] Verified bibliography entries = 34.
- [x] Standard Racah/Wigner/6j recoupling grounded.
- [x] Endpoint rephasing and isolated 2x2 obstruction grounded.
- [x] Structural/algebraic identifiability and elimination/model-variety literature grounded.
- [x] Parameter-free polynomial discrimination and quantum-system-identification literature grounded.
- [x] Rigorous numerical-certification literature grounded.
- [x] Prior operational F/R extraction and Racah-as-quantum-operation literature grounded.
- [x] Broad novelty/priority claim **not** established.
- [ ] `[V3-PENDING: design/result-specific targeted novelty addendum after reconciliation]`.

## Manuscript gates

- [ ] `[V3-PENDING: reconciled V3 design/result incorporated without changing pre-V3 claims]`.
- [ ] All scientific assertions map to `AUTHORITY-MANIFEST.json`.
- [ ] `CLAIM-LEDGER.md` agrees with the final manuscript.
- [ ] Literature/novelty wording agrees with the completed general audit and the later result-specific targeted addendum.
- [ ] No unsupported priority wording remains.
- [ ] No quantum-gravity shorthand is used for ordinary Racah/6j mathematics.
- [ ] Every figure is either supported by frozen evidence or explicitly conceptual/not-to-scale.
- [ ] Every table value is traceable to a frozen authority.
- [ ] Every equation/result copied from an authority is exact and source-located.
- [ ] Search entire release tree for `V3-PENDING` and `V3-RECONCILIATION-PENDING`; required result: zero unresolved matches in the final release.
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
- [ ] PR #276/#277 content checked for promotion only through frozen reconciliation authority.
- [ ] `[V3-PENDING: V3 positive/negative/null findings checked against final reconciliation]`.
- [ ] General literature audit and targeted novelty addendum distinguished correctly.
- [ ] Priority claim remains absent unless explicitly established downstream.
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
- [ ] Frozen non-moving release tag created only after all pre-tag checks pass: `paper/coherent-recoupling/vMAJOR.MINOR.PATCH`.
- [ ] Project policy recorded: release tag is non-moving after creation.
- [ ] No technical tag-immutability claim is made unless independently verified repository protection actually enforces it.
- [ ] Tag points exactly to commit A.
- [ ] Tag has never existed previously.
- [ ] No intentional force-move or tag replacement permitted by project policy.

## Archive / DOI gates

- [ ] Archive metadata finalized from `FIGSHARE-METADATA.md` or deliberately selected alternative.
- [ ] Archive payload exported from commit A/tag, not mutable working tree.
- [ ] Uploaded artifact hashes verified against manifest before archive publication where platform workflow permits.
- [ ] Archive description records commit A and the frozen non-moving release tag by project policy.
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

- [ ] Final venue selected only after V3 result strength and result-specific novelty addendum are known.
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
git_tag = [V3-PENDING: frozen non-moving version tag by project policy]
archive_doi = [V3-PENDING: DOI]
release_executed = NO
```
