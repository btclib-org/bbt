<!-- markdownlint-disable MD022 MD032 -->
<!-- This file is merge=union, so a rebase joins two sections and drops
     the blank line between them without a conflict: the rule is off
     here for the duration of btclib-org/.github#33, and goes back on
     when that queue is empty. btclib-org/.github#138 is the record. -->

# Changelog

What changed in this repository, and why. Nothing here is released —
`CONTRIBUTING.md`'s *A version, and no release* says what that means and
what it costs — so the entries are grouped by subject rather than by
version, and there are no release notes for this file to be the record
behind.

## Unreleased

### The material runs, and mypy is the gate that says the names resolve

- **Every script under `py-scripts/` and every notebook under `ipynb/`
  imports what btclib exports.** `btclib.ecc.curve` is
  `btclib.curves.curve`, `btclib.curvegroup` and `btclib.curvegroup2` are
  `btclib.curves.curve_group` and `btclib.curves.curve_group_2`,
  `btclib.ecc.number_theory` is `btclib.number_theory`, `ansi_x9_63_kdf`
  moved from `btclib.dh` to `btclib.kdf`, `b58encode` and `b58decode` are
  `base58.encode` and `base58.decode`, and many of the group-law
  helpers a benchmark reaches into carry a `_var` suffix. An import that resolves
  is not a demonstration that works, so each script was run and its
  output read: `uv run python py-scripts/<name>.py`. `curves.py` and
  `rfc6979.py` exit 1 still, writing as they do into a checkout of btclib
  at paths it does not have, which is btclib-org/bbt#17.

- **The `mypy` hook runs the type check `[tool.mypy]` configures.** The
  strictness was declared and read by nothing, which is the finding
  section 15 of the standard names on its own. The hook is section 4's
  local shape — `uv run --locked --no-default-groups --group lint mypy
  py-scripts`, against the environment the scripts import btclib from —
  rather than the mirror, whose `--ignore-missing-imports` would have
  turned every moved module into `Any` and reported a clean run over code
  that could not import. `ci:`'s `skip:` names it, uv being absent on
  pre-commit.ci.

- **The annotations strict mode asks for are at the `def` that needs
  one**, in `ec_explorer.py` and `pubkey2address.py`. `hash_puzzle.py`'s
  `# type: ignore` on the matplotlib import is gone: matplotlib ships a
  `py.typed`, so the ignore silenced nothing and strict mode reported it.

- **`PartialHashInversion.ipynb` passes `base` to `yscale`, not
  `basey`.** matplotlib answers the second with a `TypeError` naming the
  first, which is the one failure in `ipynb/` that was not btclib's.

- **The notebooks' committed outputs were not re-run.** They are what the
  lecture produced, and what re-running them would change is
  btclib-org/bbt#19.

### This tree answers the rows the standard's suite held against it

