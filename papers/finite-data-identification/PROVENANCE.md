# Public Promotion Provenance

paper title = Finite-Data Non-Identification of Effective Quantum Coarse Dynamics

author = Tobias Croydon-McRae

private manuscript SHA = 53e365b6c947d5abd672c9b02f905e0175d6176a

scientific cutoff SHA = 0a598dceefff780ccb1e1a25caceda4d30643997

hostile publication review terminal SHA = 846267c2abb15c8e659aeeec08efc2ed4dd9ce58

repair terminal SHA = f8ff6d96ca51071c52b1cdb754bc2c3c55b2d981

readiness terminal SHA = 2c026ed1321bbb782667665ec9c7b19ce7cca2ef

frozen public packet SHA = 0155ec7f1c765b41737322837f3266337626c201

canonical Actions run = 34818555115

clean Actions run = 34820170490

final private readiness disposition = MANUSCRIPT_READY_FOR_PUBLIC_PROMOTION

NO scientific edits during promotion

NO manuscript scientific-content edits during promotion

NO reproducibility semantic changes during promotion

NO DOI minted during promotion

NO GitHub Release created during promotion

NO Figshare action during promotion

## Historical incomplete custody attempt

```text
prior_incomplete_PR = 1
prior_incomplete_terminal_SHA = 88f3706ae0972a9040f5ca8fbf42bf15a19de44f
prior_incomplete_disposition = PUBLIC_PROMOTION_CUSTODY_INCOMPLETE
```

PR #1 remains the historical record of the first custody attempt. Its blocker was limited to transport of six NPZ binary artifacts through the connected GitHub interface. That historical result is not rewritten or erased.

## Binary transport remediation

```text
binary_transport_remediation_branch = publication/resolve-fdi-binary-custody-2026-09-14
binary_transport_remediation_SHA = eeb07cc701775cf7d2feda9b606d3ba618c83a09
binary_transport_remediation_parent = 88f3706ae0972a9040f5ca8fbf42bf15a19de44f
```

The remediation commit transferred the frozen manuscript source and frozen executable reproducibility packet by exact local Git custody transfer.

Mechanical verification after the pushed remediation established:

- every manuscript blob/subtree outside `reproducibility/` matched the frozen manuscript authority by Git object SHA before the public landing-metadata update;
- the promoted `reproducibility/` tree SHA is `ff41547263ed9356a55d7cdc28f5cdbcfdb8da39`, exactly equal to the frozen packet authority tree SHA;
- the reproducibility tree contains 29 files, including six NPZ Git blobs;
- the remediation commit is one commit directly above the historical incomplete terminal;
- the remediation diff introduced no path outside `papers/finite-data-identification/` and no deletions;
- no private development subtree, private absolute path, credential, or secret was promoted;
- no scientific manuscript content or reproducibility semantics were changed.

The public paper README and repository-root README were subsequently updated only as public landing/status metadata. Root `CITATION.cff` was not modified.

## Current custody status

The prior binary transport defect is resolved. The exact scientific/manuscript payload and exact executable packet are present in the public promotion branch, with public-only metadata layered around them. Paper DOI assignment, GitHub Release creation, Figshare action, and merging remain outside this custody lane.
