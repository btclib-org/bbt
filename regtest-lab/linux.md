# Bitcoin Core Setup (Linux)

1. open terminal

1. export convenience variables (for an easy installation)

   ```shell
   export BITCOIN=bitcoin-core-31.1
   export BITCOINPLAIN=`echo $BITCOIN | sed 's/bitcoin-core/bitcoin/'`
   ```

1. download Bitcoin Core, and the checksums of its release (every time
   you see *username* in the code below, please replace it with your
   personal username)

   ```shell
   wget -O ~username/$BITCOINPLAIN-x86_64-linux-gnu.tar.gz \
     https://bitcoincore.org/bin/$BITCOIN/$BITCOINPLAIN-x86_64-linux-gnu.tar.gz
   wget -O ~username/SHA256SUMS https://bitcoincore.org/bin/$BITCOIN/SHA256SUMS
   ```

1. check the archive against those checksums: the line printed must end
   in `OK`, and anything else means the file is not the release, so stop
   here

   ```shell
   cd ~username && sha256sum --ignore-missing --check SHA256SUMS
   ```

   That `SHA256SUMS` is itself genuine is the signature check that
   [Verify your download](https://bitcoincore.org/en/download/#verify-your-download)
   walks through.

1. install Bitcoin Core

   ```shell
   /bin/tar xzf ~username/$BITCOINPLAIN-x86_64-linux-gnu.tar.gz -C ~username
   sudo /usr/bin/install -m 0755 -o root -g root -t /usr/local/bin \
     ~username/$BITCOINPLAIN/bin/*
   /bin/rm -rf ~username/$BITCOINPLAIN/
   ```

1. create the bitcoin working directory

   ```shell
   /bin/mkdir ~username/.bitcoin
   ```

1. start the Bitcoin Core daemon in regtest mode, with a fallback fee —
   without it a send fails until the node has fee estimates of its own

   ```shell
   bitcoind -regtest -daemon -fallbackfee=0.0002
   ```

You are now ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network*, stop the
daemon, wait for it to remove `bitcoind.pid`, which it does once its data is
written, and *clear the regtest data folder*. With no daemon running, `stop`
answers that it could not connect and the rest runs at once:

```shell
bitcoin-cli -regtest stop
while [ -e ~/.bitcoin/regtest/bitcoind.pid ]; do sleep 1; done
rm -rf ~/.bitcoin/regtest
```
