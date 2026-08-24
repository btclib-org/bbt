# Bitcoin Core Setup (Mac-OS)

1. open terminal

1. name the build for your machine — `arm64` for Apple silicon,
   `x86_64` for an Intel Mac, which `uname -m` tells you:

   ```shell
   export BITCOINARCH=arm64-apple-darwin
   ```

1. download Bitcoin Core

   ```shell
   curl -O https://bitcoincore.org/bin/bitcoin-core-31.1/bitcoin-31.1-$BITCOINARCH.tar.gz
   ```

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
   rm -rf bitcoin-31.1*
   ```

1. start the Bitcoin Core daemon in regtest mode, with a fallback fee —
   without it a send fails until the node has fee estimates of its own:

   ```shell
   bitcoind -regtest -daemon -fallbackfee=0.0002
   ```

You are now ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network, remember to
clear the regtest data folder* in the bitcoin working folder:

```shell
cd /Users/your_username/Library/Application Support/Bitcoin
rm -rf regtest
```
