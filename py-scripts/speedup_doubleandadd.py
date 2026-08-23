# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

import random
import time

from btclib.curves.curve import secp256k1 as ec
from btclib.curves.curve_group import (
    _mult_aff_var,
    _mult_jac_var,
    _mult_recursive_aff_var,
    _mult_recursive_jac_var,
)

# setup
random.seed(42)
qs = [random.getrandbits(ec.nlen) % ec.n for _ in range(100)]

start = time.time()
for q in qs:
    # starts from affine coordinates, ends with affine coordinates
    ec.aff_from_jac_var(_mult_jac_var(q, ec.GJ, ec))
benchmark = time.time() - start
print("Benchmark completed")

start = time.time()
for q in qs:
    _mult_recursive_aff_var(q, ec.G, ec)
recursive_aff = time.time() - start
print(f"Recursive aff       : {recursive_aff / benchmark:.0%}")

start = time.time()
for q in qs:
    ec.aff_from_jac_var(_mult_recursive_jac_var(q, ec.GJ, ec))
recursive_jac = time.time() - start
print(f"Recursive jac       : {recursive_jac / benchmark:.0%}")

start = time.time()
for q in qs:
    _mult_aff_var(q, ec.G, ec)
double_add_aff = time.time() - start
print(f"Double and add aff  : {double_add_aff / benchmark:.0%}")

start = time.time()
for q in qs:
    ec.aff_from_jac_var(_mult_jac_var(q, ec.GJ, ec))
double_add_jac = time.time() - start
print(f"Double and add jac  : {double_add_jac / benchmark:.0%}")
