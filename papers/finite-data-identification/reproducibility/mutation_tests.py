#!/usr/bin/env python3
"""Failure-sensitivity tests for PUB-REPRO-FDI-PAPER-001 verifier.

Requires a canonical PUBLIC-REPRODUCTION-RESULTS.json produced by a normal run.
Mutated copies use explicit mutation-fixture mode so expensive scientific work is
not rerun; the fixture must itself attest an actual canonical execution.
"""
from __future__ import annotations
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BASELINE=ROOT/'PUBLIC-REPRODUCTION-RESULTS.json'


def run_case(name, mutate):
    with tempfile.TemporaryDirectory(prefix='pub-repro-mutation-') as td:
        dst=Path(td)/'packet'
        shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('PUBLIC-REPRODUCTION-RESULTS.json','__pycache__'))
        fixture=Path(td)/'baseline.json'
        shutil.copy2(BASELINE,fixture)
        mutate(dst)
        env=os.environ.copy(); env['PUB_REPRO_MUTATION_TEST']='1'
        p=subprocess.run([sys.executable,str(dst/'verify_all.py'),'--mutation-fixture',str(fixture)],cwd=dst,env=env,
                         stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        return {'name':name,'detected':p.returncode!=0,'returncode':p.returncode,'tail':p.stdout[-2000:]}


def corrupt_phi4(root):
    p=root/'maps/Phi4-candidate-map-dyadic.npz'
    b=bytearray(p.read_bytes()); b[len(b)//2] ^= 1; p.write_bytes(b)

def perturb_expected(root):
    p=root/'expected/frozen_certificate_targets.json'; d=json.loads(p.read_text())
    d['targets']['U4']['expected_exact']='1/2'; p.write_text(json.dumps(d,indent=2)+'\n')

def reorder_f1_f2(root):
    p=root/'inputs/transitions.json'; d=json.loads(p.read_text())
    d['order'][-2:]=['F2','F1']; d['transitions'][-2:]=[d['transitions'][-1],d['transitions'][-2]]
    p.write_text(json.dumps(d,indent=2)+'\n')

def alter_class(root):
    p=root/'inputs/physical-map-class.json'; d=json.loads(p.read_text())
    d['central_transfers_allowed']=48; p.write_text(json.dumps(d,indent=2)+'\n')


def main():
    if not BASELINE.is_file():
        raise SystemExit('run python verify_all.py successfully before mutation tests')
    b=json.loads(BASELINE.read_text())
    if not b.get('load_bearing_calculations_actually_executed') or b.get('public_reproduction_disposition')!='PASS':
        raise SystemExit('baseline is not a successful actual-execution result')
    cases=[run_case('corrupt_Phi4_hash',corrupt_phi4),run_case('perturb_expected_certificate_target',perturb_expected),
           run_case('reorder_F1_F2',reorder_f1_f2),run_case('alter_physical_class_parameter',alter_class)]
    out={'mutation_tests':cases,'all_mutations_detected':all(x['detected'] for x in cases)}
    (ROOT/'MUTATION-TEST-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    return 0 if out['all_mutations_detected'] else 1

if __name__=='__main__': raise SystemExit(main())
