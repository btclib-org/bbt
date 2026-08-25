# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Sign and verify a message under each btclib message-signing address type."""

from btclib.b32 import p2wpkh
from btclib.b58 import p2pkh, p2wpkh_p2sh, wif_from_prv_key
from btclib.ecc.bms import sign, verify
from btclib.to_prv_key import prv_keyinfo_from_prv_key
from btclib.to_pub_key import pub_keyinfo_from_prv_key

msg = b"Paolo is afraid of ephemeral random numbers"
print("\n0. Message:", msg.decode())

wif = b"Kx45GeUBSMPReYQwgXiKhG9FzNXrnCeutJp4yjTd5kKxCitadm3C"
print("1. Compressed WIF:", wif.decode())
pubkey, network = pub_keyinfo_from_prv_key(wif)

print("2. Addresses")
address1 = p2pkh(pubkey)
print("      p2pkh:", address1)
address2 = p2wpkh_p2sh(pubkey)
print("p2wpkh_p2sh:", address2)
address3 = p2wpkh(pubkey)
print("     p2wpkh:", address3)


print(
    "\n3. Sign message with no address (i.e., with default compressed p2pkh address):",
)
sig1 = sign(msg, wif)
print(f"rf1: {sig1.rf}")
print(f" r1: {hex(sig1.dsa_sig.r).upper()}")
print(f" s1: {hex(sig1.dsa_sig.r).upper()}")

bsmsig1 = sig1.serialize()
print("4. Serialized signature:")
print("     bytes:", bsmsig1)
print("hex-string:", bsmsig1.hex().upper())

print("5. Verify signature")
print("Bitcoin Core p2pkh  :", verify(msg, address1, sig1))
print("Electrum p2wpkh_p2sh:", verify(msg, address2, sig1))
print("Electrum p2wpkh     :", verify(msg, address3, sig1))


print("\n3. Sign message with p2wpkh_p2sh address (BIP137):")
sig2 = sign(msg, wif, address2)
print(f"rf2: {sig2.rf}")
print(f" r2: {hex(sig2.dsa_sig.r).upper()}")
print(f" s2: {hex(sig2.dsa_sig.s).upper()}")

bsmsig2 = sig2.serialize()
print("4. Serialized signature:")
print("     bytes:", bsmsig2)
print("hex-string:", bsmsig2.hex().upper())

print("5. Verify signature")
print("Bitcoin Core p2pkh:", verify(msg, address1, sig2))
print("BIP137 p2wpkh_p2sh:", verify(msg, address2, sig2))
print("BIP137 p2wpkh     :", verify(msg, address3, sig2))


print("\n3. Sign message with p2wpkh address (BIP137):")
sig3 = sign(msg, wif, address3)
print(f"rf3: {sig3.rf}")
print(f" r3: {hex(sig3.dsa_sig.r).upper()}")
print(f" s3: {hex(sig3.dsa_sig.s).upper()}")

bsmsig3 = sig3.serialize()
print("4. Serialized signature:")
print("     bytes:", bsmsig3)
print("hex-string:", bsmsig3.hex().upper())

print("5. Verify signature")
print("Bitcoin Core p2pkh:", verify(msg, address1, sig3))
print("BIP137 p2wpkh_p2sh:", verify(msg, address2, sig3))
print("BIP137 p2wpkh     :", verify(msg, address3, sig3))


# uncompressed WIF / P2PKH address
q, network, _ = prv_keyinfo_from_prv_key(wif)
wif2 = wif_from_prv_key(q, network, compressed=False)
print("\n1. Uncompressed WIF          :", wif2)
pubkey, network = pub_keyinfo_from_prv_key(wif2)

address4 = p2pkh(pubkey)
print("2. Uncompressed P2PKH address:", address4)

print("3. Sign message with uncompressed p2pkh:")
sig4 = sign(msg, wif2, address4)
print(f"rf4: {sig4.rf}")
print(f" r4: {hex(sig4.dsa_sig.r).upper()}")
print(f" s4: {hex(sig4.dsa_sig.s).upper()}")

bsmsig4 = sig4.serialize()
print("4. Serialized signature:")
print("     bytes:", bsmsig4)
print("hex-string:", bsmsig4.hex().upper())

print("5. Verify signature")
print("Bitcoin Core compressed p2pkh  :", verify(msg, address1, sig4))
print("Electrum p2wpkh_p2sh           :", verify(msg, address2, sig4))
print("Electrum p2wpkh                :", verify(msg, address3, sig4))
print("Bitcoin Core uncompressed p2pkh:", verify(msg, address4, sig4))
