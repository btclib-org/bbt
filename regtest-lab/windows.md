# Bitcoin Core Setup (Windows)

1. Download Bitcoin Core's portable zip from
   <https://bitcoincore.org/bin/bitcoin-core-31.1/bitcoin-31.1-win64.zip>
   and unzip it in your favorite location; in the following
   `C:\your\bitcoinfolder` is where the `bin`, `libexec` and `share`
   folders are located.

   Before unzipping, check it against the release's
   [SHA256SUMS](https://bitcoincore.org/bin/bitcoin-core-31.1/SHA256SUMS)
   as
   [Verify your download](https://bitcoincore.org/en/download/#verify-your-download)
   shows for Windows, and stop if the checksums differ.

1. add the `C:\your\bitcoinfolder\bin folder` (the one including the
   `bitcoin-qt`, `bitcoind` and `bitcoin-cli` executables) to your %PATH%
   environment variable, so that whenever you will call the bitcoin
   executables from the command line, Windows will know where to find
   them even if you are not in the `c:\your\bitcoinfolder\bin` folder.
   You can do this
   [permanently](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho),
   or for each command prompt window

    ```bat
    > ECHO %PATH%
    > SET PATH=%PATH%;c:\your\bitcoinfolder\bin
    > ECHO %PATH%
    ```

1. open a command prompt window (with the `C:\your\bitcoinfolder\bin`
   augmented PATH) and start the Bitcoin Core GUI+daemon in regtest mode:

   ```bat
   > if not exist "%APPDATA%\Bitcoin\regtest_Alice" ^
       mkdir "%APPDATA%\Bitcoin\regtest_Alice"
   > bitcoin-qt -regtest -datadir="%APPDATA%\Bitcoin\regtest_Alice" ^
       -addresstype=bech32 -walletrbf=1 -server -rpcallowip=127.0.0.1 ^
       -fallbackfee=0.0002
   ```

   Do not be scared by the alert about >160GB being required. This would
   be true only if you launch Bitcoin Core for mainnet, as it would try
   to download the whole blockchain. Be sure you are launching
   **regtest**: that one will require almost no space.

1. in the GUI open the console (Window | Console) type

   ```text
   getblockcount
   ```

1. to really experiment beyond easy commands, the genuine command line
   `bitcoin-cli` is a better experience than using the GUI console.
   `bitcoin-cli` can be used along with the GUI just opening another
   command prompt window (with the `C:\your\bitcoinfolder\bin` augmented
   PATH) and using it, e.g.:

    ```bat
    > bitcoin-cli -regtest -datadir="%APPDATA%\Bitcoin\regtest_Alice" ^
        getblockcount
    ```

You should now be ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network*, close
Bitcoin Core, wait until the window saying *Do not shut down the computer
until this window disappears* has gone, and *clear the regtest data
folder* the launch command above set with `-datadir`:

```bat
> rmdir "%APPDATA%\Bitcoin\regtest_Alice" /s /q
```

For convenience the
[regtest-18444-start-Alice.bat](./windowsbat/regtest-18444-start-Alice.bat)
and
[regtest-18444-reset-Alice.bat](./windowsbat/regtest-18444-reset-Alice.bat)
batch files are provided to respectively launch and reset the regtest
network, without tweaking with the %PATH% environment variable: put the
batch files into `c:\your\bitcoinfolder` rather than unpacking Bitcoin
Core into this repository's `windowsbat` folder. Close a node as above
before running its reset file.

One can start multiple nodes, as separate instances of the bitcoin
GUI+daemon, on the same machine: each node must use a different p2p port
and data folder to avoid conflicts. For convenience the
[regtest-18555-start-Bob.bat](./windowsbat/regtest-18555-start-Bob.bat)
and
[regtest-18555-reset-Bob.bat](./windowsbat/regtest-18555-reset-Bob.bat)
batch files are provided to respectively launch and reset Bob's node,
while
[regtest-18666-start-Carol.bat](./windowsbat/regtest-18666-start-Carol.bat)
and
[regtest-18666-reset-Carol.bat](./windowsbat/regtest-18666-reset-Carol.bat)
batch files are provided to launch and reset Carol's node. Every node
(Alice 18444, Bob 18555, and Carol 18666) has its own wallet and can
interact with the other nodes generating blocks which are broadcasted to
the network and sending/receiving regtest-bitcoins. Bob's and Carol's
nodes are driven from their own GUI console (Window | Console), neither
passing `-server` for a second `bitcoin-cli` prompt to reach.
