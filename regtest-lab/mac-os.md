# Bitcoin Core Setup (Mac-OS)

1. open terminal

1. download Bitcoin Core

   ```shell
   curl -O https://bitcoin.org/bin/bitcoin-core-0.17.0.1/bitcoin-0.17.0.1-osx64.tar.gz
   ```

1. extract the archive

   ```shell
   tar -zxf bitcoin-0.17.0.1-osx64.tar.gz
   ```

1. move executables into your default path to make bitcoin daemon
   running and stopping easily:

   ```shell
   sudo mkdir -p /usr/local/bin
   sudo cp bitcoin-0.17.0/bin/bitcoin* /usr/local/bin/.
   ```

1. clean up the temporary directory

   ```shell
   rm -rf bitcoin-0.17.0*
   ```

1. start the Bitcoin Core daemon in regtest mode:

   ```shell
   bitcoind -regtest -daemon
   ```

You are now ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network, remember to
clear the regtest data folder* in the bitcoin working folder:

```shell
cd /Users/your_username/Library/Application Support/Bitcoin
rm -rf regtest
```
