# Bitcoin Core Setup (Mac-OS)

1. open terminal

1. name the build for your machine — `arm64` for Apple silicon,
   `x86_64` for an Intel Mac, which `uname -m` tells you:

   ```shell
   export BITCOINARCH=arm64-apple-darwin
   ```

1. download Bitcoin Core, and the checksums of its release

   ```shell
   curl -O https://bitcoincore.org/bin/bitcoin-core-31.1/bitcoin-31.1-$BITCOINARCH.tar.gz
   curl -O https://bitcoincore.org/bin/bitcoin-core-31.1/SHA256SUMS
   ```

1. check the archive against those checksums: the line printed must end
   in `OK`, and anything else means the file is not the release, so stop
   here

   ```shell
   shasum -a 256 --ignore-missing -c SHA256SUMS
   ```

   That `SHA256SUMS` is itself genuine is the signature check that
   [Verify your download](https://bitcoincore.org/en/download/#verify-your-download)
   walks through.

1. extract the archive

   ```shell
   tar -zxf bitcoin-31.1-$BITCOINARCH.tar.gz
   ```

1. move executables into your default path to make bitcoin daemon
   running and stopping easily:

   ```shell
   sudo mkdir -p /usr/local/bin
   sudo cp bitcoin-31.1/bin/bitcoin* /usr/local/bin/.
   ```

1. clean up the temporary directory

   ```shell
   rm -rf bitcoin-31.1* SHA256SUMS
   ```

1. start the Bitcoin Core daemon in regtest mode, with a fallback fee —
   without it a send fails until the node has fee estimates of its own:

   ```shell
   bitcoind -regtest -daemon -fallbackfee=0.0002
   ```

You are now ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network*, stop the
daemon, wait for it to remove `bitcoind.pid`, which it does once its data is
written, and *clear the regtest data folder*. With no daemon running, `stop`
answers that it could not connect and the rest runs at once:

```shell
REGTEST="$HOME/Library/Application Support/Bitcoin/regtest"
bitcoin-cli -regtest stop
while [ -e "$REGTEST/bitcoind.pid" ]; do sleep 1; done
rm -rf "$REGTEST"
```
