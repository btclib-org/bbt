# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Benchmark Shamir's trick against two double-and-add multiplications.

The two multiplications are added together afterwards; Shamir's trick combines
them into one double-and-add pass over the bits of both scalars.
"""

import random
import time

from btclib_ecc.curves.curve import secp256k1 as ec
from btclib_ecc.curves.curve_group import _double_mult_var, _mult_jac_var

random.seed(42)

# setup
us = []
vs = []
QJs = []
for _ in range(500):
    us.append(random.getrandbits(ec.nlen) % ec.n)
    vs.append(random.getrandbits(ec.nlen) % ec.n)
    q = random.getrandbits(ec.nlen) % ec.n
    QJs.append(_mult_jac_var(q, ec.GJ, ec))

# the two methods agree, checked outside the timed loops
for u, v, QJ in zip(us, vs, QJs, strict=True):
    t1 = ec.add_jac(_mult_jac_var(u, ec.GJ, ec), _mult_jac_var(v, QJ, ec))
    t2 = _double_mult_var(u, ec.GJ, v, QJ, ec)
    assert ec.is_jac_equal(t1, t2)

start = time.time()
for u, v, QJ in zip(us, vs, QJs, strict=True):
    ec.add_jac(_mult_jac_var(u, ec.GJ, ec), _mult_jac_var(v, QJ, ec))
elapsed1 = time.time() - start

start = time.time()
for u, v, QJ in zip(us, vs, QJs, strict=True):
    _double_mult_var(u, ec.GJ, v, QJ, ec)
elapsed2 = time.time() - start

print(f"{elapsed2 / elapsed1:.0%}")
