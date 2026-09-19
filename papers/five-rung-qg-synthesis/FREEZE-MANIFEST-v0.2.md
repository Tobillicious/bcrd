# BCRD five-rung QG synthesis v0.2 — freeze manifest

Date: 2026-09-20
Repository: Tobillicious/physics-lane
Branch: `sol/bcrd-five-rung-qg-paper-finalize-2026-09-20`

## Scientific provenance

- Fail-closed post-review scientific base: `4071f4f7df1ed5526e83f323a3bf301683144c22`
- Inherited staging head used for takeover: `4eaf155aae10398139673f4fff9fc59a6377c137`
- Completed source commit: `30d8f7bef45b212dd4db0c16c89677c0623b6f08`
- Post-completion editorial commits (no science change): `750a8d6a15` (traceability
  footnote, Definition label, patchwise Rung IV wording, W2asym exact commit),
  `834d271248` (exact C4/C8 evidence footnote at `3cd7f316`), `d3d1b0891c`
  (compact provenance note), `2a0c07250b` (`\enlargethispage` pagination repair)
- Superseded pre-`4071f4f` paper state is not authority for this revision.

## Exact source artifact

Path: `publications/papers/bcrd-five-rung-qg-synthesis/main.tex`

SHA-256:
`7e332b654fe33b32085ec75e8e765641f6afe71fb04cb58c0b4d0ba5fa501661`

## Exact compiled PDF artifact

Filename: `main.pdf` (committed natively in this revision)

SHA-256:
`d5cc8addca84d0be30f455025bf8e1d2cea1c82cdaf071f30fa9bef9b6f38a5f`

Size: 411032 bytes
Pages: 10

The exact PDF above was built from the source above with three successful
`pdflatex` passes in an isolated local worktree (pdfTeX 3.141592653-2.6-1.40.29,
TeX Live 2026basic + genuine CTAN `authblk.sty` v1.3 via TEXINPUTS; no system
tree modified). Full verification record: `BUILD-REPORT-v0.2.txt` in the same
directory. The earlier author-side compiled hash
`c0cf0cf3d270d21293a4725b00bb968e84a78d6fae7bb7ceab06bfa82f6f55b1`
(338604 bytes, untransferable by the authoring connector) is superseded as the
frozen artifact and retained only for traceability; scientific content is
unchanged and only the bound PDF bytes differ by toolchain.

## Build recipe

From `publications/papers/bcrd-five-rung-qg-synthesis/`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
sha256sum main.tex main.pdf
```

Final build diagnostics (local native build, see `BUILD-REPORT-v0.2.txt`):
- no TeX fatal errors (all three passes exit 0);
- no undefined citations;
- no undefined references;
- no overfull boxes;
- three cosmetic underfull-box warnings only (footnote/compressed provenance
  paragraph; non-blocking, no text loss);
- 10-page A4 PDF; pdftotext clean (no replacement glyphs); all word boxes
  within media box on all 10 pages.

## Scope contract frozen in the manuscript

The paper explicitly states:
- Riemannian/Euclidean signature only for the five-rung theorem;
- coherent, nondegenerate boundary data;
- admissible large-spin sequences;
- near-flat / fluctuation-ball / selected-local-branch / quadratic scope;
- Hypothesis N removed as a load-bearing dependency;
- Conjecture-eig remains open;
- no BCRD graviton propagator or pole is claimed;
- no finite-spin four-dimensional metricity claim is made for arbitrary tetrahedral data;
- no universal finiteness claim is made;
- generalized dagger-dipole divergence is separated from strict simplicial finiteness;
- strict-simplicial `S^4` divergence is only `CANDIDATE DIVERGENCE`;
- Lorentzian implementation checks are consistency checks, not a Lorentzian completion of the theorem.

## Takeover edits relative to the four staged source chunks

The completion:
1. repaired the malformed `remark` theorem declaration;
2. completed the source where chunk 4 ended mid-sentence in the Lorentzian-status section;
3. added explicit limitations/open-problems and conclusion sections;
4. closed the bibliography and citation keys;
5. added reproducibility/provenance and AI-assistance disclosure;
6. preserved the fail-closed scope and did not promote any open candidate to theorem status.

No new load-bearing physics calculation was introduced by these editorial/provenance repairs.
