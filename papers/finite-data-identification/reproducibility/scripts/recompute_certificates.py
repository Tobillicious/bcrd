#!/usr/bin/env python3
"""Public mechanical reproduction of the five frozen FDI-paper certificates.

Publication-reproducibility only. No optimisation, fitting, refitting, search, or
new scientific evidence is performed. The calculations are minimal ports of the
frozen reviewed certificate implementations identified in the provenance ledger.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import time
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_k, "1")

import numpy as np

PACKET = Path(__file__).resolve().parents[1]
INPUTS = PACKET / "inputs"
MAPS = PACKET / "maps"

B = 1 << 40
CNUM = (1 << 20) + 1
CDEN = 1 << 20
C_SCALE = F(CNUM, CDEN)
EPS = F(1, 100)
NS = (2, 2, 1, 2, 1, 2, 1)
MS = (1, 1, 1, 1, 1, 2, 2)
T0 = 0.832388182473
HIST_TIMES = tuple(T0 + x for x in (0.0, 0.1, 0.2, 0.4, 0.5, 0.55, 0.65))
FWD_TIMES = tuple(float(x) for x in ("24.232388182473", "24.332388182473", "24.532388182473", "24.632388182473"))
TIMES = HIST_TIMES + FWD_TIMES
TRANSITIONS = (
    ("TRAIN0", 0, 1, F(26, 25), 64),
    ("TRAIN1", 1, 2, F(26, 25), 64),
    ("H1", 3, 4, F(3331, 2500), 64),
    ("H2", 5, 6, F(1853, 1250), 64),
    ("F1", 7, 8, F(60831, 2500), 1536),
    ("F2", 9, 10, F(61581, 2500), 1536),
)
EXPECTED_CHANNEL_DIGEST = "9d8afea27ddb3582ab9aaecbf3c3614bba23a04ef45b16f3cc9c9b0748641331"
SPECTRAL_BITS = 52  # frozen PR #223 reviewer route
L6_BITS = 60       # frozen PR #222 exact integer lower route


# ---------------------------------------------------------------------------
# basic custody helpers
# ---------------------------------------------------------------------------



def consume_machine_definitions():
    transitions = json.loads((INPUTS / "transitions.json").read_text())
    expected_rows = [
        {"label": "TRAIN0", "current_time": "0.832388182473", "next_time": "0.9323881824729999"},
        {"label": "TRAIN1", "current_time": "0.9323881824729999", "next_time": "1.032388182473"},
        {"label": "H1", "current_time": "1.232388182473", "next_time": "1.332388182473"},
        {"label": "H2", "current_time": "1.382388182473", "next_time": "1.482388182473"},
        {"label": "F1", "current_time": "24.232388182473", "next_time": "24.332388182473"},
        {"label": "F2", "current_time": "24.532388182473", "next_time": "24.632388182473"},
    ]
    if transitions.get("transitions") != expected_rows:
        raise RuntimeError("machine transition definition differs from frozen canonical order/values")
    pc = json.loads((INPUTS / "physical-map-class.json").read_text())
    required = {
        "class_id": "FULL_PHYSICAL_SOURCE_INDEPENDENT_TIME_INDEPENDENT_WHOLE_ALGEBRA_CPTP",
        "N": 8, "record": "R2_07", "source_dimension": 2,
        "whole_algebra": True, "CPTP": True, "source_independent": True,
        "time_independent": True, "same_map_all_transitions": True,
        "central_transfers_allowed": 49,
        "sector_n": list(NS), "sector_m": list(MS),
        "ambient_dimensions": [32*n for n in NS],
        "map_scaling": {"numerator": CNUM, "denominator": CDEN},
        "physical_epsilon": {"numerator": 1, "denominator": 100},
    }
    for k, v in required.items():
        if pc.get(k) != v:
            raise RuntimeError(f"physical map class custody mismatch at {k}: {pc.get(k)!r}")
    return transitions, pc

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    h = hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode())
    h.update(data)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# exact complex dyadic arithmetic (mechanically identical core semantics)
# ---------------------------------------------------------------------------

def as_obj_int(a):
    a = np.asarray(a)
    return np.array([int(x) for x in a.reshape(-1)], dtype=object).reshape(a.shape)


def unpack(re, im, e=40):
    return as_obj_int(re), as_obj_int(im), int(e)


def adj(x):
    return x[0].T, -x[1].T, x[2]


def add(x, y):
    a, b, e = x
    c, d, f = y
    g = max(e, f)
    return (a * (1 << (g - e)) + c * (1 << (g - f)),
            b * (1 << (g - e)) + d * (1 << (g - f)), g)


def neg(x):
    return -x[0], -x[1], x[2]


def conj(x):
    return x[0], -x[1], x[2]


def mm(x, y):
    a, b, e = x
    c, d, f = y
    return a @ c - b @ d, a @ d + b @ c, e + f


def zero(n, m=None, e=0):
    if m is None:
        m = n
    return np.zeros((n, m), dtype=object), np.zeros((n, m), dtype=object), e


def op_bound(re, im, den):
    v = np.abs(re) + np.abs(im)
    one = max(int(x) for x in np.sum(v, axis=0))
    infn = max(int(x) for x in np.sum(v, axis=1))
    return F(max(one, infn), int(den))


def gram_defect(x):
    g = mm(adj(x), x)
    re = g[0].copy()
    for i in range(re.shape[0]):
        re[i, i] -= 1 << g[2]
    return op_bound(re, g[1], 1 << g[2])


def trace_norm_frob_upper(re, im, den, rank):
    sq = sum(int(v) ** 2 for v in re.flat) + sum(int(v) ** 2 for v in im.flat)
    q = int(rank) * sq
    r = isqrt(q)
    if r * r < q:
        r += 1
    return F(r, int(den))


def exact_channel_digest(L):
    h = hashlib.sha256()
    for a in range(7):
        for k in range(11):
            for i in range(2):
                for j in range(2):
                    re, im, e = L[a][k][i][j]
                    h.update(f"{a}:{k}:{i}:{j}:{e};".encode())
                    h.update(",".join(str(int(v)) for v in re.flat).encode())
                    h.update(b"|")
                    h.update(",".join(str(int(v)) for v in im.flat).encode())
    return h.hexdigest()


# ---------------------------------------------------------------------------
# frozen endpoint/channel reconstruction
# ---------------------------------------------------------------------------

def reviewer_taylor_endpoints(times, steps, Hq, Xq):
    H = np.asarray(Hq, float) / B
    X = np.asarray(Xq, float) / B
    out = []
    for t, s in zip(times, steps):
        v = X.astype(complex)
        for _ in range(int(s)):
            term = v.copy()
            acc = v.copy()
            for j in range(1, 33):
                term = (-1j * (t / s) / j) * (H @ term)
                acc = acc + term
            v = acc
        rr = np.rint(v.real * B).astype(np.int64)
        ii = np.rint(v.imag * B).astype(np.int64)
        out.append((rr, ii))
    return out


def exact_block_channels(Ws, endpoints):
    channels = []
    for a, (n, m) in enumerate(zip(NS, MS)):
        W = Ws[a]
        per = []
        for pr, pi in endpoints:
            psi = unpack(pr, pi, 40)
            fs = []
            for mu in range(m):
                wm = (W[0][:, mu::m], W[1][:, mu::m], 40)
                vr, vi = [], []
                for r in range(32):
                    p = (psi[0][r * 14:(r + 1) * 14], psi[1][r * 14:(r + 1) * 14], 40)
                    f = mm(adj(wm), p)
                    vr.append(f[0])
                    vi.append(f[1])
                fs.append((np.vstack(vr), np.vstack(vi), 80))
            ops = []
            for i in range(2):
                row = []
                for j in range(2):
                    x = zero(32 * n, 32 * n, 160)
                    for v in fs:
                        u = (v[0][:, i:i + 1], v[1][:, i:i + 1], 80)
                        w = (v[0][:, j:j + 1], v[1][:, j:j + 1], 80)
                        x = add(x, mm(u, adj(w)))
                    row.append(x)
                ops.append(row)
            per.append(ops)
        channels.append(per)
    return channels


def reconstruct_channels():
    mz = np.load(INPUTS / "model-enclosure.npz", allow_pickle=False)
    hist = reviewer_taylor_endpoints(HIST_TIMES, [64] * 7, mz["H_real"], mz["X_real"])
    fz = np.load(INPUTS / "forward-endpoints.npz", allow_pickle=False)
    fwd = [(fz[f"psi{k}_real"], fz[f"psi{k}_imag"]) for k in range(4)]
    wz = np.load(INPUTS / "pr201-certified-map-dyadic.npz", allow_pickle=False)
    Ws = [unpack(wz[f"W{a}_real"], wz[f"W{a}_imag"], 40) for a in range(7)]
    L = exact_block_channels(Ws, hist + fwd)
    digest = exact_channel_digest(L)
    if digest != EXPECTED_CHANNEL_DIGEST:
        raise RuntimeError(f"exact channel digest mismatch: {digest}")
    return L, digest


# ---------------------------------------------------------------------------
# frozen candidate parser / exact residuals
# ---------------------------------------------------------------------------

def expected_candidate_keys():
    keys = set()
    for q in "PQW":
        for a in range(7):
            keys.add(f"{q}{a}_real")
            keys.add(f"{q}{a}_imag")
    for b in range(7):
        for a in range(7):
            keys.add(f"K{b}_{a}_real")
            keys.add(f"K{b}_{a}_imag")
    return keys


def parse_candidate(path: Path, expected_sha256: str):
    if sha256_file(path) != expected_sha256:
        raise RuntimeError(f"candidate SHA256 mismatch: {path.name}")
    z = np.load(path, allow_pickle=False)
    if set(z.files) != expected_candidate_keys():
        raise RuntimeError(f"candidate schema mismatch: {path.name}")
    for k in z.files:
        if z[k].dtype != np.int64:
            raise RuntimeError(f"candidate {k} is not int64")
    Ps = [unpack(z[f"P{a}_real"], z[f"P{a}_imag"], 40) for a in range(7)]
    Qs = [unpack(z[f"Q{a}_real"], z[f"Q{a}_imag"], 40) for a in range(7)]
    rs = [p[0].shape[1] for p in Ps]
    ss = [q[0].shape[1] for q in Qs]
    if any(Ps[a][0].shape[0] != 32 * NS[a] or Qs[a][0].shape[0] != 32 * NS[a] for a in range(7)):
        raise RuntimeError("candidate support ambient dimension mismatch")
    pg = max(gram_defect(p) for p in Ps)
    qg = max(gram_defect(q) for q in Qs)
    Cs, nk = {}, {}
    gmax = F(0)
    for a in range(7):
        gram = zero(rs[a], rs[a], 80)
        for b in range(7):
            kr = z[f"K{b}_{a}_real"]
            ki = z[f"K{b}_{a}_imag"]
            if kr.ndim != 3 or kr.shape != ki.shape or kr.shape[1:] != (ss[b], rs[a]):
                raise RuntimeError(f"malformed transfer {b},{a}")
            l = int(kr.shape[0])
            nk[(b, a)] = l
            if l:
                Ks = (as_obj_int(kr).reshape(l * ss[b], rs[a]), as_obj_int(ki).reshape(l * ss[b], rs[a]), 40)
                gram = add(gram, mm(adj(Ks), Ks))
                Vr = as_obj_int(kr).transpose(0, 2, 1).reshape(l, -1).T
                Vi = as_obj_int(ki).transpose(0, 2, 1).reshape(l, -1).T
                V = (Vr, Vi, 40)
                Cs[(b, a)] = mm(V, adj(V))
            else:
                Cs[(b, a)] = zero(rs[a] * ss[b], rs[a] * ss[b], 80)
        gd = gram[0].copy()
        for i in range(rs[a]):
            gd[i, i] -= 1 << 80
        gmax = max(gmax, op_bound(gd, gram[1], 1 << 80))
    trace_bound = (1 + pg) * (1 + qg) * (1 + gmax)
    if trace_bound > C_SCALE:
        raise RuntimeError("candidate raw trace bound exceeds frozen completion scale")
    return dict(z=z, Ps=Ps, Qs=Qs, rs=rs, ss=ss, Cs=Cs, nk=nk,
                pg=pg, qg=qg, gmax=gmax, trace_bound=trace_bound)


def residual_blocks(mp, L, kc, kn):
    Ps, Qs, rs, ss, Cs = mp["Ps"], mp["Qs"], mp["rs"], mp["ss"], mp["Cs"]
    red = []
    for a in range(7):
        red.append([[mm(mm(adj(Ps[a]), L[a][kc][i][j]), Ps[a]) for j in range(2)] for i in range(2)])
    pred = []
    for b in range(7):
        brow = []
        for i in range(2):
            line = []
            for j in range(2):
                y = zero(ss[b], ss[b], 320)
                for a in range(7):
                    C = Cs[(b, a)]
                    r, s = rs[a], ss[b]
                    Sr = C[0].reshape(r, s, r, s).transpose(1, 3, 0, 2).reshape(s * s, r * r)
                    Si = C[1].reshape(r, s, r, s).transpose(1, 3, 0, 2).reshape(s * s, r * r)
                    xv = (red[a][i][j][0].reshape(-1, 1), red[a][i][j][1].reshape(-1, 1), 240)
                    v = mm((Sr, Si, 80), xv)
                    y = add(y, (v[0].reshape(s, s), v[1].reshape(s, s), 320))
                line.append(mm(mm(Qs[b], y), adj(Qs[b])))
            brow.append(line)
        pred.append(brow)
    den = (1 << 400) * CNUM
    blocks = []
    for b, n in enumerate(NS):
        d = 32 * n
        re = np.zeros((2 * d, 2 * d), dtype=object)
        im = np.zeros((2 * d, 2 * d), dtype=object)
        for i in range(2):
            for j in range(2):
                target = L[b][kn][i][j]
                raw = pred[b][i][j]
                sl = np.s_[i * d:(i + 1) * d, j * d:(j + 1) * d]
                re[sl] = target[0] * (1 << 240) * CNUM - raw[0] * (1 << 20)
                im[sl] = target[1] * (1 << 240) * CNUM - raw[1] * (1 << 20)
                if b == 0:
                    inr = sum(int(np.trace(L[a][kc][i][j][0])) for a in range(7))
                    ini = sum(int(np.trace(L[a][kc][i][j][1])) for a in range(7))
                    outr = sum(int(np.trace(pred[bb][i][j][0])) for bb in range(7))
                    outi = sum(int(np.trace(pred[bb][i][j][1])) for bb in range(7))
                    re[i * d, j * d] -= inr * (1 << 240) * CNUM - outr * (1 << 20)
                    im[i * d, j * d] -= ini * (1 << 240) * CNUM - outi * (1 << 20)
        if not np.array_equal(re, re.T) or not np.array_equal(im, -im.T):
            raise RuntimeError(f"residual sector {b} not exactly Hermitian")
        blocks.append((re, im, den))
    return blocks


# ---------------------------------------------------------------------------
# certificate routes U1 / L1 / reviewer U2+U3
# ---------------------------------------------------------------------------

def u1_exact(blocks, ss):
    tot = F(0)
    for b, (re, im, den) in enumerate(blocks):
        rank = MS[b] + 2 * ss[b] + (2 if b == 0 else 0)
        tot += trace_norm_frob_upper(re, im, den, rank) / 2
    return tot


def l1_exact(blocks):
    tot = F(0)
    for re, im, den in blocks:
        sq = sum(int(v) ** 2 for v in re.flat) + sum(int(v) ** 2 for v in im.flat)
        tot += F(isqrt(sq), int(den))
    return tot / 4


def spectral_enclosure(re, im, den, want_trout=True):
    n = re.shape[0]
    jf = np.asarray(re, float) / float(den) + 1j * np.asarray(im, float) / float(den)
    jf = (jf + jf.conj().T) / 2
    lam, V = np.linalg.eigh(jf)
    scale = 1 << SPECTRAL_BITS
    Vt = (as_obj_int(np.rint(V.real * scale)), as_obj_int(np.rint(V.imag * scale)), SPECTRAL_BITS)
    lr = [int(x) for x in np.rint(lam * float(den))]
    g = mm(adj(Vt), Vt)
    gre = g[0].copy()
    for k in range(n):
        gre[k, k] -= 1 << g[2]
    delta = op_bound(gre, g[1], 1 << g[2])
    D = np.zeros((n, n), dtype=object)
    for k, x in enumerate(lr):
        D[k, k] = x
    Jt = mm(mm(Vt, (D, np.zeros((n, n), dtype=object), 0)), adj(Vt))
    sc = 1 << (2 * SPECTRAL_BITS)
    rn = op_bound(re * sc - Jt[0], im * sc - Jt[1], int(den) * sc)
    sum_abs = F(sum(abs(x) for x in lr), int(den))
    upper = (1 + delta) * sum_abs + n * rn
    lower = max(F(0), (1 - delta) * sum_abs - n * rn) if delta < 1 else F(0)
    out = dict(upper=upper, lower=lower, delta=delta, residual=rn)
    if want_trout:
        d = n // 2
        Dabs = np.zeros((n, n), dtype=object)
        for k, x in enumerate(lr):
            Dabs[k, k] = abs(x)
        Yt = mm(mm(Vt, (Dabs, np.zeros((n, n), dtype=object), 0)), adj(Vt))
        deny = int(den) * sc
        M = {}
        for i in range(2):
            for j in range(2):
                rr = sum(int(Yt[0][i * d + k, j * d + k]) for k in range(d))
                ii = sum(int(Yt[1][i * d + k, j * d + k]) for k in range(d))
                M[(i, j)] = (F(rr, deny), F(ii, deny))
        shift = rn * d
        M[(0, 0)] = (M[(0, 0)][0] + shift, F(0))
        M[(1, 1)] = (M[(1, 1)][0] + shift, F(0))
        out["trout"] = M
    return out


def watrous_u3(spectra):
    a = sum((s["trout"][(0, 0)][0] for s in spectra), F(0))
    d = sum((s["trout"][(1, 1)][0] for s in spectra), F(0))
    br = sum((s["trout"][(0, 1)][0] for s in spectra), F(0))
    bi = sum((s["trout"][(0, 1)][1] for s in spectra), F(0))
    h = (a - d) / 2
    q2 = h * h + br * br + bi * bi
    p, q = q2.numerator, q2.denominator
    r = isqrt(p * q)
    if r * r < p * q:
        r += 1
    return ((a + d) / 2 + F(r, q)) / 2


def rigorous_upper_routes(blocks, ss):
    u1 = u1_exact(blocks, ss)
    spectra = [spectral_enclosure(*x) for x in blocks]
    u2 = sum((s["upper"] for s in spectra), F(0)) / 2
    u3 = watrous_u3(spectra)
    return {"U1": u1, "U2": u2, "U3": u3}


def _dup(x):
    return Decimal(repr(math.nextafter(float(x), math.inf)))


def model_padding(tceil: F, steps: int, ref: dict):
    with localcontext() as ctx:
        ctx.prec = 70
        ctx.rounding = ROUND_CEILING
        one, two = Decimal(1), Decimal(2)
        du = _dup(ref["U_exact_distance_bound"])
        dh = _dup(ref["Hamiltonian_error_bound"])
        dx = _dup(ref["initial_isometry_error_bound"])
        hn = _dup(ref["H_abs_norm_bound"])
        u = one / (two ** 53)
        nops = Decimal(8 * 448 + 32)
        gamma = nops * u / (one - nops * u)
        tc = Decimal(tceil.numerator) / Decimal(tceil.denominator)
        beta = hn * tc / Decimal(steps)
        if beta >= 1:
            raise RuntimeError("enclosure beta >= 1")
        term, err, acc, local = one, Decimal(0), one, Decimal(0)
        for j in range(1, 33):
            jd = Decimal(j)
            err = beta * err / jd + gamma * beta * term / jd
            term = beta * (one + gamma) * term / jd
            local = local + err + u * (acc + term)
            acc = (acc + term) * (one + u)
        tail = Decimal(3) * (beta ** 33) / Decimal(math.factorial(33))
        per = Decimal("1.1") * (local + tail)
        numerical = two * ((one + per) ** steps - one) + Decimal(64) / (two ** 40)
        time_term = (hn + one) / (two ** 40)
        pe = dx + two * tc * dh + numerical + time_term
        ve = two * du + pe
        ce = (two + ve) * ve
        q = (ce * Decimal(10 ** 12)).to_integral_value(rounding=ROUND_CEILING) / Decimal(10 ** 12)
        pad = max(Decimal("0.0000007"), q)
        return F(pad)


# ---------------------------------------------------------------------------
# exact L6 verifier: frozen TRAIN0+F1+F2 dual, no new solve
# ---------------------------------------------------------------------------

def assert_exact_ints(*arrays):
    for a in arrays:
        for v in np.asarray(a, dtype=object).flat:
            if not isinstance(v, (int, np.integer)):
                raise RuntimeError("non-integer object in exact route")


def quant(x):
    return np.rint(np.asarray(x).real * B).astype(np.int64), np.rint(np.asarray(x).imag * B).astype(np.int64)


def dy(x, bits=L6_BITS):
    a = np.asarray(x)
    sc = float(1 << bits)
    return (as_obj_int(np.rint(a.real * sc)), as_obj_int(np.rint(a.imag * sc)), bits)


def herm_dy(x, bits=L6_BITS):
    re, im, e = dy(x, bits)
    return re + re.T, im - im.T, e + 1


def kron(A, Bm):
    return (np.kron(A[0], Bm[0]) - np.kron(A[1], Bm[1]),
            np.kron(A[0], Bm[1]) + np.kron(A[1], Bm[0]), A[2] + Bm[2])


def eye(n, e=0):
    re = np.zeros((n, n), dtype=object)
    for i in range(n):
        re[i, i] = 1 << e
    return re, np.zeros((n, n), dtype=object), e


def scal(t, fr):
    den = fr.denominator
    k = den.bit_length() - 1
    if den != 1 << k:
        raise RuntimeError("non-dyadic scale")
    return t[0] * fr.numerator, t[1] * fr.numerator, t[2] + k


def up_dyadic(fr, bits=L6_BITS):
    n = -((-fr.numerator << bits) // fr.denominator)
    return F(n, 1 << bits)


def opnorm(t):
    assert_exact_ints(t[0], t[1])
    return op_bound(t[0], t[1], 1 << t[2])


def trace_re(t):
    return F(int(sum(t[0][i, i] for i in range(t[0].shape[0]))), 1 << t[2])


def psd_margin_int(M):
    re, im, e = M
    assert_exact_ints(re, im)
    if not (np.array_equal(re, re.T) and np.array_equal(im, -im.T)):
        raise RuntimeError("psd_margin_int: not exactly Hermitian")
    n = re.shape[0]
    Mf = (np.array(re, dtype=float) + 1j * np.array(im, dtype=float)) / 2.0 ** e
    lam, V = np.linalg.eigh((Mf + Mf.conj().T) / 2)
    Vt = dy(V, L6_BITS)
    g = mm(adj(Vt), Vt)
    gr = g[0].copy()
    for i in range(n):
        gr[i, i] -= 1 << g[2]
    assert_exact_ints(gr, g[1])
    delta = op_bound(gr, g[1], 1 << g[2])
    if not delta < 1:
        raise RuntimeError("psd_margin_int: eigenvector Gram defect >= 1")
    li = [int(v) for v in np.rint(lam * float(1 << L6_BITS))]
    D = np.zeros((n, n), dtype=object)
    for i in range(n):
        D[i, i] = li[i]
    Jt = mm(mm(Vt, (D, np.zeros((n, n), dtype=object), L6_BITS)), adj(Vt))
    Res = add(M, neg(Jt))
    Rn = opnorm(Res)
    mu = F(min(li), 1 << L6_BITS)
    return mu * (1 - delta) - Rn if mu >= 0 else mu * (1 + delta) - Rn


def l6_exact(L, paddings):
    z = np.load(INPUTS / "l6-dual-TRAIN0+F1+F2.npz", allow_pickle=False)
    subset = (TRANSITIONS[0], TRANSITIONS[4], TRANSITIONS[5])
    K = 3
    Pt, Qt = [], []
    for a in range(7):
        pr, pi = quant(z[f"P{a}"])
        qr, qi = quant(z[f"Q{a}"])
        Pt.append((as_obj_int(pr), as_obj_int(pi), 40))
        Qt.append((as_obj_int(qr), as_obj_int(qi), 40))
    r = [p[0].shape[1] for p in Pt]
    s = [q[0].shape[1] for q in Qt]
    dQ = [gram_defect(q) for q in Qt]
    R = [herm_dy(z[f"R{k}"]) for k in range(K)]
    Fk = {(k, b): herm_dy(z[f"F{k}_{b}"]) for k in range(K) for b in range(7)}
    La = [herm_dy(z[f"L{a}"]) for a in range(7)]

    def blk(t, i, j, n):
        return (t[0][i*n:(i+1)*n, j*n:(j+1)*n],
                t[1][i*n:(i+1)*n, j*n:(j+1)*n], t[2])

    Xc, Yc, Dn = {}, {}, {}
    for k, (_, kc, kn, _, _) in enumerate(subset):
        for a in range(7):
            for i in range(2):
                for j in range(2):
                    xa = L[a][kc][i][j]
                    xc = mm(mm(adj(Pt[a]), xa), Pt[a])
                    Xc[k, a, i, j] = xc
                    Dn[k, a, i, j] = opnorm(add(xa, neg(mm(mm(Pt[a], xc), adj(Pt[a])))))
                    ya = L[a][kn][i][j]
                    Yc[k, a, i, j] = mm(mm(adj(Qt[a]), ya), Qt[a])

    repairs = {"R_shift": [], "L_shift": [], "L_psd_shift": []}
    for k in range(K):
        worst = F(0)
        for b in range(7):
            H = kron(R[k], eye(s[b]))
            for sign in (1, -1):
                Mx = add(H, Fk[k, b] if sign > 0 else neg(Fk[k, b]))
                worst = min(worst, psd_margin_int(Mx))
        a0 = F(int(R[k][0][0, 0]), 1 << R[k][2])
        d0 = F(int(R[k][0][1, 1]), 1 << R[k][2])
        br = F(int(R[k][0][0, 1]), 1 << R[k][2])
        bi = F(int(R[k][1][0, 1]), 1 << R[k][2])
        shift = up_dyadic(-worst) if worst < 0 else F(0)
        if not (a0 + shift >= 0 and d0 + shift >= 0 and (a0 + shift)*(d0 + shift) - br*br - bi*bi >= 0):
            raise RuntimeError(f"L6 R_{k} not PSD after frozen repair")
        if shift:
            R[k] = add(R[k], scal(eye(2), shift))
        repairs["R_shift"].append(str(shift))

    t_a = []
    for a in range(7):
        worst = F(0)
        for b in range(7):
            acc = None
            for k in range(K):
                for i in range(2):
                    for j in range(2):
                        term = kron(conj(Xc[k, a, i, j]), blk(Fk[k, b], i, j, s[b]))
                        acc = term if acc is None else add(acc, term)
            Mx = add(kron(La[a], eye(s[b])), neg(acc))
            worst = min(worst, psd_margin_int(Mx))
        sh = up_dyadic(-worst) if worst < 0 else F(0)
        if sh:
            La[a] = add(La[a], scal(eye(r[a]), sh))
        repairs["L_shift"].append(str(sh))
        mL = psd_margin_int(La[a])
        sh2 = up_dyadic(-mL) if mL < 0 else F(0)
        if sh2:
            La[a] = add(La[a], scal(eye(r[a]), sh2))
        repairs["L_psd_shift"].append(str(sh2))
        ta = F(0)
        for k in range(K):
            for i in range(2):
                for j in range(2):
                    ta += Dn[k, a, i, j] * max(opnorm(blk(Fk[k, b], i, j, s[b])) for b in range(7))
        t_a.append(ta)

    pos = F(0)
    for k in range(K):
        for b in range(7):
            acc = F(0)
            for i in range(2):
                for j in range(2):
                    acc += trace_re(mm(blk(Fk[k, b], j, i, s[b]), Yc[k, b, i, j]))
            pos += acc / (1 + dQ[b])
    negt = F(0)
    for a in range(7):
        G = mm(adj(conj(Pt[a])), conj(Pt[a]))
        negt += trace_re(mm(La[a], G)) + t_a[a] * (32 * NS[a])
    norm = sum((2 * trace_re(R[k]) for k in range(K)), F(0))
    raw = (pos - negt) / norm
    pad = max(paddings["TRAIN0"], paddings["F1"], paddings["F2"])
    return raw - pad, {"raw": str(raw), "padding": str(pad), "normalisation": str(norm), "repairs": repairs}


# ---------------------------------------------------------------------------
# public entry point
# ---------------------------------------------------------------------------

def compute_all():
    started = time.monotonic()
    transitions_def, physical_class_def = consume_machine_definitions()
    with (INPUTS / "model-enclosure.json").open() as f:
        enclosure_ref = json.load(f)
    paddings = {tag: model_padding(tceil, steps, enclosure_ref)
                for tag, _, _, tceil, steps in TRANSITIONS}
    L, digest = reconstruct_channels()

    phi4 = parse_candidate(MAPS / "Phi4-candidate-map-dyadic.npz",
                           "48abd5f52812ef7503cfdde92fe630b99ded9c10c4ef35d2c4edc8d934028125")
    phi6 = parse_candidate(MAPS / "Phi6-C-S2-frob-pr213.npz",
                           "c674e471c6bbad2e3376e53315d8e1e5cb83dbbb85f4120c7b5b8602b78f7e0a")

    phi4_rows = {}
    for tag, kc, kn, _, _ in TRANSITIONS:
        blocks = residual_blocks(phi4, L, kc, kn)
        if tag in ("TRAIN0", "TRAIN1", "H1", "H2"):
            phi4_rows[tag] = {"U1": u1_exact(blocks, phi4["ss"]) + paddings[tag]}
        else:
            phi4_rows[tag] = {"L1": l1_exact(blocks) - paddings[tag]}
    U4 = max(phi4_rows[tag]["U1"] for tag in ("TRAIN0", "TRAIN1", "H1", "H2"))

    phi6_rows = {}
    for tag, kc, kn, _, _ in TRANSITIONS:
        blocks = residual_blocks(phi6, L, kc, kn)
        routes = rigorous_upper_routes(blocks, phi6["ss"])
        upper_routes = {k: v + paddings[tag] for k, v in routes.items()}
        best_route = min(upper_routes, key=upper_routes.get)
        phi6_rows[tag] = {"routes": {k: str(v) for k, v in upper_routes.items()},
                          "U": upper_routes[best_route], "route": best_route}
    K6 = max(phi6_rows[tag]["U"] for tag, *_ in TRANSITIONS)
    K6_worst = max((tag for tag, *_ in TRANSITIONS), key=lambda t: phi6_rows[t]["U"])

    L6, l6_detail = l6_exact(L, paddings)

    values = {
        "U4": U4,
        "PHI4_F1_LOWER": phi4_rows["F1"]["L1"],
        "PHI4_F2_LOWER": phi4_rows["F2"]["L1"],
        "K6_CONSTRUCTIVE_UPPER": K6,
        "L6": L6,
    }
    return {
        "values": {k: {"exact": str(v), "float": float(v)} for k, v in values.items()},
        "channel_digest": digest,
        "paddings": {k: str(v) for k, v in paddings.items()},
        "phi4_U1": {k: str(phi4_rows[k]["U1"]) for k in ("TRAIN0", "TRAIN1", "H1", "H2")},
        "phi6": {k: {"U": str(v["U"]), "route": v["route"], "routes": v["routes"]} for k, v in phi6_rows.items()},
        "K6_worst": K6_worst,
        "L6_detail": l6_detail,
        "load_bearing_calculations_actually_executed": True,
        "seconds": time.monotonic() - started,
        "transition_definition_consumed": transitions_def["transitions"],
        "physical_map_class_consumed": physical_class_def["class_id"],
        "environment": {"python_numpy": np.__version__},
    }


if __name__ == "__main__":
    print(json.dumps(compute_all(), indent=2, sort_keys=True))
