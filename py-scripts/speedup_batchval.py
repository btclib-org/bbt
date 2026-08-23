# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

import random
import time
from hashlib import sha256 as hf

from btclib.curves.curve import mult
from btclib.curves.curve import secp256k1 as ec
from btclib.ecc.ssa import batch_verify_, sign_, verify_

random.seed(42)

hsize = hf().digest_size
hlen = hsize * 8

# n = 1 loops forever and does not really test batch verify
n_sig = [4, 8, 16, 32, 64, 128, 256, 512]
m = [random.getrandbits(hlen).to_bytes(hsize, "big") for _ in range(max(n_sig))]
q = [random.getrandbits(ec.nlen) % ec.n for _ in m]
sig = [sign_(msg, qq) for msg, qq in zip(m, q)]
Q = [mult(qq, ec.G)[0] for qq in q]

for n in n_sig:

    # no batch
    start = time.time()
    for j in range(n):
        assert verify_(m[j], Q[j], sig[j])
    elapsed1 = time.time() - start

    # batch
    ms = m[:n]
    Qs = Q[:n]
    sigs = sig[:n]
    start = time.time()
    assert batch_verify_(ms, Qs, sigs), n
    elapsed2 = time.time() - start

    print(n, elapsed2 / elapsed1)
