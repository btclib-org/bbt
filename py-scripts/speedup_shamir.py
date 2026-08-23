# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

import random
import time

from btclib.ecc.curve import secp256k1 as ec
from btclib.curvegroup import _double_mult, _mult

random.seed(42)

# setup
us = []
vs = []
QJs = []
for _ in range(500):
    us.append(random.getrandbits(ec.nlen) % ec.n)
    vs.append(random.getrandbits(ec.nlen) % ec.n)
    q = random.getrandbits(ec.nlen) % ec.n
    QJs.append(_mult(q, ec.GJ, ec))

"""
for u, v, QJ in zip(us, vs, QJs):
    t1 = ec._add_jac(_mult(u, ec.GJ, ec), _mult(v, QJ, ec))
    t2 = _double_mult(u, ec.GJ, v, QJ, ec)
    assert ec._jac_equality(t1, t2)
"""

start = time.time()
for u, v, QJ in zip(us, vs, QJs):
    ec._add_jac(_mult(u, ec.GJ, ec), _mult(v, QJ, ec))
elapsed1 = time.time() - start

start = time.time()
for u, v, QJ in zip(us, vs, QJs):
    _double_mult(u, ec.GJ, v, QJ, ec)
elapsed2 = time.time() - start

print(f"{elapsed2 / elapsed1:.0%}")
