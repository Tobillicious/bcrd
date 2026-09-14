# PAPER-BCRD-KNOWN-SPIN-ERASURE-001

## Reconciled title

**Exact Reconstructive Autonomous Closure in Finite Singlet Quantum Systems**

Status: **published preprint**.

## Publication

**Figshare DOI:** https://doi.org/10.6084/m9.figshare.33730069  
**Author:** Tobias Croydon-McRae  
**Licence:** CC BY 4.0  
**Published:** 2026-09-14

The published Figshare item contains the certified 19-page PDF and a frozen 25-file source archive.

```text
certified_pdf_sha256 =
12fdfc5eb1f76fd6374c9de3096c4d32e8d22812821b93659351002e506017a7

source_archive_sha256 =
e12f28d6f57ef57770a4281364c202c3327869783facc495c282b473c174c7fa
```

Final publication-readiness closure:

```text
build certificate commit =
1af614a7f06b186ce3f7a4cbad3e38a230906db8

publication-readiness PR =
#268

publication-readiness terminal SHA =
342ca267c21a98d428ce90847296892898c065cb

final disposition =
MANUSCRIPT_READY_FOR_PUBLIC_PROMOTION
```

This lane performs no new physics, new theorem, or new literature search.

## Publication centre

One-particle-loss immunity and its syndrome-factor structure are established QEC/DFS results. The present finite BCRD application places that reversible structure in a common record-dynamics formulation and uses it to interpret the reviewed `J2/J4/J6` records at `N=8,10,12` as exact reconstructive autonomous closure.

```text
EXACT_RECONSTRUCTIVE_AUTONOMOUS_CLOSURE
!=
AUTONOMOUS_CLOSURE_AFTER_GENUINE_INFORMATION_LOSS
```

## Settled contribution audit

```text
A_Wi_factorization = DIRECT_PRIOR_ART
B_full_algebra_recovery = STANDARD_COROLLARY_OR_REFORMULATION
C_recoverability_to_autonomy = STANDARD_COROLLARY_OR_REFORMULATION
D_reconstructive_vs_lossy = DISTINCT_SYNTHESIS_OR_APPLICATION
E_BCRD_finite_application = DISTINCT_SYNTHESIS_OR_APPLICATION
```

No priority adjective is attached to A–E.

## Scope controls

The general even-`N` singlet/DFS recovery structure remains general where supported. The BCRD realization remains finite at `N=8,10,12`. No strict minimality, minimum-support growth, common cross-`N` map, arbitrary-`N` BCRD theorem, genuinely lossy autonomous closure, semigroup/Markovianity, thermodynamic irreversibility, continuum, geometry, gravity, or quantum gravity is claimed.

## Reconciliation authorities

- PR #254 hostile review: `7622473f21276f014224954a21ae8f26b22a2fbf`
- PR #256 manuscript base: `78584848a1051f8eb963ddbc1dd7f2bb1a42def0`
- PR #258 novelty authority: `9d67e480ea2278ad8781a269e39e904c41fe9a3d`

See `reconciliation/` for the contract, authority crosswalk, novelty classification, scope audit, wording audit, contribution statement, and publication-readiness gate.

## Build

The manuscript uses conventional BibTeX:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The exact reconciled source was subsequently subjected to the required clean build and all-page render inspection. The custody build certificate is directly parented by the frozen manuscript head and records LaTeX/BibTeX PASS, zero undefined references or citations, zero overfull boxes, two nonmaterial underfull boxes, and successful inspection of all 19 pages. Final publication-readiness closure PR #268 assigned `MANUSCRIPT_READY_FOR_PUBLIC_PROMOTION` without modifying scientific manuscript content.
