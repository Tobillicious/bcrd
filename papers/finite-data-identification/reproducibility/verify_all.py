#!/usr/bin/env python3
"""One-command verifier for PUB-REPRO-FDI-PAPER-001.

Normal mode always executes the five load-bearing calculations. A separate,
explicit mutation-fixture mode exists only so the mutation harness can test the
verifier's failure sensitivity without repeating the expensive scientific
recomputation four extra times; normal verification cannot use that mode.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "PUBLIC-REPRODUCTION-RESULTS.json"
EXPECTED_ORDER = ["TRAIN0", "TRAIN1", "H1", "H2", "F1", "F2"]
EXPECTED_ROWS = [
    {"label":"TRAIN0","current_time":"0.832388182473","next_time":"0.9323881824729999"},
    {"label":"TRAIN1","current_time":"0.9323881824729999","next_time":"1.032388182473"},
    {"label":"H1","current_time":"1.232388182473","next_time":"1.332388182473"},
    {"label":"H2","current_time":"1.382388182473","next_time":"1.482388182473"},
    {"label":"F1","current_time":"24.232388182473","next_time":"24.332388182473"},
    {"label":"F2","current_time":"24.532388182473","next_time":"24.632388182473"},
]


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''):
            h.update(c)
    return h.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data=path.read_bytes()
    h=hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode())
    h.update(data)
    return h.hexdigest()


def run_packaging_verifier(root: Path) -> None:
    p=subprocess.run([sys.executable, str(root/'verification/verify_packet.py')], cwd=root,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode:
        raise RuntimeError("existing packaging verifier failed:\n"+p.stdout)


def validate_static(root: Path) -> dict:
    run_packaging_verifier(root)
    custody=json.loads((root/'inputs/custody.json').read_text())
    custody_results={}
    for rel,meta in custody['files'].items():
        p=root/rel
        if not p.is_file():
            raise RuntimeError(f"missing frozen input: {rel}")
        got_blob=git_blob_sha1(p)
        if got_blob != meta['git_blob_sha1']:
            raise RuntimeError(f"Git-blob custody mismatch for {rel}: {got_blob}")
        got_sha=sha256(p)
        want_sha=meta.get('sha256')
        if want_sha is not None and got_sha != want_sha:
            raise RuntimeError(f"SHA256 custody mismatch for {rel}: {got_sha}")
        custody_results[rel]={"git_blob_sha1":got_blob,"sha256":got_sha,"pass":True}

    td=json.loads((root/'inputs/transitions.json').read_text())
    if td.get('order') != EXPECTED_ORDER or td.get('transitions') != EXPECTED_ROWS:
        raise RuntimeError("transition definition/order custody failure")

    pc=json.loads((root/'inputs/physical-map-class.json').read_text())
    required={
      'class_id':'FULL_PHYSICAL_SOURCE_INDEPENDENT_TIME_INDEPENDENT_WHOLE_ALGEBRA_CPTP',
      'N':8,'record':'R2_07','source_dimension':2,'whole_algebra':True,'CPTP':True,
      'source_independent':True,'time_independent':True,'same_map_all_transitions':True,
      'central_transfers_allowed':49,
      'sector_n':[2,2,1,2,1,2,1], 'sector_m':[1,1,1,1,1,2,2],
      'ambient_dimensions':[64,64,32,64,32,64,32],
      'map_scaling':{'numerator':1048577,'denominator':1048576},
      'physical_epsilon':{'numerator':1,'denominator':100},
    }
    for k,v in required.items():
        if pc.get(k) != v:
            raise RuntimeError(f"physical-map-class custody failure at {k}")
    return {"custody":custody_results,"transition_definition_verified":True,"physical_map_class_verified":True}


def load_recompute_module(root: Path):
    path=root/'scripts/recompute_certificates.py'
    spec=importlib.util.spec_from_file_location('pub_repro_fdi_recompute',path)
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def compare_targets(root: Path, calculated: dict) -> dict:
    expected=json.loads((root/'expected/frozen_certificate_targets.json').read_text())['targets']
    checks={}
    for key,meta in expected.items():
        if key not in calculated:
            raise RuntimeError(f"calculation missing target {key}")
        got=F(calculated[key]['exact'])
        want=F(meta['expected_exact'])
        tol=F(meta['tolerance_for_reproduction_comparison'])
        dev=abs(got-want)
        ok=dev <= tol
        checks[key]={
            'certificate_type':meta['certificate_type'],
            'authority_sha':meta['authority_sha'],
            'expected_exact':str(want), 'observed_exact':str(got),
            'absolute_deviation_exact':str(dev), 'tolerance_exact':str(tol),
            'exact_equal':got==want, 'pass':ok,
        }
        if not ok:
            raise RuntimeError(f"{key} reproduction mismatch: deviation {dev} > {tol}")
    return checks


def fixture_values(path: Path) -> dict:
    d=json.loads(path.read_text())
    if not d.get('load_bearing_calculations_actually_executed'):
        raise RuntimeError('mutation fixture does not attest actual canonical execution')
    return d['calculated_values']


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--mutation-fixture', type=Path, default=None,
                    help='MUTATION HARNESS ONLY: reuse values from a prior actual canonical execution')
    args=ap.parse_args()
    mutation_mode=args.mutation_fixture is not None
    if mutation_mode and __import__('os').environ.get('PUB_REPRO_MUTATION_TEST') != '1':
        raise SystemExit('--mutation-fixture is forbidden outside PUB_REPRO_MUTATION_TEST=1')

    started=time.monotonic()
    static=validate_static(ROOT)
    if mutation_mode:
        calculated=fixture_values(args.mutation_fixture)
        details={'mutation_fixture_only':True,'load_bearing_calculations_actually_executed':False}
    else:
        mod=load_recompute_module(ROOT)
        details=mod.compute_all()
        if not details.get('load_bearing_calculations_actually_executed'):
            raise RuntimeError('recomputation module did not execute load-bearing calculations')
        calculated=details['values']
    target_checks=compare_targets(ROOT, calculated)

    out={
      'packet_version':'PUB-REPRO-FDI-PAPER-001-v1',
      'target_manuscript_SHA':'53e365b6c947d5abd672c9b02f905e0175d6176a',
      'scientific_cutoff_SHA':'0a598dceefff780ccb1e1a25caceda4d30643997',
      'Phi4_hash_verified':static['custody']['maps/Phi4-candidate-map-dyadic.npz']['pass'],
      'Phi6_hash_verified':static['custody']['maps/Phi6-C-S2-frob-pr213.npz']['pass'],
      'transition_definition_verified':static['transition_definition_verified'],
      'physical_map_class_verified':static['physical_map_class_verified'],
      'U4_reproduced':target_checks['U4']['pass'],
      'Phi4_F1_lower_reproduced':target_checks['PHI4_F1_LOWER']['pass'],
      'Phi4_F2_lower_reproduced':target_checks['PHI4_F2_LOWER']['pass'],
      'K6_constructive_upper_reproduced':target_checks['K6_CONSTRUCTIVE_UPPER']['pass'],
      'L6_reproduced':target_checks['L6']['pass'],
      'all_load_bearing_certificates_reproduced':all(x['pass'] for x in target_checks.values()),
      'private_repo_archaeology_required':False,
      'load_bearing_calculations_actually_executed':bool(not mutation_mode and details.get('load_bearing_calculations_actually_executed')),
      'mutation_fixture_mode':mutation_mode,
      'calculated_values':calculated,
      'target_checks':target_checks,
      'packet_custody':static['custody'],
      'recomputation_detail':details,
      'seconds':time.monotonic()-started,
    }
    out['public_reproduction_disposition'] = ('PASS' if out['all_load_bearing_certificates_reproduced'] and
        (out['load_bearing_calculations_actually_executed'] or mutation_mode) else 'FAIL')
    if not mutation_mode:
        RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['public_reproduction_disposition']=='PASS' else 1


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"PUBLIC_REPRODUCTION_VERIFY_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
