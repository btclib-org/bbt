if not exist "%APPDATA%\Bitcoin\regtest_Alice" mkdir "%APPDATA%\Bitcoin\regtest_Alice"
start bin\bitcoin-qt.exe -regtest -datadir="%APPDATA%\Bitcoin\regtest_Alice" -server -rpcallowip=127.0.0.1 -txindex -uacomment=Alice -addresstype=bech32 -walletrbf -fallbackfee=0.0002
::start cmd /k cd bin
