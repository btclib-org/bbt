# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Derive a Type-2 key sequence, public child keys from the master public key.

A public random number lets each child's public key be derived from the
master public key alone, without the master private key.
"""

import secrets
from hashlib import sha256 as hf

from btclib.curves.curve import mult
from btclib.curves.curve import secp256k1 as ec
from btclib.utils import int_from_bits

# master prvkey in [1, n-1]
mprvkey = 1 + secrets.randbelow(ec.n - 1)
print(f"\nmaster prvkey: {hex(mprvkey).upper()}")

# Master Pubkey:
mpubkey = mult(mprvkey, ec.G)
print(f"Master Pubkey: {hex(mpubkey[0]).upper()}")
print(f"               {hex(mpubkey[1]).upper()}")

r = secrets.randbits(ec.nlen)
print(f"\npublic random number: {hex(r).upper()}")

rbytes = r.to_bytes(ec.n_size, "big")
n_keys = 3
for i in range(n_keys):
    ibytes = i.to_bytes(ec.n_size, "big")
    hd = hf(ibytes + rbytes).digest()
    offset = int_from_bits(hd, ec.nlen) % ec.n
    q = (mprvkey + offset) % ec.n
    Q = mult(q, ec.G, ec)
    print(f"\nprvkey #{i}: {hex(q).upper()}")
    print(f"Pubkey #{i}: {hex(Q[0]).upper()}")
    print(f"           {hex(Q[1]).upper()}")

# Pubkeys could also be calculated without using prvkeys
for i in range(n_keys):
    ibytes = i.to_bytes(ec.n_size, "big")
    hd = hf(ibytes + rbytes).digest()
    offset = int_from_bits(hd, ec.nlen) % ec.n
    Q = ec.add_var(mpubkey, mult(offset, ec.G, ec))
    assert mult((mprvkey + offset) % ec.n, ec.G, ec) == Q
