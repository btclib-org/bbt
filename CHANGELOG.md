<!-- markdownlint-disable MD022 MD032 -->
<!-- This file is merge=union, so a rebase joins two sections and drops
     the blank line between them without a conflict: the rule is off
     here for the duration of btclib-org/.github#33, and goes back on
     when that queue is empty. btclib-org/.github#138 is the record. -->

# Changelog

What changed in this repository, and why. Nothing here is released —
`RELEASING.md` says what that means and what it costs — so the entries
are grouped by subject rather than by version.

## Unreleased

### The repository carries the organization's shape

- **The files the standard's section 2 names, which this tree had none
  of**: `AUTHORS.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `COPYRIGHT`,
  `RELEASE_NOTES.md`, `RELEASING.md`, `REPOSITORY.md`, `REVIEWING.md`,
  `SECURITY.md`, `.gitattributes`, `.python-version` and the shared
  linter configurations. `CONTRIBUTING.md` existed and said in its own
  words what the standard says once; what is left of it is under
  `## This repository in particular`, which is the heading the comparison
  stops at.

- **`LICENSE` loses its year range and gains its title.** `COPYRIGHT`
  names the holder without a year, so the two would have disagreed the
  first January nobody remembered.

- **`REPOSITORY.md` is measured, not copied.** Every setting in it is the
  `gh api` call that reads it back and the answer that call gave; one of
  those answers is that `main` has no required status check, so the lint
  workflow this change adds gates nothing until the rule is created.

### One `pyproject.toml` in place of five files

- **`.flake8`, `.isort.cfg`, `mypy.ini`, `requirements.txt` and
  `requirements-dev.txt` are gone.** What each said that is still true
  moved into `pyproject.toml`: the complexity bound `.flake8` carried
  commented out, the 80 columns it asked for — kept on the prose, where
  it still holds — and `mypy.ini`'s two display settings. `black`,
  `flake8`, `isort` and `pylint` became ruff, which is the substitution
  every repository of the organization has already made, and `pip` and
  `wheel` became uv's business.

- **`requirements.txt` named `matplot`**, a different project on PyPI
  from the `matplotlib` this tree imports, and left out `requests`, which
  `py-scripts/getutxo.py` imports. The dependency list is read off the
  tree now.

- **The ruff `select` list is what answers zero over this tree today.**
  It is much shorter than the organization's, and each family left out
  carries the count it reaches and the command that re-derives it: no
  Python here had ever been through ruff, and closing those counts is a
  rewrite of the material the course is taught from rather than a lint
  fix. `ruff-format` is left out for the same reason.

- **No mypy hook.** `uv run --group lint mypy py-scripts` answers with
  errors that are mostly `import-not-found` against modules current
  btclib does not have: the scripts were written against its 2020 layout.
  That is code that no longer runs, not a typing gap, so the
  configuration records it and no hook fails on every commit over it.

### A gate that runs on a pull request

- **`.pre-commit-config.yaml` and `lint.yml`.** The tree had neither, so
  the linters it did configure ran only where somebody chose to run them.
  The hooks are the ones with a subject here — markdown, yaml, jsonc,
  toml, the text files, the notebooks as json, secrets, ruff — and
  `lint.yml` runs that file rather than a second list of the same tools.

- **`pretty-format-json` and `ruff-format` are deliberately absent.**
  Either would rewrite every notebook in `ipynb/`, outputs and embedded
  images included, to settle a formatting nobody reads.

- **The two entropy plugins are off in `.secrets.baseline`.** A scan with
  them on reports findings in the BIP32 test vectors, the derived WIF
  keys and the txids in the regtest walk-through, none of them a
  credential — and each new vector would be another baseline edit, which
  is how a baseline stops being a list anybody reads.

### The tree is what the gate asks for

- **The markdown is wrapped at the width the shared `.markdownlint.jsonc`
  sets**, fenced blocks carry a language, and the image links in
  `lab-tutorial/01.md` are `./`-prefixed as the `local-link-prefix` hook
  requires. No step and no command changed; what changed is where the
  lines break.

- **The scripts open with the notice `COPYRIGHT` holds, and with nothing
  above it.** They carried btclib's pre-MIT header instead: a restriction
  `LICENSE` does not impose, a year range neither licence file carries,
  and a claim that the file is part of a package this tree is not. `CPY`
  is selected now, with the `notice-rgx` the siblings carry, so the
  header is checked rather than copied from a neighbour.

  What the rule's anchor costs is the shebang, no pattern anchored at
  byte zero matching a file that keeps one — and the interpreter it
  declared is not one these scripts run under. `#!/usr/bin/env python3`
  resolves off PATH, where `python3 -c "import btclib"` fails, while
  `py-scripts/README.md` documents `uv run python
  py-scripts/<name>.py`, which consults no shebang. So the shebang goes,
  and the executable bit `check-shebang-scripts-are-executable` pairs
  with it. What that costs is measured rather than assumed:
  `./py-scripts/conversions.py` ran and does not any more, while a script
  importing btclib never ran that way to begin with.

- **The notebooks are ignored for that rule.** Where a notice belongs in
  a `.ipynb`, or whether one does, is a question of its own —
  btclib-org/bbt#27 — and `ipynb/field_table.ipynb` is the only notebook
  ruff reads at all — btclib-org/bbt#26 — so selecting the rule over
  them would settle the first by accident of the second.

- **`typos` corrupted a vector before it was configured**, and that
  is why `[tool.typos]` exists: run with `--write-changes` it rewrote a
  BIP32 xprv and xpub in `py-scripts/bip32_testvector*.py` and a Colab
  cell id in two notebooks. Each token is named in `pyproject.toml` with
  the string it belongs to, rather than the files being excluded, so the
  next vector that trips the checker is an edit somebody makes on
  purpose.

- **`uv.lock` is tracked.** It is not there because anything asked for a
  pinned resolution: `uv sync` writes it whether or not it was asked to,
  so an untracked lock is a dirty tree after the first documented command
  a session runs. Section 1 asks for it committed anyway, and the
  `uv-lock` hook is what keeps it in step with `pyproject.toml`.

### What the organization keeps once, this tree stops keeping twice

- **`claude-review.yml`.** The file every sibling carries, taken from
  btclib-org/.github and differing only where this tree does — there is
  no package, no suite and one gating workflow — so a pull request here
  gets the ack of record a landing reads instead of its author's own,
  which was [btclib-org/bbt#29](https://github.com/btclib-org/bbt/issues/29).
  Its check is red when no ack names the head, and it is not required:
  `REPOSITORY.md` says why it must not become one.

- **`CODE_OF_CONDUCT.md` is gone.** It was a pointer to the PSF code of
  conduct, byte for byte the copy btclib-org/.github keeps, and GitHub
  shows that copy for a public repository that carries none; section 14
  of the standard stopped listing it for that reason
  ([btclib-org/.github#123](https://github.com/btclib-org/.github/issues/123)).

- **`SECURITY.md` is gone, and its limitations are in `README.md`.** The
  policy is conditional on publishing and this tree publishes nothing,
  so what is shown at `security/policy` is the organization's. What an
  inherited file cannot state — the private key `lab-tutorial/01.md`
  publishes on purpose, the scanner that does not see it, the seeded
  `random` in the `speedup_*` scripts — is under *Limitations, not
  vulnerabilities* in `README.md`, where somebody about to follow the
  material reads, rather than behind a reporting form
  ([btclib-org/.github#116](https://github.com/btclib-org/.github/issues/116)).
