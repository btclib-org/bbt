# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Sign and verify ECDSA by hand, from btclib's number-theory primitives.

Shows that the public key is recoverable from the signature alone, that a
signature's s can be malleated into another valid one, and what reusing an
ephemeral key across two messages exposes.
"""

from hashlib import sha256

from btclib.curves.curve import mult
from btclib.curves.curve import secp256k1 as ec
from btclib.exceptions import BTClibValueError
from btclib.number_theory import mod_inv
from btclib.utils import int_from_bits

# note: no import from btclib.ecc.dsa
# the private key is recoverable from the two signatures below, and this
# script stops short of doing it on purpose: ipynb/DSA.ipynb sets that as
# the reader's exercise, and a script that answered it would spend it

print("\n*** EC:")
print(ec)

print("0. Key generation")
q = 0x18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725
q %= ec.n
Q = mult(q, ec.G)
print(f"prvkey:    {hex(q).upper()}")
print(f"PubKey: {'02' if Q[1] % 2 == 0 else '03'} {hex(Q[0]).upper()}")


print("\n1. Message to be signed")
msg1 = b"Paolo is afraid of ephemeral random numbers"
print(msg1.decode())

print("2. Sign message")
msghd1 = sha256(msg1).digest()
# hash(msg) must be transformed into an integer modulo ec.n, and
# int_from_bits is the transformation SEC 1 v.2 4.1.3(5) asks for: it
# drops the bits by which the digest is longer than the group order.
# Here it drops none, ec.nlen being 256 and the digest 256 bits, so the
# plainer int.from_bytes(msghd1, "big") is the same number -- on a curve
# whose order is shorter it is not
c1 = int_from_bits(msghd1, ec.nlen) % ec.n
assert c1 != 0
print(f"    c1:    {hex(c1).upper()}")

# ephemeral key k must be kept secret and never reused !!!!!
# good choice: k = hf(q||c)
# different for each msg, private because of q
temp = q.to_bytes(32, "big") + c1.to_bytes(32, "big")
k1_bytes = sha256(temp).digest()
k1 = int_from_bits(k1_bytes, ec.nlen) % ec.n
assert 0 < k1 < ec.n, "Invalid ephemeral key"
print(f"eph k1:    {hex(k1).upper()}")

K1 = mult(k1, ec.G)
r1 = K1[0] % ec.n
# if r1 == 0 (extremely unlikely for large ec.n) go back to a different k
assert r1 != 0
s1 = (c1 + r1 * q) * mod_inv(k1, ec.n) % ec.n
# if s1 == 0 (extremely unlikely for large ec.n) go back to a different k
assert s1 != 0
print(f"    r1:    {hex(r1).upper()}")
print(f"    s1:    {hex(s1).upper()}")

print("3. Verify signature")
w = mod_inv(s1, ec.n)
u = (c1 * w) % ec.n
v = (r1 * w) % ec.n
assert u != 0
assert v != 0
U = mult(u, ec.G)
V = mult(v, Q)
x, y = ec.add_var(U, V)
print(r1 == x % ec.n)

print("4. Recover keys")
# the verification just above recomputes K = s^-1 (c G + r Q) and reads
# its x; solved for Q instead, the same equation is Q = r^-1 (s K - c G),
# which needs no private key. K is not in the signature, but r is K[0]
# reduced mod ec.n, so K[0] is r or r + ec.n -- 2*ec.n exceeds ec.p, so
# there is no third -- and an x on the curve carries two y, one of each
# parity: four candidate K at most, one of them the K the signing step
# above computed, and its Q the signer's public key
r1_inv = mod_inv(r1, ec.n)
cG = mult(c1, ec.G)
i = 0
for x_K in (r1, r1 + ec.n):
    try:
        y_even = ec.y_even_var(x_K)
    except BTClibValueError:
        # x_K is outside the field, or is no curve point's x-coordinate
        continue
    for y_K in (y_even, ec.p - y_even):
        sK = mult(s1, (x_K, y_K))
        key = mult(r1_inv, ec.add_var(sK, ec.negate(cG)))
        print(f" key#{i}: {'02' if key[1] % 2 == 0 else '03'} {hex(key[0]).upper()}")
        i += 1


print("\n** Malleated signature")
sm = ec.n - s1
print(f"    r1:    {hex(r1).upper()}")
print(f"    sm:    {hex(sm).upper()}")

print("** Verify malleated signature")
w = mod_inv(sm, ec.n)
u = c1 * w % ec.n
v = r1 * w % ec.n
assert u != 0
assert v != 0
U = mult(u, ec.G)
V = mult(v, Q)
x, y = ec.add_var(U, V)
print(r1 == x % ec.n)


print("\n1. Another message to sign")
msg2 = b"and Paolo is right to be afraid"
print(msg2.decode())

print("2. Sign message")
msghd2 = sha256(msg2).digest()
# hash(msg) must be transformed into an integer modulo ec.n:
c2 = int_from_bits(msghd2, ec.nlen) % ec.n
assert c2 != 0
print(f"    c2:    {hex(c2).upper()}")

# very bad! Never reuse an ephemeral key!!!
k2 = k1
print(f"eph k2:    {hex(k2).upper()}")

K2 = mult(k2, ec.G)
r2 = K2[0] % ec.n
# if r2 == 0 (extremely unlikely for large ec.n) go back to a different k
assert r2 != 0
s2 = (c2 + r2 * q) * mod_inv(k2, ec.n) % ec.n
# if s2 == 0 (extremely unlikely for large ec.n) go back to a different k
assert s2 != 0
print(f"    r2:    {hex(r2).upper()}")
print(f"    s2:    {hex(s2).upper()}")

print("3. Verify signature")
w = mod_inv(s2, ec.n)
u = c2 * w % ec.n
v = r2 * w % ec.n
assert u != 0
assert v != 0
U = mult(u, ec.G)
V = mult(v, Q)
x, y = ec.add_var(U, V)
print(r2 == x % ec.n)
