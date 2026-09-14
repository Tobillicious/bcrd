# Public Promotion Crosswalk

Promotion ID: `PUB-PROMOTE-FDI-PAPER-001`

This crosswalk records the superseding custody state after exact binary transport remediation. PR #1 and `PROMOTION-RESULT.json` remain the historical incomplete record; they are not rewritten.

| Public path | Classification | Authority / note |
|---|---|---|
| `papers/finite-data-identification/PROMOTION-CUSTODY.md` | `PUBLIC_CUSTODY_METADATA_HISTORICAL` | Original promotion contract committed alone first at `ce4dc503a0ed67813792b3caf4a8453f4a5e8918` |
| `papers/finite-data-identification/PROMOTION-RESULT.json` | `PUBLIC_CUSTODY_METADATA_HISTORICAL` | Historical PR #1 incomplete-custody terminal record; unchanged |
| `papers/finite-data-identification/AUTHORITIES.md` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA matches frozen manuscript authority |
| `papers/finite-data-identification/BUILD-REPORT-AFTER-HR-253.md` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA matches frozen manuscript authority |
| `papers/finite-data-identification/CLAIMS.md` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA matches frozen manuscript authority |
| `papers/finite-data-identification/LITERATURE-NOTES.md` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA matches frozen manuscript authority |
| `papers/finite-data-identification/REVISION-AFTER-HR-253.md` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA matches frozen manuscript authority |
| `papers/finite-data-identification/main.tex` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA `c358a946f098708b6f65da0275697970b34dda71` |
| `papers/finite-data-identification/references.bib` | `EXACT_BYTE_COPY_FROM_MANUSCRIPT_SHA` | Git blob SHA `9f78bda5e2234eccc525ef0eaa2830da0601684d` |
| `papers/finite-data-identification/appendices/` | `EXACT_TREE_COPY_FROM_MANUSCRIPT_SHA` | Tree SHA `5b397bbe6de81f7b70ba4465d3dc278e1e7f5874` |
| `papers/finite-data-identification/figures/` | `EXACT_TREE_COPY_FROM_MANUSCRIPT_SHA` | Tree SHA `2f04dbfd106ce9b3a9dc476b82538dc7f226e3d8` |
| `papers/finite-data-identification/sections/` | `EXACT_TREE_COPY_FROM_MANUSCRIPT_SHA` | Tree SHA `4d3f0be39ec2c039b9ee49807e212c6e64f6a6e9` |
| `papers/finite-data-identification/README.md` | `PUBLIC_LANDING_METADATA_UPDATED_AFTER_EXACT_COPY_VERIFICATION` | Exact frozen README was present at remediation SHA, then only public custody/status metadata was updated; scientific contribution/firewalls retained |
| `papers/finite-data-identification/reproducibility/` | `EXACT_TREE_COPY_FROM_PUBLIC_PACKET_SHA` | 29-file recursive tree SHA `ff41547263ed9356a55d7cdc28f5cdbcfdb8da39`; includes all six exact NPZ blobs |
| `papers/finite-data-identification/PROVENANCE.md` | `PUBLIC_CUSTODY_METADATA_UPDATED` | Records historical incomplete attempt and exact binary remediation |
| `papers/finite-data-identification/PUBLIC-MANIFEST.json` | `PUBLIC_CUSTODY_METADATA_UPDATED` | Machine-readable complete-custody manifest |
| `papers/finite-data-identification/PUBLIC-CROSSWALK.md` | `PUBLIC_CUSTODY_METADATA_UPDATED` | This file |
| `papers/finite-data-identification/PROMOTION-RESULT-SUPERSEDING.json` | `PUBLIC_CUSTODY_METADATA_NEW` | Superseding final custody result, committed after metadata verification |
| `README.md` | `PUBLIC_LANDING_METADATA_UPDATED` | Narrow paper title/status correction only |
| `CITATION.cff` | `UNCHANGED` | Root citation metadata deliberately not modified |

The frozen manuscript authority contains 22 non-reproducibility files. All 22 were byte-identical at remediation SHA `eeb07cc701775cf7d2feda9b606d3ba618c83a09`; only the paper README was subsequently adapted as explicitly authorized public landing metadata. All scientific TeX, appendices, figures, literature/bibliography, claims/authority ledgers, and build/revision records remain byte-identical to the frozen manuscript authority.

The complete reproducibility subtree is unchanged after remediation and is Git-tree-identical to frozen packet authority `0155ec7f1c765b41737322837f3266337626c201`. No `PORTING`, `REGENERATION`, `NORMALIZATION`, binary rewrite, scientific edit, or reproducibility semantic change was performed.
