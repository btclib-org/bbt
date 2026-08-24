# Bitcoin Core Setup (Windows)

1. Download and install Bitcoin Core from
   <https://bitcoincore.org/en/download/>. You can pick one of the
   following two version:
   - portable version (zip)
     <https://bitcoincore.org/bin/bitcoin-core-0.18.0/bitcoin-0.18.0-win64.zip>;
     unzip it in your favorite location; in the following
     `C:\your\bitcoinfolder` is where the `bin`, `include`, `lib`, and
     `share` folders are located
   - regular version (exe)
     <https://bitcoincore.org/bin/bitcoin-core-0.18.0/bitcoin-0.18.0-win64-setup.exe>;
     execute the installer; in the following `C:\your\bitcoinfolder` is
     where the `bin`, `include`, `lib`, and `share` folders are located
     (usually it should be `C:\Program Files\Bitcoin\bitcoin-qt.exe`)

1. add the `C:\your\bitcoinfolder\bin folder` (the one including the
   `bitcoinqt`, `bitcoind`, and `bitcoin-cli` executables) to your %PATH%
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
   > bitcoinqt -regtest -addresstype=bech32 -walletrbf=1 -server -rpcallowip=127.0.0.1
   ```

   Do not be scared by the alert about >160GB being required. This would
   be true only if you launch Bitcoin Core for mainnet, as it would try
   to download the whole blockchain. Be sure you are launching
   **regtest**: that one will require almost no space.

1. in the GUI open the console (Help | Debug Window | Console) type

   ```text
   getblockcount
   ```

1. to really experiment beyond easy commands, the genuine command line
   `bitcoin-cli` is a better experience than using the GUI console.
   `bitcoin-cli` can be used along with the GUI just opening another
   command prompt window (with the `C:\your\bitcoinfolder\bin` augmented
   PATH) and using it, e.g.:

    ```bat
    > bitcoin-cli -regtest getblockcount
    ```

You should now be ready to start the regtest lab session.

Whenever you want *to start with a fresh new regtest network, remember to
clear the regtest data folder* that has been created in the
`%APPDATA%\Bitcoin\regtest` folder:

```bat
> rmdir %APPDATA%\Bitcoin\regtest /s /q
```

For convenience the
[regtest-18444-start-Alice.bat](./windowsbat/regtest-18444-start-Alice.bat)
and
[regtest-18444-reset-Alice.bat](./windowsbat/regtest-18444-reset-Alice.bat)
batch files are provided to respectively launch and reset the regtest
network, without tweaking with the %PATH% environment variable: just put
the batch files in `c:\your\bitcoinfolder`.

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
the network and sending/receiving regtest-bitcoins.
