# Publication reproducibility packet

Paper: `PAPER-BCRD-FINITE-DATA-IDENTIFICATION-001`

Status: **publication-ready packet prepared in the private revision branch; not yet promoted to the public `Tobillicious/bcrd` repository.**

This directory is a curated immutable reproduction object for the paper's central finite-data result. It intentionally does **not** mirror the private development archive.

An external reader can determine from this packet:

1. the exact physical common-CPTP class;
2. the six transition endpoints, including the canonical binary64 shared endpoint;
3. the exact frozen K=4 witness `Phi4`;
4. the exact prospective F1/F2 lower certificates for that witness;
5. the exact accepted K=6 witness `Phi6`;
6. the reviewer-owned K=6 upper recomputation and universal lower audit;
7. which claims are exact set-theoretic deductions versus numerical/certified statements;
8. the PR/SHA/path/Git-blob authority for every load-bearing object.

## Central scientific statement

At tolerance `epsilon=0.01`, the four-transition dataset does not uniquely identify a tolerance-feasible physical map. The K=4 feasible set contains at least two distinct admissible maps. The exact frozen `Phi4` fails both prospectively selected F1/F2 transitions, while the unchanged full physical map class remains feasible after those transitions are added, with

```text
0.002306082156934015...
<= epsilon_*^(6)
<= 0.004582638648933954...
< 0.01.
```

This is **finite-data non-identification / set-membership ambiguity**, not map-class failure.

## Verification

Run from this directory after the two map files are present:

```bash
python3 verification/verify_packet.py
```

The wrapper verifies publication packaging only: immutable map SHA-256 digests, the canonical transition CSV, and the banked certificate-summary constants. It does **not** refit a map, open a transition, run a new lower-bound search, or pretend to re-derive the full diamond-norm certificates. Reviewer-owned certificate outputs are included separately so the scientific calculation remains traceable to its frozen authority.

`CHECKSUMS.sha256` supplies SHA-256 values for the immutable packet objects. `MANIFEST.json` records source custody and whether each item is an exact copy or a curated publication-facing file.

## Scope ceiling

Not established here: universal estimator failure, map-class misspecification, arbitrary-time autonomy, Markovianity or non-Markovianity, hidden memory, semigroup structure, cross-N persistence, continuum physics, geometry, gravity, or quantum gravity.