- **`REVIEWING.md`'s *The gates are the evidence* excepts no gate from
  the run a reviewer may rely on, the test suite included.** The
  organization's copy, shared half byte for byte (section 14): a run is
  whole whoever makes it — never a module on its own, a `-k`, a `--lf`,
  a deselect or a marker in its place — and one that was narrowed or cut
  short is reported as no run (btclib-org/.github#168).

- **`.github/dependabot.yml` exists, watching `github-actions` and
  `uv`, and `check-dependabot` validates it.** `REPOSITORY.md` recorded
  the file's absence as a gap: this tree pins its actions to commit SHAs
  and commits a `uv.lock`, and nothing moved either. Weekly on Thursday
  with the seven-day cooldown, grouped, as section 11 asks; the file's
  header says why no sentinel pre-validates what it opens. The gate runs
  section 4's `check-dependabot` over it, `check-yaml` alone reading the
  file as yaml and not as what it is. The cell `tests/dependabot_test.py`
  reported on this repository against btclib-org/.github#107 goes from
  the backlog.

- **`pretty-format-json` runs, over the hand-written json and not the
  notebooks.** The hook was declined for what it would do to `ipynb/`,
  and that reason holds for the notebooks alone: `.claude/settings.json`
  is json written by hand, which is the hook's subject, and prettier —
  a yaml and jsonc formatter by its own name — had it for want of the
  hook that formats json. The cell `tests/hooks_test.py` reported on
  this repository against btclib-org/.github#130 goes from the backlog.

- **The gate runs `toml-comment-width` and `decoded-subprocess-encoding`.**
  Section 4 lists both among the local hooks and section 3 names the
  first as what holds a `pyproject.toml`'s comments to 80 columns, and
  `.pre-commit-config.yaml` ran neither: the width was kept by hand, and
  nothing under `py-scripts/` decodes a child process, which is the tree
  in which the first call that does so without naming its encoding is
  refused by nothing. The cell `tests/hooks_test.py` reported on this
  repository against btclib-org/.github#134 goes from the backlog.

### The repository carries the organization's shape

- **`[tool.mypy]` enables the organization's optional error codes, and
  one of them answered.** The list is the one btclib-org/.github#165
  decides for section 6 of the standard, the same in every repository
  that carries the table. The hook runs mypy since btclib-org/bbt#24, so
  what the codes report is measured rather than deferred:
  `possibly-undefined` refused `py-scripts/hash_puzzle.py`, where the
  report at the end of the script read two names bound only inside the
  loop above it. They are bound before the loop now — what said the loop
  runs was the size of `maxEval`, which is arithmetic and not control
  flow. The rest of the list answers nothing today, which is the point
  of a ratchet.

- **`REVIEWING.md` is the organization's copy.** A review reads the prose
  that stays in the tree, treats a commit message or a pull request's
  body as a finding only where it decides something, and asks a stated
  count, a measurement nothing re-derives, or the history of the code
  told in a comment to go — section 14 of the standard, the shared half
  byte for byte.

- **`RELEASING.md` and `RELEASE_NOTES.md` are gone, and what the first
  said is a section of `CONTRIBUTING.md`.** Section 2 of the standard
  says a tier-2 repository carries neither (btclib-org/.github#150): the
  first opened *Nothing here is released* and the second's one section
  read *Nothing a user has to act on*, and a file whose content is its
  own absence tells a reader who has not opened it that there is a
  procedure here. What the first said — the commands that answer `0`
  releases and `0` tags, what a release would first need, and that
  `tag-integrity` is in place before the first tag and refuses one that
  is not signed — is `CONTRIBUTING.md`'s *A version, and no release*,
  under *This repository in particular*; nothing of the second is lost.
  `README.md` says the material is not released and points there,
  `REPOSITORY.md`'s `tag-integrity` bullet and its *No publishing* bullet
  cite that section where they cited `RELEASING.md`, `pyproject.toml`'s
  comment on the placeholder version does the same, and this file's
  introduction with it. The entry below that lists the two files among
  those the tree gained describes the tree between that landing and this
  one. `.gitattributes` keeps `RELEASE_NOTES.md merge=union`: section 14
  of the standard owes the two `merge=union` entries to every copy, and
  an attribute on a path the tree does not hold is inert.

- **The files the standard's section 2 names, which this tree had none
  of**: `AUTHORS.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `COPYRIGHT`,
  `RELEASE_NOTES.md`, `RELEASING.md`, `REPOSITORY.md`, `REVIEWING.md`,
  `SECURITY.md`, `.gitattributes`, `.python-version` and the shared
  linter configurations. `CONTRIBUTING.md` existed and said in its own
  words what the standard says once; what is left of it is under
  `## This repository in particular`, which is the heading the comparison
  stops at.

- **`.gitattributes` is the organization's copy of itself**
  (btclib-org/.github#102). Section 14 names it as the same file in every
  repository, and `tests/verbatim_test.py` there compares the copies it
  finds; this one differed in the comment's closing sentence, which
  named `README.md` as where section 9 is without saying whose. It is
  now byte for byte the copy in `btclib-org/.github`, the two
  `merge=union` lines unchanged under it, and `git check-attr merge`
  still answers `union` for both files.

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

### Three settings that read as checks this tree did not run

- **`[tool.mypy]`'s `show_error_codes` is gone.** mypy 2.3.1, the
  version `uv.lock` pins, already reports a code on every error —
  `hide_error_codes` defaults to `False` before a config file is read —
  so the key bought no check while reading as though it did
  ([btclib-org/.github#191](https://github.com/btclib-org/.github/issues/191)).

- **`.gitattributes` carries the standard's sentence on the two
  `merge=union` lines matching a tree that holds neither file.** This
  tree has no `RELEASE_NOTES.md`, and the copy here now says why that
  is not a mismatch, byte for byte with `btclib-org/.github`'s
  ([btclib-org/.github#192](https://github.com/btclib-org/.github/issues/192)).

- **`select` in `[tool.ruff.lint]` gains `W`, so `max-doc-length = 80`
  gates something.** W505 was configured and never selected; the four
  lines it now catches are rewrapped, and one notebook cell's
  blank-line whitespace, which the wider `W` family also refused, is
  stripped alongside them
  ([btclib-org/.github#176](https://github.com/btclib-org/.github/issues/176)).

### `D` is selected, and every public name now carries a docstring

- **`select` in `[tool.ruff.lint]` gains `D`, and
  `[tool.ruff.lint.pydocstyle]` declares `convention = "pep257"`.**
  Neither was there, so section 5's docstring family reached nothing;
  the convention is what settles ruff's D203/D211 and D212/D213
  incompatible-pair warnings, printed until one is chosen. Measured
  against the tree this declares, every public module under
  `py-scripts/`, `ipynb/field_table.ipynb`'s one function and the four
  public functions `pubkey2address.py` defines now carry one, and the
  five other pydocstyle findings — a summary wrapped in whitespace, two
  missing terminal periods, one non-imperative mood — are fixed at the
  line
  ([btclib-org/.github#177](https://github.com/btclib-org/.github/issues/177)).

- **`det_keychain_type2.py`'s one-line docstring named Type-1.** The
  script derives a Type-2 sequence — a public random number lets each
  child's public key come from the master public key alone, which
  `det_keychain_type1.py` cannot do — and its docstring named the wrong
  one, copied from its sibling and never corrected.
