# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Derive a BIP39 and an Electrum seed phrase from one entropy.

Prints both phrases and the first hardened child key each one yields.
"""

import secrets

from btclib import bip32
from btclib.mnemonic import bip39, electrum

entropy = secrets.randbits(256)

bip39_mnemonic = bip39.mnemonic_from_entropy(entropy)
print()
print(bip39_mnemonic)
rxprv = bip39.mxprv_from_mnemonic(bip39_mnemonic)
rxpub = bip32.xpub_from_xprv(rxprv)
# warning: first level should always be hardened
# or any (depth=1) child private key would compromise rxprv
path = "m/0h"
xprv = bip32.derive(rxprv, path)
print(path + f" : {xprv!r}")

electrum_mnemonic = electrum.mnemonic_from_entropy(entropy=entropy)
print()
print(electrum_mnemonic)
mxprv = electrum.mxprv_from_mnemonic(electrum_mnemonic)
mxpub = bip32.xpub_from_xprv(mxprv)
# warning: first level should always be hardened
# or any (depth=1) child private key would compromise mxprv
path = "m/0h"
xprv = bip32.derive(mxprv, path)
print(path + f" : {xprv!r}")
