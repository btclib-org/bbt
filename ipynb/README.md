# Jupyter Notebook folder

Four notebooks, each carrying the outputs of a run, and what that
promises is not the same for all four.

Three of them are **transcripts**: executing the file reproduces every
output stored in it, byte for byte, so what a reader sees on GitHub
without running anything is what they get when they run it.

| notebook | what it shows |
| --- | --- |
| `DSA.ipynb` | ECDSA over secp256k1, signed and verified by hand |
| `SSA.ipynb` | BIP340 Schnorr, the same way |
| `field_table.ipynb` | opposites, inverses and square roots in Z/79Z |

The first cell of `DSA.ipynb` and `SSA.ipynb` installs btclib and carries
no output on purpose. `!pip install --upgrade btclib` answers one thing
on Colab, another in an environment built with `pip`, and
`command not found: pip` in the one `uv sync` builds, so anything stored
there would describe the reader's machine rather than the material. That
cell is provisioning; the transcript is everything after it.

`PartialHashInversion.ipynb` is an **illustration**, and cannot be a
transcript. Its first cell calls `input()` twice, for a string and for a
number of leading zeros, so nothing executes it without a person at the
keyboard — run headless it raises `StdinNotImplementedError` before it
computes anything. What it then prints is how long the search took and
how many hashes a second this machine managed, over two matplotlib
figures. Its committed output is one run on one machine, kept because
the shape is the point and not because the numbers will come back: the
counts fall by roughly a factor of sixteen for each additional leading
zero, `[111676, 6834, 446, 26, 1]`, which is what the second chart plots
on a base-16 log scale.
