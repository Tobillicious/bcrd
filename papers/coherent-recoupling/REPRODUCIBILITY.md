# Reproducibility and release custody

Status: **STAGING TEMPLATE — NO RELEASE ACTION AUTHORIZED**

This document defines the mechanical custody path for `PAPER-BCRD-COHERENT-RECOUPLING-001`. It does not authorize physics execution, publication, DOI creation, or archival deposition.

## 1. Reproducibility principle

A public release is valid only if a third party can identify exactly:

1. the frozen scientific authorities;
2. the frozen manuscript source commit;
3. the exact public-repository target commit and frozen non-moving release tag by project policy;
4. the exact files deposited in the archive;
5. the SHA-256 of every deposited artifact;
6. the archive DOI that resolves to those exact artifacts; and
7. the metadata-only GitHub commit that records the DOI without changing the frozen target.

No result may be reconstructed from conversation history, private-machine paths, or undocumented repository archaeology when a public reproducibility artifact is required.

A release tag is treated as non-moving by project policy. This document does **not** claim that repository technology or rulesets independently prevent tag mutation unless such protection is separately verified.

## 2. Required final provenance chain

The non-circular release chain is:

```text
final scientific authority
  -> [V3-PENDING: final reconciled V3 scientific authority]
  -> [V3-PENDING: frozen final manuscript source SHA in physics-lane]
  -> exact-copy verification
  -> [V3-PENDING: frozen public target commit A in Tobillicious/bcrd]
  -> frozen non-moving release tag by project policy:
     paper/coherent-recoupling/vMAJOR.MINOR.PATCH -> commit A
  -> archive deposit containing bytes from commit A
  -> [V3-PENDING: archive DOI D]
  -> metadata-only GitHub commit B records DOI D + points back to commit A/tag
```

**Commit A is the scientific/reproducibility target. Commit B is only the DOI backlink.** The DOI backlink must never rewrite, retag, or replace commit A. The project release tag remains on commit A by custody policy.

## 3. Exact-copy verification procedure

Run in clean clones with `core.autocrlf=false`.

### A. Freeze the source authority

Record:

```text
SOURCE_REPO=Tobillicious/physics-lane
SOURCE_SHA=[V3-PENDING: frozen final manuscript source SHA]
SOURCE_PATH=[V3-PENDING: final manuscript/reproducibility source path]
```

The source SHA must be a full 40-character commit ID. Do not use a moving branch name as authority.

### B. Export exact Git objects

Preferred method for a complete source subtree:

```bash
git -c core.autocrlf=false archive --format=tar "$SOURCE_SHA" -- "$SOURCE_PATH" > /tmp/bcrd-source.tar
mkdir -p /tmp/bcrd-source
cd /tmp/bcrd-source
tar -xf /tmp/bcrd-source.tar
```

For an individual file, compare its Git blob identity first:

```bash
git ls-tree "$SOURCE_SHA" -- "$SOURCE_PATH/path/to/file"
```

Record the blob SHA in the transfer ledger. Binary files must be copied byte-for-byte; never reserialize NPZ, PDF, PNG, JSON, or other binary/structured artifacts merely to move them.

### C. Compare source and public copies

For every custody-copied file, compute SHA-256 on both sides. The file passes only when the two SHA-256 values are identical.

For text trees, a zero `git diff --no-index --binary` is a useful secondary check, but **SHA-256 equality is the normative byte-level criterion**.

### D. Freeze the public target

After all final files and manifests are present, record the full commit SHA as:

```text
PUBLIC_FROZEN_TARGET_SHA=[V3-PENDING: exact bcrd commit A]
```

No scientific, manuscript, figure, data, code, or reproducibility file may change after this point. Any such change requires a new commit, a new manifest, and—if already released—a new version tag/archive version.

## 4. Canonical SHA-256 manifest generation

The canonical procedure is Python 3 so it behaves consistently on macOS and Linux. Run from the release root that will be archived. Exclude `.git`, transient build products, and the checksum file itself unless the release specification explicitly includes them.

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib

root = Path('.')
out = root / 'ARTIFACT-MANIFEST.sha256'
exclude = {
    '.git',
    'ARTIFACT-MANIFEST.sha256',
}

files = []
for p in root.rglob('*'):
    if not p.is_file():
        continue
    rel = p.relative_to(root)
    if any(part == '.git' for part in rel.parts):
        continue
    if rel.as_posix() in exclude:
        continue
    files.append(rel)

