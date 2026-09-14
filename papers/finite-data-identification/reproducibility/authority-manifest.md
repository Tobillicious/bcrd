# Authority manifest

This packet is a curated publication object. It does not replace the frozen review chain; it maps each public-facing object back to exact repository custody.

## Manuscript authorities

```text
frozen manuscript PR #251 = 3433b889a301beb41a55a694337fb75f9b9994f6
manuscript review PR #253 = 846267c2abb15c8e659aeeec08efc2ed4dd9ce58
PR #253 review contract = f09b7dd42775750068e6e0466d037009dbb86969
scientific cutoff PR #223 = 0a598dceefff780ccb1e1a25caceda4d30643997
```

PR #253 is a manuscript-review authority, not a new scientific authority.

## Load-bearing scientific objects

| packet object / claim | source PR | source terminal | source path / identity | source Git blob | scientific SHA-256 / reviewed value |
|---|---:|---|---|---|---|
| `maps/Phi4-candidate-map-dyadic.npz` | #213 | `1ad514541a6c8977db80a6ab7ac1a2bda3257107` | `orthogonal-validation/bcrd-r207-four-transition-common-cptp-2026-09-13/artifacts/candidate-map-dyadic.npz` | `302991a3f3737bcfc3920fa8d7f5a6611feb6b62` | `48abd5f52812ef7503cfdde92fe630b99ded9c10c4ef35d2c4edc8d934028125` |
| K=4 physical common-map existence | #213/#214 | author `1ad514...`; review `683e83807df926664268fd6600d8900972485fd5` | frozen Phi4 plus hostile U1 audit | -- | worst reviewed upper `0.006670414972746646...` |
| prospective Phi4 failure | #219/#220/#221 | author `4de999a05a0173b5f82c4b572dad1479bc5bb33c`; review `069b9edba77358bcedc9fffe256ecf006c846bc0`; reconciliation `dc782001d75247ab1c56d9ee52aac430c12333cc` | reviewer certificate copied as `verification/prospective-hostile-certificate.json` | `e54250c2d36400029a42d8117468ab756b0e147c` | F1 >= `0.6246936110454476`; F2 >= `0.6217658417777687` |
| `maps/Phi6-C-S2-frob-pr213.npz` | #222 | `bdf8597aa427abb789805fb331c32932bf97de28` | `orthogonal-validation/bcrd-r207-n8-six-transition-common-cptp-2026-09-13/artifacts/candidates/C-S2-frob-pr213.npz` | `3c16236a601745b1b55d766bc6fa5a5177c81a78` | `c674e471c6bbad2e3376e53315d8e1e5cb83dbbb85f4120c7b5b8602b78f7e0a` |
| K=6 reviewer recomputation | #223 | `0a598dceefff780ccb1e1a25caceda4d30643997` | copied as `verification/k6-reviewer-recomputation-summary.json` | `48772b4800e3c489d399b5aeb132d6178cddd71b` | U6 `0.004582638648933954...` |
| K=6 universal lower audit | #223 | `0a598dceefff780ccb1e1a25caceda4d30643997` | copied as `verification/k6-L6-AUDIT.md` | `fdbb565cd4b71bcf64ae37cff43ca7adf6f2b518` | L6 `0.002306082156934015...` |

## Representation-only post-cutoff custody

The canonical shared TRAIN0/TRAIN1 endpoint `0.9323881824729999` may be cross-checked against methodology/custody PR #226. That use is `CUSTODY_REPRESENTATION_ONLY`; it does not change the scientific cutoff.

## Firewalls

This packet contains no N=10/N=12 result, no K>6 execution, no later BCRD scientific result, and no N=4 coherent-Racah result. No map was refit or altered while constructing the packet.
