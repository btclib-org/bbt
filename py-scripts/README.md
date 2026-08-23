# Running these scripts

The Python scripts in this folder depend on the
[btclib](https://github.com/btclib-org/btclib) library, and on the other
packages `pyproject.toml` declares. `uv sync`, run from the repository
root, is what builds an environment holding all of them:

```shell
uv sync
uv run python py-scripts/conversions.py
```

Each script prints what it computes and exits. What a reader should know
before running one:

- `curves.py` and `rfc6979.py` demonstrate nothing. They generate data
  files for btclib and write them into a checkout of it beside this one,
  at `../../btclib/btclib/data` and `../../btclib/btclib/tests/test_data`.
  btclib has neither path —
  `gh api "repos/btclib-org/btclib/git/trees/main?recursive=1"` is what
  says so — and both scripts raise `FileNotFoundError` whether or not the
  sibling checkout is there;
- `hash_puzzle.py` reads a string and a number of leading zeros from
  stdin, taking a documented default for an empty line, and then opens
  matplotlib windows. `MPLBACKEND=Agg` is what runs it without a display;
- `ec_explorer.py` searches every curve over each prime it lists, which
  takes minutes, and prints only once a prime is done;
- the `speedup_*.py` scripts are benchmarks: they print ratios, so what
  they answer depends on what else the machine is doing;
- `getutxo.py` queries blockchain.info, so it needs the network.
