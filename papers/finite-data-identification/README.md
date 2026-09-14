# Finite-Data Non-Identification of Effective Quantum Coarse Dynamics

Paper ID: `PAPER-BCRD-FINITE-DATA-IDENTIFICATION-001`

Formal author name: **Tobias Croydon-McRae**

## Frozen lineage

```text
scientific cutoff PR #223:
0a598dceefff780ccb1e1a25caceda4d30643997

frozen manuscript PR #251:
3433b889a301beb41a55a694337fb75f9b9994f6

governing hostile manuscript review PR #253:
846267c2abb15c8e659aeeec08efc2ed4dd9ce58
```

Current revision branch:

```text
sol/revise-paper-finite-data-identification-after-review-2026-09-14
```

This branch is a bounded publication revision. **No new physics, transition opening, map optimization, lower-bound search, K>6 execution, N10/N12 import, or later BCRD scientific result is authorized.**

## Publication-safe contribution

The four-transition data do not uniquely identify a tolerance-feasible physical map. The K=4 feasible set contains at least two distinct admissible maps with sharply different certified errors on the later prospective transitions. The exact frozen `Phi_4` fails both prospective tests, while the unchanged full physical map class remains feasible after those transitions are added as constraints.

The accepted six-transition bracket is

```text
0.002306082156934015...
<= epsilon_*^(6)
<= 0.004582638648933954...
< 0.01.
```

Primary terminology: **finite-data non-identification** / **set-membership ambiguity**.

## Literature positioning

The revision now directly engages incomplete quantum process tomography (Ziman 2008; Teo et al. 2011) and the classical set-membership identification literature (Milanese & Novara 2004, 2011). The generic phenomenon of non-unique compatible model sets under incomplete/finite data is prior art. The BCRD contribution is the frozen, custody-preserved finite case and its certified prospective/refit sequence.

## Reproducibility

`reproducibility/` is a curated publication-ready packet containing the exact `Phi_4` and `Phi_6` map artifacts, reviewed machine outputs, transition metadata, class definition, authority manifest, SHA-256 checksums, and a mechanical packaging verifier.

The packet is **prepared but not promoted** to a public repository in this lane.

## Build

Run from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

(If a system's `bibtex` alternative is unavailable, invoke its TeX Live BibTeX binary directly.)

The post-review build gate and page inspection are recorded in `BUILD-REPORT-AFTER-HR-253.md`.

## Firewalls

The paper does not claim universal estimator failure, map-class misspecification, arbitrary-time autonomy, semigroup structure, Markovianity/non-Markovianity, hidden memory, cross-N persistence, continuum physics, geometry, gravity, or quantum gravity.

The N=4 coherent-Racah lane was not inspected.
