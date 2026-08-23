# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

import hashlib

from btclib import base58
from btclib.curves.curve import mult

# https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
prvkey = 0x18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725

print("\n** [0] Private ECDSA Key:")
print(hex(prvkey))

PubKey = mult(prvkey)
PubKey_bytes = (
    b"\x04"
    + PubKey[0].to_bytes(32, byteorder="big")
    + PubKey[1].to_bytes(32, byteorder="big")
)
print("\n*** [1] Public Key (uncompressed):")
print(PubKey_bytes.hex())

print("\n** [2] SHA-256 hashing of the public key:")
h1 = hashlib.sha256(PubKey_bytes).digest()
print(h1.hex())

print("\n*** [3] RIPEMD-160 hashing on the result of SHA-256, i.e., HASH160:")
h2 = hashlib.new("ripemd160", h1).digest()
print(h2.hex())

version_byte = "\x00"  # for mainnet
print("\n*** [4] version byte added in front of the HASH160:")
vh160 = b"\x00" + h2
print(vh160.hex())

print("\n** [5] SHA-256 hashing of the extended HASH160:")
h3 = hashlib.sha256(vh160).digest()
print(h3.hex())

print("\n** [6] second SHA-256 hashing of the previous result:")
h4 = hashlib.sha256(h3).digest()
print(h4.hex())

print("\n** [7] First 4 bytes of the second SHA-256 used as checksum:")
print(h4[:4].hex())

print("\n** [8] checksum added at the end of extended HASH160:")
addr = vh160 + h4[:4]
print(addr.hex())

print("\n** [9] Base58 encoded address from uncompressed PubKey")
address = base58._b58encode(addr)
print(address)
assert address == b"16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"
assert base58.encode(vh160) == b"16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"

print("\n** steps [5]-[9] are also known as Base58Check b58encode")


def hash_160_from_address(addr: bytes) -> bytes:
    return base58.decode(addr)[1:21]


print("\n*** HASH160 from address")
print(hash_160_from_address(address).hex())


def pubkey_bytes_from_prvkey(prvkey: int, compressed: bool = True) -> bytes:
    PubKey = mult(prvkey)
    if compressed:
        prefix = b"\x02" if (PubKey[1] % 2 == 0) else b"\x03"
        return prefix + PubKey[0].to_bytes(32, byteorder="big")
    return (
        b"\x04"
        + PubKey[0].to_bytes(32, byteorder="big")
        + PubKey[1].to_bytes(32, byteorder="big")
    )


print("\n** [1] Public Key compressed:")
PubKey_bytes = pubkey_bytes_from_prvkey(prvkey, True)
print(PubKey_bytes.hex())


def hash160(inp: bytes) -> bytes:
    h1 = hashlib.sha256(inp).digest()
    return hashlib.new("ripemd160", h1).digest()


def address_from_pubkey_bytes(inp: bytes, version: bytes = b"\x00") -> bytes:
    vh160 = version + hash160(inp)
    return base58.encode(vh160)


print("\n*** [9] base58 encoded address from compressed PubKey_bytes")
address = address_from_pubkey_bytes(PubKey_bytes)
assert address == b"1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs"
print(address)
