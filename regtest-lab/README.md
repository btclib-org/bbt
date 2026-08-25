# Bitcoin Core: `regtest` Lab Session

## Install and Run Bitcoin Core

Please install and run Bitcoin Core in `regtest` mode, following the
instructions provided for your platform:

- [windows.md](./windows.md)
- [linux.md](./linux.md)
- [mac-os.md](./mac-os.md)

## The `bitcoin-cli` Command Line Tool

In general any command line must starts with `bitcoin-cli -regtest [...]`
to use the *regtest* daemon process. In the GUI console environment
`bitcoin-cli -regtest` is already assumed and can be skipped, typing only
the `[...]` part.

- get the block count (zero if you have not generated blocks yet or
  joined other nodes which might have)

  ```shell
  $ bitcoin-cli -regtest getblockcount
  0
  ```

- create a wallet. A node does not make one by itself, so every command
  below that reaches an address or a balance needs this first; once per
  node, `loadwallet lab` being what brings it back on a later start

  ```shell
  $ bitcoin-cli -regtest createwallet lab
  {
    "name": "lab"
  }
  ```

## Digital Signature Using `bitcoin-cli`

- get a new *legacy* (non *p2sh-segwit* or *bech32*) address to be used
  for signatures, optionally labelling it with "used to sign":

  ```shell
  $ bitcoin-cli -regtest getnewaddress "used to sign" legacy
  mpXZvfkgYhpH2JR7bSrVMjxji3KnJi2s8s
  ```

- use this new address (not the `mpXZvfkgYhpH2JR7bSrVMjxji3KnJi2s8s`
  above!) to sign a message (e.g. `Hello, world!`). Note that
  `bitcoin-cli` uses the address to retrieve in background the
  corresponding private key actually used to sign:

  ```shell
  $ bitcoin-cli -regtest signmessage your_signing_address "Hello, world!"
  H6dXIhm+8cWKhYPv3e2zOba8+Nsnkh8osrZZGh4OPRR3MJk/HyzcaelHnhakg/YkUIWiFz73eY/klLgeCke8WwQ=
  ```

- verify the just generated signature (not the
  `H6dXIhm+8cWKhYPv3e2zOba8+Nsnkh8osrZZGh4OPRR3MJk/HyzcaelHnhakg/YkUIWiFz73eY/klLgeCke8WwQ=`
  above!):

  ```shell
  $ bitcoin-cli -regtest verifymessage \
      your_signing_address your_signature "Hello, world!"
  true
  ```

- finally, verify this exogenously generated signature
  `IG+uGUUJ7VJ7tNBxhyBR92BF3PeMTQmqTBvPpxZAHxuRT938ehUmXfh7eORd/XiCARQbbKFlDew1O7nJiggdx7c=`
  for the message `Yes, it's me` signed by the address
  `mkiZWnZyaYTyv6Z6frLibmNuBRwnnXTZTY`

  ```shell
  $ SIG=IG+uGUUJ7VJ7tNBxhyBR92BF3PeMTQmqTBvPpxZAHxuRT938ehUmXfh7eORd/XiCARQbbKFlDew1O7nJiggdx7c=
  $ bitcoin-cli -regtest verifymessage \
      mkiZWnZyaYTyv6Z6frLibmNuBRwnnXTZTY "$SIG" "Yes, it's me"
  true
  ```

## Block Generation

- optionally, connect to at least one node of the lab network to
  synchronize your node with the common blockchain, then check the
  updated block count, which is now probably greater than zero:

  ```shell
  $ bitcoin-cli -regtest addnode ipaddress_to_be_communicated_in_lab add
  $ bitcoin-cli -regtest getblockcount
  412
  ```

- get a new address, that will be used to receive coins:

  ```shell
  $ bitcoin-cli -regtest getnewaddress
  bcrt1q26dwxdz0ht62gpy4py6jukc4qm7yvkw22hadar
  ```

