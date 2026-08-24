# Bitcoin Core Setup (Linux)

1. open terminal

1. export convenience variables (for an easy installation)

   ```shell
   export BITCOIN=bitcoin-core-31.1
   export BITCOINPLAIN=`echo $BITCOIN | sed 's/bitcoin-core/bitcoin/'`
   ```

1. download relevant files (every time you see *username* in the code
   below, please replace it with your personal username)

   ```shell
   wget -O ~username/$BITCOINPLAIN-x86_64-linux-gnu.tar.gz \
     https://bitcoincore.org/bin/$BITCOIN/$BITCOINPLAIN-x86_64-linux-gnu.tar.gz
   ```

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

Whenever you want *to start with a fresh new regtest network, remember to
clear the regtest data folder* in the bitcoin working folder:

```shell
cd .bitcoin
rm -rf regtest
```
