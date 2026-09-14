#!/usr/bin/env python3
"""Mechanical verifier for the curated publication packet.

This script performs NO physics, fitting, optimization, propagation, or certificate search.
It checks immutable object hashes and publication-summary consistency only.
"""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_MAPS = {
    "maps/Phi4-candidate-map-dyadic.npz":
        "48abd5f52812ef7503cfdde92fe630b99ded9c10c4ef35d2c4edc8d934028125",
    "maps/Phi6-C-S2-frob-pr213.npz":
        "c674e471c6bbad2e3376e53315d8e1e5cb83dbbb85f4120c7b5b8602b78f7e0a",
}
EXPECTED_TRANSITIONS = [
    ("TRAIN0","0.832388182473","0.9323881824729999"),
    ("TRAIN1","0.9323881824729999","1.032388182473"),
    ("H1","1.232388182473","1.332388182473"),
    ("H2","1.382388182473","1.482388182473"),
    ("F1","24.232388182473","24.332388182473"),
    ("F2","24.532388182473","24.632388182473"),
]

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    for rel, expected in EXPECTED_MAPS.items():
        path=ROOT/rel
        if not path.is_file():
            raise SystemExit(f"MISSING: {rel}")
        got=sha256(path)
        if got != expected:
            raise SystemExit(f"HASH FAIL: {rel}\nexpected {expected}\nobserved {got}")
        print(f"HASH PASS {rel} {got}")

    with (ROOT/"transition-dataset.csv").open(newline="") as f:
        rows=list(csv.DictReader(f))
    got=[(r["label"],r["current_time"],r["next_time"]) for r in rows]
    if got != EXPECTED_TRANSITIONS:
        raise SystemExit(f"TRANSITION DATASET FAIL: {got!r}")
    print("TRANSITION DATASET PASS")

    cert=json.loads((ROOT/"certificate-summary.json").read_text())
    assert cert["K4"]["sha256"] == EXPECTED_MAPS["maps/Phi4-candidate-map-dyadic.npz"]
    assert cert["K6"]["sha256"] == EXPECTED_MAPS["maps/Phi6-C-S2-frob-pr213.npz"]
    assert cert["prospective_Phi4"]["F1_lower"] == 0.6246936110454476
    assert cert["prospective_Phi4"]["F2_lower"] == 0.6217658417777687
    assert cert["K6"]["universal_lower"] == 0.002306082156934015
    assert cert["K6"]["existence_upper"] == 0.004582638648933954
    assert cert["physical_setting"]["epsilon"] == 0.01
    print("CERTIFICATE SUMMARY CONSTANTS PASS")

    print("PACKET_MECHANICAL_VERIFICATION = PASS")
    print("NEW_PHYSICS_PERFORMED = NO")

if __name__ == "__main__":
    main()