- generate 101 blocks, sending the coinbase reward to your new address
  (not the `bcrt1q26dwxdz0ht62gpy4py6jukc4qm7yvkw22hadar` above!):

  ```shell
  $ bitcoin-cli -regtest generatetoaddress 101 your_address
  [
    "...",
    ...
    "..."
  ]
  ```

## A Simple Transaction

- generating 101 blocks has created a spendable balance associated to
  your wallet:

  ```shell
  $ bitcoin-cli -regtest getbalance
  50.00000000
  ```

- send part of your balance (e.g. 0.99 coins) to
  `bcrt1qry4w50spgegfaemv7kl8q5efkfk3gpc5zvxnrd` (or any alternative
  address provided by a lab member) and note the returned transaction ID
  (`txid`)

  ```shell
  $ bitcoin-cli -regtest sendtoaddress \
      bcrt1qry4w50spgegfaemv7kl8q5efkfk3gpc5zvxnrd 0.99
  ...
  ```

- inspect the transaction, replacing `your_txid` below with the one the
  previous command returned

  ```shell
  $ bitcoin-cli -regtest gettransaction your_txid
  {
    "amount": -0.99000000,
    "fee": -0.00002820,
    "confirmations": 0,
    "trusted": true,
    "txid": "...",
    "wtxid": "...",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": ...,
    "timereceived": ...,
    "bip125-replaceable": "yes",
    "details": [
      {
        "address": "bcrt1qry4w50spgegfaemv7kl8q5efkfk3gpc5zvxnrd",
        "category": "send",
        "amount": -0.99000000,
        "vout": 0,
        "fee": -0.00002820,
        "abandoned": false
      }
    ],
    "hex": "...",
    "lastprocessedblock": {
      "hash": "...",
      "height": 101
    }
  }
  ```

  The block above is an illustration and not a screenshot: every `...`
  stands for a value only your own run produces, and there is nothing to
  compare it against. What is worth comparing is the rest — the keys,
  their order, and the amounts, which are the same on any machine that
  followed these pages, because `-fallbackfee=0.0002` is what fixes the
  fee. Two exceptions to expect: `vout` is `0` or `1` depending on which
  of the two outputs the wallet happened to put first, and `height` is
  the number of blocks you have generated so far.

- no confirmation yet; now generate one more block and notice that the
  transaction has been confirmed:

  ```shell
  $ bitcoin-cli -regtest generatetoaddress 1 your_address
  [
    "..."
  ]
  $ bitcoin-cli -regtest gettransaction your_txid
  {
    "amount": -0.99000000,
    "fee": -0.00002820,
    "confirmations": 1,
    "blockhash": "...",
    "blockheight": 102,
    "blockindex": 1,
    "blocktime": ...,
    "txid": "...",
    "wtxid": "...",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": ...,
    "timereceived": ...,
    "bip125-replaceable": "no",
    "details": [
      {
        "address": "bcrt1qry4w50spgegfaemv7kl8q5efkfk3gpc5zvxnrd",
        "category": "send",
        "amount": -0.99000000,
        "vout": 0,
        "fee": -0.00002820,
        "abandoned": false
      }
    ],
    "hex": "...",
    "lastprocessedblock": {
      "hash": "...",
      "height": 102
    }
  }
  ```

  Four keys are new since the block before it — `blockhash`,
  `blockheight`, `blockindex` and `blocktime` — and `bip125-replaceable`
  has turned from `yes` to `no`: a transaction in a block can no longer
  be replaced. `lastprocessedblock` now names the block that confirmed
  it, which is the one `generatetoaddress` just printed. Its `height`
  and `blockheight` are the same kind of number as before: these if
  you generated exactly the blocks these pages ask for, larger if you
  generated more.

- stop the daemon (and the GUI) with the command

  ```shell
  bitcoin-cli -regtest stop
  ```

## Further Material

For a [full command list](https://bitcoincore.org/en/doc/31.0.0/):

```shell
bitcoin-cli help
```

For help about a peculiar command (e.g. `generatetoaddress`, which the
command list above does not carry, the site documenting no `generate`
RPC):

```shell
bitcoin-cli generatetoaddress
```

To go beyond this short lab, please see
<https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line>
