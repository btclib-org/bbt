# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Benchmark fixed-window and Montgomery-ladder against double-and-add."""

import random
import time

from btclib.curves.curve import secp256k1 as ec
from btclib.curves.curve_group import (
    _mult_base_3_var,
    _mult_fixed_window_var,
    _mult_jac_var,
    _mult_mont_ladder_var,
)

# _mult_fixed_window_var asks whether to index the memoized table. What
# this script times against double & add is the window decomposition
# itself, so it does not, and speedup_curvemult.py is where the cached
# arm is measured beside the uncached one
CACHED = False

# setup
random.seed(42)
qs = [random.getrandbits(ec.nlen) % ec.n for _ in range(300)]


T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_jac_var(q, T, ec)
benchmark = time.time() - start
print("Benchmark completed")

T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_jac_var(q, T, ec)
double_and_add = time.time() - start
print(f"Double & add     : {double_and_add / benchmark:.0%}")

T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_mont_ladder_var(q, T, ec)
montgomery = time.time() - start
print(f"Montgomery ladder: {montgomery / benchmark:.0%}")

T = ec.GJ
start = time.time()
for q in qs:
    T = _mult_base_3_var(q, T, ec)
base3 = time.time() - start
print(f"Base 3           : {base3 / benchmark:.0%}")

T = ec.GJ
w = 4
start = time.time()
for q in qs:
    T = _mult_fixed_window_var(q, T, ec, w, CACHED)
fixed_window_4 = time.time() - start
print(f"Fixed window 4   : {fixed_window_4 / benchmark:.0%}")

T = ec.GJ
w = 5
start = time.time()
for q in qs:
    T = _mult_fixed_window_var(q, T, ec, w, CACHED)
fixed_window_5 = time.time() - start
print(f"Fixed window 5   : {fixed_window_5 / benchmark:.0%}")
