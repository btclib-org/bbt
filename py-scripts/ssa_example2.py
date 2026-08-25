# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Sign and verify ECSSA by hand, from btclib's curve primitives.

Reuses an ephemeral key across two messages, the way dsa_example2.py does for
ECDSA.
"""

from hashlib import sha256

from btclib.curves.curve import double_mult_var, mult
from btclib.curves.curve import secp256k1 as ec
from btclib.utils import int_from_bits


def tagged_hash(tag: str, x: bytes) -> bytes:
    """Return BIP340's tagged hash of x under tag."""
    t = sha256(tag.encode()).digest()
    return sha256(t + t + x).digest()


def challenge(x_K: int, x_Q: int, msg: bytes) -> int:
    """Return the challenge over the two x coordinates and the message."""
    t = tagged_hash(
        "BIP0340/challenge",
        x_K.to_bytes(32, "big") + x_Q.to_bytes(32, "big") + msg,
    )
    return int_from_bits(t, ec.nlen) % ec.n


print("\n*** EC:")
print(ec)

print("Key generation")
q = 0x18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725
q %= ec.n
Q = mult(q, ec.G)
if Q[1] % 2:
    q = ec.n - q
    Q = (Q[0], ec.p - Q[1])
print(f"prvkey: {hex(q).upper()}")
print(f"PubKey: {hex(Q[0]).upper()}")


print("\n1. Message to be signed")
orig_msg1 = "Paolo is afraid of ephemeral random numbers"
msg1 = sha256(orig_msg1.encode()).digest()
print(msg1.hex().upper())


print("\n*** Ephemeral key and challenge")
# ephemeral key k must be kept secret and never reused !!!!!
# good choice: k = hf(q||msg)
# different for each msg, private because of q
temp = q.to_bytes(32, "big") + msg1
k1_bytes = sha256(temp).digest()
k1 = int.from_bytes(k1_bytes, "big") % ec.n
k1 = int_from_bits(k1_bytes, ec.nlen) % ec.n
assert 0 < k1 < ec.n, "Invalid ephemeral key"

K1 = mult(k1, ec.G)
# x_K is all the verifier gets, so K is the even-y point of the two, and
# an ephemeral key landing on the odd one is negated -- the same choice
# made for the public key above, made again for each signature
if K1[1] % 2:
    k1 = ec.n - k1
    K1 = (K1[0], ec.p - K1[1])
print(f"eph k: {hex(k1).upper()}")

c1 = challenge(K1[0], Q[0], msg1)
print(f"   c1: {hex(c1).upper()}")


print("2. Sign message")
r1 = K1[0]
s1 = (k1 + c1 * q) % ec.n
print(f"   r1: {hex(r1).upper()}")
print(f"   s1: {hex(s1).upper()}")


print("3. Verify signature")
K = double_mult_var(-c1, Q, s1, ec.G)
# s*G - c*Q is K itself, and BIP340 names only its even-y root, so the
# parity is as much of the check as the x coordinate is
print(K[0] == r1 and K[1] % 2 == 0)


print("\n1. Another message to sign")
orig_msg2 = "and Paolo is right to be afraid"
msg2 = sha256(orig_msg2.encode()).digest()
print(msg2.hex().upper())


print("\n*** Ephemeral key and challenge")
# ephemeral key k must be kept secret and never reused !!!!!
k2 = k1

K2 = mult(k2, ec.G)
if K2[1] % 2:
    k2 = ec.n - k2
    K2 = (K2[0], ec.p - K2[1])
print(f"eph k: {hex(k2).upper()}")

c2 = challenge(K2[0], Q[0], msg2)
print(f"   c2: {hex(c2).upper()}")


print("2. Sign message")
r2 = K2[0]
s2 = (k2 + c2 * q) % ec.n
print(f"   r2: {hex(r2).upper()}")
print(f"   s2: {hex(s2).upper()}")


print("3. Verify signature")
K = double_mult_var(-c2, Q, s2, ec.G)
print(K[0] == r2 and K[1] % 2 == 0)