with out.open('w', encoding='utf-8', newline='\n') as f:
    for rel in sorted(files, key=lambda x: x.as_posix().encode('utf-8')):
        h = hashlib.sha256()
        with (root / rel).open('rb') as src:
            for chunk in iter(lambda: src.read(1024 * 1024), b''):
                h.update(chunk)
        f.write(f"{h.hexdigest()}  {rel.as_posix()}\n")
PY
```

Then record the checksum of the manifest itself separately:

```bash
shasum -a 256 ARTIFACT-MANIFEST.sha256      # macOS
# or
sha256sum ARTIFACT-MANIFEST.sha256          # GNU/Linux
```

Store that value in `PUBLICATION-RELEASE.json` only after the final manifest is frozen.

## 5. Canonical SHA-256 verification

Cross-platform Python verification:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib, sys

root = Path('.')
manifest = root / 'ARTIFACT-MANIFEST.sha256'
fail = False
for raw in manifest.read_text(encoding='utf-8').splitlines():
    if not raw.strip() or raw.lstrip().startswith('#'):
        continue
    digest, rel = raw.split('  ', 1)
    p = root / rel
    if not p.is_file():
        print(f'MISSING  {rel}')
        fail = True
        continue
    h = hashlib.sha256()
    with p.open('rb') as src:
        for chunk in iter(lambda: src.read(1024 * 1024), b''):
            h.update(chunk)
    actual = h.hexdigest()
    if actual != digest:
        print(f'FAIL     {rel}\n expected {digest}\n actual   {actual}')
        fail = True
    else:
        print(f'OK       {rel}')
sys.exit(1 if fail else 0)
PY
```

Platform-native secondary checks are acceptable:

```bash
shasum -a 256 -c ARTIFACT-MANIFEST.sha256   # macOS
sha256sum -c ARTIFACT-MANIFEST.sha256       # GNU/Linux
```

## 6. Build and render gate

Before the public target is frozen:

- compile the exact manuscript source in a clean environment;
- record toolchain versions;
- require zero fatal LaTeX errors;
- require zero undefined references and citations;
- inspect every rendered page;
- record overfull/underfull boxes and adjudicate whether any are material;
- SHA-256 the final PDF;
- verify every figure/table shown in the PDF comes from the frozen source tree;
- verify every `[V3-PENDING: ...]` and `[V3-RECONCILIATION-PENDING: ...]` token is absent from the release candidate.

Exact commands depend on the production manuscript tree and are `[V3-PENDING: final build instructions from the frozen production manuscript]`.

## 7. Archive-deposit exactness

Before upload, create a clean export from `PUBLIC_FROZEN_TARGET_SHA` rather than zipping a mutable working tree. If an archive file is used, hash that archive and record its SHA-256.

After upload but before final publication of the archive record:

1. download every uploaded file back from the archive if the platform permits a draft verification round;
2. recompute SHA-256;
3. compare against `ARTIFACT-MANIFEST.sha256`;
4. confirm the archive metadata names `PUBLIC_FROZEN_TARGET_SHA` and the frozen non-moving release tag by project policy;
5. only then finalize the archive record and accept the DOI.

If the archive service mutates uploaded bytes, do not claim byte-identical deposit; document the transformation explicitly and preserve the original exact artifact separately.

## 8. DOI backlink and GitHub custody

Once DOI `[V3-PENDING: archive DOI D]` exists, make one metadata-only commit B that may update only DOI/citation/public-README metadata. It must contain:

```text
archive_doi = D
public_frozen_target_sha = commit A
release_tag = paper/coherent-recoupling/vMAJOR.MINOR.PATCH
release_tag_policy = FROZEN_NON_MOVING_BY_PROJECT_POLICY
scientific_content_modified = NO
reproducibility_content_modified = NO
```

Do not move the tag from commit A to commit B.

## 9. Reproduction success criterion

A reproduction attempt passes release custody only when:

```text
manifest_verification = PASS
exact_copy_verification = PASS
clean_build = PASS
all_page_render_inspection = PASS
public_frozen_target_identified = YES
archive_files_match_frozen_target = YES
DOI_points_to_correct_version = YES
pending_tokens_in_release = 0
scientific_claim_audit = PASS
```

Anything weaker remains a draft or staging package.
