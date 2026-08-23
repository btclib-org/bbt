# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

""" Deterministic Key Sequence (Type-1)"""

import secrets
from hashlib import sha256 as hf

from btclib.ecc.curve import mult
from btclib.ecc.curve import secp256k1 as ec
from btclib.utils import int_from_bits

# master prvkey
mprvkey = 1 + secrets.randbelow(ec.n - 1)
print(f"\nmaster private key = {hex(mprvkey).upper()}")

mprvkey_bytes = mprvkey.to_bytes(ec.nlen, "big")
nKeys = 3
for i in range(nKeys):
    ibytes = i.to_bytes(ec.nlen, "big")
    hd = hf(ibytes + mprvkey_bytes).digest()
    q = int_from_bits(hd, ec.nlen) % ec.n
    Q = mult(q, ec.G)
    print(f"\nprvkey# {i}: {hex(q).upper()}")
    print(f"Pubkey# {i}: {hex(Q[0]).upper()}")
    print(f"           {hex(Q[1]).upper()}")
