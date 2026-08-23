# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

from btclib.curves.curve import mult
from btclib.curves.curve import secp256k1 as ec
from btclib.ecc.dsa import Sig, recover_pub_keys, sign, verify

print("\n*** EC:")
print(ec)

print("0. Key generation")
q = 0x18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725
q %= ec.n
Q = mult(q, ec.G)
print(f"prvkey:    {hex(q).upper()}")
print(f"PubKey: {'02' if Q[1] % 2 == 0 else '03'} {hex(Q[0]).upper()}")


print("\n1. Message to be signed")
msg1 = "Paolo is afraid of ephemeral random numbers".encode()
print(msg1.decode())

print("2. Sign message")
sig1 = sign(msg1, q)
print(f"    r1:    {hex(sig1.r).upper()}")
print(f"    s1:    {hex(sig1.s).upper()}")

print("3. Verify signature")
print(verify(msg1, Q, sig1))

print("4. Recover keys")
keys = recover_pub_keys(msg1, sig1)
for i, key in enumerate(keys):
    print(f" key#{i}: {'02' if key[1] % 2 == 0 else '03'} {hex(key[0]).upper()}")


print("\n** Malleated signature")
sm = ec.n - sig1.s
print(f"    r1:    {hex(sig1.r).upper()}")
print(f"    sm:    {hex(sm).upper()}")

# what tells the two apart is which half of the order the s falls in:
# sign()'s lower_s argument defaults to True, and n - s is the other root
# of the same signature
print(f" s1 low:    {sig1.s < ec.n // 2}")
print(f" sm low:    {sm < ec.n // 2}")

print("** Verify malleated signature")
# and it verifies: verify() has no low-s argument, that rule being a
# policy of whoever signs
print(verify(msg1, Q, Sig(sig1.r, sm)))


print("\n1. Another message to sign")
msg2 = "and Paolo is right to be afraid".encode()
print(msg2.decode())

print("2. Sign message")
sig2 = sign(msg2, q)
print(f"    r2:    {hex(sig2.r).upper()}")
print(f"    s2:    {hex(sig2.s).upper()}")

print("3. Verify signature")
print(verify(msg2, Q, sig2))

print("4. Recover keys")
keys = recover_pub_keys(msg2, sig2)
for i, key in enumerate(keys):
    print(f" key#{i}: {'02' if key[1] % 2 == 0 else '03'} {hex(key[0]).upper()}")


print("\n** Serialize signature")
dersig = sig2.serialize()
print("     bytes:", dersig)
print("hex-string:", dersig.hex().upper())
sig3 = Sig.parse(dersig)
if sig2.r == sig3.r and sig2.s == sig3.s:
    print("Successfully parsed!")
