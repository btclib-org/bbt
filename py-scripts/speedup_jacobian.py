# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

import random
import time

from btclib.curves.curve import secp256k1 as ec
from btclib.curves.curve_group import _mult_aff_var, _mult_jac_var

random.seed(42)

# setup
qs = [random.getrandbits(ec.nlen) % ec.n for _ in range(50)]
start = time.time()
for q in qs:
    _mult_aff_var(q, ec.G, ec)
elapsed1 = time.time() - start

start = time.time()
for q in qs:
    # starts from affine coordinates, ends with affine coordinates
    ec.aff_from_jac_var(_mult_jac_var(q, ec.GJ, ec))
elapsed2 = time.time() - start

print(elapsed2 / elapsed1)
