# Running these scripts

The Python scripts in this folder depend on the
[btclib](https://github.com/btclib-org/btclib) library, and on the other
packages `pyproject.toml` declares. `uv sync --locked`, run from the
repository root, is what builds an environment holding all of them:

```shell
uv sync --locked
uv run python py-scripts/conversions.py
```

Each script prints what it computes and exits. What a reader should know
before running one:

- `hash_puzzle.py` reads a string and a number of leading zeros from
  stdin, taking a documented default for an empty line, and then opens
  matplotlib windows. `MPLBACKEND=Agg` is what runs it without a display;
- `ec_explorer.py` searches every curve over each prime it lists, which
  takes minutes, and prints only once a prime is done;
- the `speedup_*.py` scripts are benchmarks: they print ratios, so what
  they answer depends on what else the machine is doing.
