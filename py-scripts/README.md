# Warning

The Python scripts in this folder depend on the
[btclib](https://github.com/dginst/btclib) library, and on the other
packages `pyproject.toml` declares. `uv sync`, run from the repository
root, is what builds an environment holding all of them:

```shell
uv sync
uv run python py-scripts/conversions.py
```

**Most of these scripts do not run against the btclib that installs
today.** They import names from its 2020 layout, and the library no
longer answers to them, so an import fails before the first line of the
demonstration. Which scripts:

```shell
grep -lE "btclib\.(curvegroup2|curvegroup|dh)|\
btclib\.ecc\.(curve|der|number_theory|sec_point)" py-scripts/*.py
```

`uv run --group lint mypy py-scripts` reports the same thing one line per
import. Read them as source until somebody migrates them.
