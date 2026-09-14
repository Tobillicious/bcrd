# REVISION AFTER HR #253

Governing manuscript review: PR #253 / `846267c2abb15c8e659aeeec08efc2ed4dd9ce58`.

Scientific cutoff remains PR #223 / `0a598dceefff780ccb1e1a25caceda4d30643997`.

| review finding | revision made | manuscript/artifact path | new science? |
|---|---|---|---|
| primary term “underidentification” imprecise | replaced primary terminology with finite-data non-identification / set-membership ambiguity; removed mechanical/rhetorical uses | `main.tex`, `sections/introduction.tex`, `sections/identification.tex`, `sections/conclusion.tex`, `CLAIMS.md` | NO |
| title should be publication-safe | title revised to **Finite-Data Non-Identification of Effective Quantum Coarse Dynamics** | `main.tex`, `README.md` | NO |
| author metadata | formal name set to Tobias Croydon-McRae | `main.tex`, `README.md` | NO |
| incomplete-QPT positioning missing | added direct engagement with Ziman (2008) and Teo et al. (2011) | `sections/introduction.tex`, `sections/literature.tex`, `references.bib`, `LITERATURE-NOTES.md` | NO |
| classical set-membership positioning required | hardened relation to Milanese & Novara (2004, 2011) and separated known framework from BCRD finite case | `sections/introduction.tex`, `sections/literature.tex`, `LITERATURE-NOTES.md` | NO |
| novelty language too strong | removed “unusually sharp” / priority cues; explicitly disclaimed novelty for generic non-identification/incomplete tomography | `sections/introduction.tex`, `sections/literature.tex`, `LITERATURE-NOTES.md` | NO |
| K=4 inference needed rewording | explicitly states at least two K=4 tolerance-feasible maps, not universal estimator failure | `main.tex`, `sections/results.tex`, `sections/identification.tex`, `CLAIMS.md` | NO |
| frozen-witness vs class failure distinction | made explicit throughout | `sections/results.tex`, `sections/discussion.tex`, `CLAIMS.md` | NO |
| main logic figure clipped / misleading | replaced with vertical custody/inference diagram fitting page width | `figures/fit-vs-prediction.tex` | NO |
| feasible-set ellipses could imply geometry | replaced with abstract nested boxes and explicit not-to-scale/non-geometric disclaimer | `figures/nested-feasible-sets.tex` | NO |
| precision/custody | preserved canonical shared endpoint `0.9323881824729999` | `sections/physical-setting.tex`, `reproducibility/transition-dataset.csv` | NO |
| public reproducibility chain insufficient | prepared curated packet with exact map blobs, reviewer outputs, manifests, checksums and verifier | `reproducibility/` | NO |
| PR #253 authority needed | recorded as manuscript-review authority only; PR #223 remains scientific cutoff | `AUTHORITIES.md`, `reproducibility/authority-manifest.md` | NO |
| Markov/memory/autonomy scope | retained only as explicit nonclaims/firewalls | `main.tex`, `sections/introduction.tex`, `sections/literature.tex`, `sections/discussion.tex`, `CLAIMS.md` | NO |
| empty feasible-set semantics | retained: empty means class incompatibility; no zero-diameter convention | `sections/framework.tex`, `sections/identification.tex`, `CLAIMS.md` | NO |
| render quality major fixes | rebuilt and inspected all 18 pages; zero overfull/underfull boxes | `BUILD-REPORT-AFTER-HR-253.md` | NO |

## Central artifact-to-claim mapping

| central claim | publication packet artifact |
|---|---|
| exact six transitions and endpoint custody | `reproducibility/transition-dataset.csv` |
| exact physical map class and half-diamond normalization | `reproducibility/physical-map-class.md` |
| exact frozen `Phi_4` | `reproducibility/maps/Phi4-candidate-map-dyadic.npz` |
| prospective F1/F2 failure of `Phi_4` | `reproducibility/verification/prospective-hostile-certificate.json` |
| exact accepted `Phi_6` | `reproducibility/maps/Phi6-C-S2-frob-pr213.npz` |
| K=6 hostile rigorous uppers | `reproducibility/verification/k6-reviewer-recomputation-summary.json` |
| K=6 universal lower | `reproducibility/verification/k6-L6-AUDIT.md` |
| K=4/K=6 logical claims and nonclaims | `reproducibility/certificate-summary.json` |
| exact source PR/SHA/path/blob identities | `reproducibility/authority-manifest.md`, `reproducibility/MANIFEST.json` |
| artifact hashes | `reproducibility/CHECKSUMS.sha256` |
| mechanical package check | `reproducibility/verification/verify_packet.py` |

## Revision firewalls

```text
scientific_result_changed = NO
new_physics_performed = NO
new_transition_opened = NO
new_map_optimization_performed = NO
new_lower_bound_search_performed = NO
K_greater_than_6_executed = NO
N10_N12_imported = NO
later_N4_lane_inspected = NO
quantum_gravity_claimed = NO
```
