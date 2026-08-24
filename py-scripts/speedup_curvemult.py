# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Benchmark every scalar-multiplication strategy against plain double-and-add.

The strategies come from curve_group.py and curve_group_2.py.
"""

import random
import time

from btclib.curves.curve import secp256k1 as ec
from btclib.curves.curve_group import (
    _cached_multiples,
    _cached_multiples_fixwind,
    _mult,
    _mult_base_3_var,
    _mult_fixed_window_cached_var,
    _mult_fixed_window_var,
    _mult_jac_var,
    _mult_mont_ladder_var,
)
from btclib.curves.curve_group_2 import (
    _mult_endomorphism_secp256k1,
    _mult_sliding_window_var,
    _mult_w_NAF_var,
)

# the windows btclib uses for itself: curve.py sets _ENDOMORPHISM_W to 4,
# and _cached_multiples_fixwind's docstring says it is made for w=4. Each
# of those functions takes the window as an argument, so a benchmark of
# them has to name it
W_ENDOMORPHISM = 4
W_FIXWIND = 4

# setup
random.seed(42)
qs = [random.getrandbits(ec.nlen) % ec.n for _ in range(300)]

gen_only = True
print("generator only") if gen_only else print("random points")

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
start = time.time()
for q in qs:
    T = _mult(q, ec.GJ, ec) if gen_only else _mult(q, T, ec)
benchmark = time.time() - start
print("Benchmark completed", _cached_multiples.cache_info())

T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_jac_var(q, ec.GJ, ec) if gen_only else _mult_jac_var(q, T, ec)
double_and_add = time.time() - start
print(f"Double & add     : {double_and_add / benchmark:.0%}")

T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_mont_ladder_var(q, ec.GJ, ec) if gen_only else _mult_mont_ladder_var(q, T, ec)
montgomery = time.time() - start
print(f"Montgomery ladder: {montgomery / benchmark:.0%}")

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_base_3_var(q, ec.GJ, ec) if gen_only else _mult_base_3_var(q, T, ec)
base3 = time.time() - start
print(f"Base 3           : {base3 / benchmark:.0%}", _cached_multiples.cache_info())

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 4
cached = False
start = time.time()
for q in qs:
    T = (
        _mult_fixed_window_var(q, ec.GJ, ec, w, cached)
        if gen_only
        else _mult_fixed_window_var(q, T, ec, w, cached)
    )
fixed_window_4 = time.time() - start
print(
    f"Fixed window 4   : {fixed_window_4 / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 5
cached = False
start = time.time()
for q in qs:
    T = (
        _mult_fixed_window_var(q, ec.GJ, ec, w, cached)
        if gen_only
        else _mult_fixed_window_var(q, T, ec, w, cached)
    )
fixed_window_5 = time.time() - start
print(
    f"Fixed window 5   : {fixed_window_5 / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 4
cached = True
start = time.time()
for q in qs:
    T = (
        _mult_fixed_window_var(q, ec.GJ, ec, w, cached)
        if gen_only
        else _mult_fixed_window_var(q, T, ec, w, cached)
    )
fixed_window_4_ca = time.time() - start
print(
    f"Fixed window 4 ca: {fixed_window_4_ca / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 5
cached = True
start = time.time()
for q in qs:
    T = (
        _mult_fixed_window_var(q, ec.GJ, ec, w, cached)
        if gen_only
        else _mult_fixed_window_var(q, T, ec, w, cached)
    )
fixed_window_5_ca = time.time() - start
print(
    f"Fixed window 5 ca: {fixed_window_5_ca / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples_fixwind.cache_clear()
_cached_multiples_fixwind(ec.GJ, ec, W_FIXWIND)
T = ec.GJ
start = time.time()
for q in qs:
    T = (
        _mult_fixed_window_cached_var(q, ec.GJ, ec, W_FIXWIND)
        if gen_only
        else _mult_fixed_window_cached_var(q, T, ec, W_FIXWIND)
    )
fixed_window_cached = time.time() - start
print(
    f"New Fixed window : {fixed_window_cached / benchmark:.0%}",
    _cached_multiples_fixwind.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 4
start = time.time()
for q in qs:
    T = (
        _mult_sliding_window_var(q, ec.GJ, ec, 5)
        if gen_only
        else _mult_sliding_window_var(q, T, ec, w)
    )
sliding_window_4 = time.time() - start
print(
    f"Sliding window 4 : {sliding_window_4 / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 5
start = time.time()
for q in qs:
    T = (
        _mult_sliding_window_var(q, ec.GJ, ec, 5)
        if gen_only
        else _mult_sliding_window_var(q, T, ec, w)
    )
sliding_window_5 = time.time() - start
print(
    f"Sliding window 5 : {sliding_window_5 / benchmark:.0%}",
    _cached_multiples.cache_info(),
)

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 4
start = time.time()
for q in qs:
    T = _mult_w_NAF_var(q, ec.GJ, ec, 4) if gen_only else _mult_w_NAF_var(q, T, ec, w)
wNAF_4 = time.time() - start
print(f"wNAF 4           : {wNAF_4 / benchmark:.0%}", _cached_multiples.cache_info())

_cached_multiples.cache_clear()
_cached_multiples(ec.GJ, ec)
T = ec.GJ
w = 5
start = time.time()
for q in qs:
    T = _mult_w_NAF_var(q, ec.GJ, ec, 4) if gen_only else _mult_w_NAF_var(q, T, ec, w)
wNAF_5 = time.time() - start
print(f"wNAF 5           : {wNAF_5 / benchmark:.0%}", _cached_multiples.cache_info())


T = ec.GJ
start = time.time()
for q in qs:
    T = (
        _mult_endomorphism_secp256k1(q, ec.GJ, ec, W_ENDOMORPHISM)
        if gen_only
        else _mult_endomorphism_secp256k1(q, T, ec, W_ENDOMORPHISM)
    )
endomorphism1 = time.time() - start
print(f"Mult eff end     : {endomorphism1 / benchmark:.0%}")
