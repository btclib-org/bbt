# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

How to work here — what the issue tracker takes, the prose style, and how
a pull request is opened and landed — is `CONTRIBUTING.md`, which is the
same file in every repository of the organization up to its last section,
which is this tree's and holds the commands and the gates. Repository
configuration is `REPOSITORY.md`: read it before changing a workflow, a
branch rule or a setting. Reviewing is `REVIEWING.md`, and `/review` is
that file as a command; read it before reviewing a pull request and
before opening one, since it is what the pull request will be answered
against.

## Architecture

This is course material, and the material is the product. Nothing here is
built, installed, imported or released; what it ships, it ships by being
read or cloned.

- `lab-tutorial/` — a walk-through of somebody else's software, with the
  screenshots it needs under `image/`.
- `regtest-lab/` — running a private Bitcoin Core network, one page per
  operating system, with the `.bat` launchers under `windowsbat/`.
- `ipynb/` — Jupyter notebooks, outputs committed.
- `py-scripts/` — one script per idea, each run from a checkout and each
  printing what it computes.
- `excel/` — the spreadsheets, generated from `excel/generate.py`: a
  change is made to that file, not to a workbook.
- `pyproject.toml` — the whole tool configuration, and `README.md` points
  at the course page the slides live on.

The slides themselves are not here. <http://www.ametrano.net/bbt/> is
where they are, so a question about what the course *says* is not one
this tree can answer.

## The primary checkout is the maintainer's

Never work in it: no edit, no `git add`, no commit, no branch switch, no
rebase, no `git stash` — the hooks fix files in place. The one write
allowed there brings it forward, and only while it is on `main` and
`git status --porcelain` prints nothing; where it is not, stop:

```shell
checkout=<checkout>
```

```shell
git -C "${checkout:?}" pull --ff-only
```

Read it only after that, once `git -C <checkout> rev-parse HEAD
origin/main` prints one sha twice. A measurement that has to hold at a
named revision reads `git -C <checkout> show <sha>:<path>` instead.

Every session works in a worktree of its own, from its first edit, named
`wt-<tracker>-<issue>-<repo>-<role>` — `wt-github-255-btclib-writer` for
issue 255 of `btclib-org/.github`'s tracker, worked in `btclib` by a
writer. The environment is created there, with the command `CONTRIBUTING.md`
names under *The environment and the gates*. Every path is written out in
full:

```shell
git worktree add \
  <scratchpad>/wt-<tracker>-<issue>-<repo>-<role> origin/main -b <branch>
```

Removing it is part of finishing:

```shell
git worktree remove --force <scratchpad>/wt-<tracker>-<issue>-<repo>-<role>
```

`refs/stash` and the local `main` are shared by every worktree: never
`git stash`, and move `main` only by the fast-forward above.

## Model

Default model: Sonnet; Opus for design decisions with conflicting
constraints. Do not use Fable unless instructed.

## Non-obvious facts that will otherwise waste a session

- **A script that imports is not a script that runs, and the gate asks
  each question with its own tool.** mypy resolves the names;
  `.github/scripts/check_scripts.py`, which `lint.yml` runs, requires
  exit 0. Neither reads what a script prints, so whether the
  demonstration still shows what the lecture shows is answered by
  `uv run python py-scripts/<name>.py` and by reading the output.
  `py-scripts/README.md` names what a script wants before it will run at
  all: a line on stdin, a display, or the network — and
  `check_scripts.py` supplies the stdin `hash_puzzle.py` prompts for and
  a headless matplotlib backend, its own `EXCLUSIONS` naming what it
  does not run and why.
- **`pyproject.toml` is not a distribution's.** `package = false`, no
  build backend and no wheel, so the standard's section 3 describes a
  file this one is not. Its ruff `select` is `["ALL"]`, section 5's
  prescribed shape, and every family it excludes sits in `ignore`,
  `per-file-ignores` or a site `# noqa`, each with its own reason and,
  where the reason is that the tree already answers zero to the rule,
  the command that measures it: removing an entry or narrowing a `noqa`
  is a claim about what the tree answers, which is a measurement and not
  an edit.
- **`uvx ruff check --select ALL .` on the command line is not what the
  gate runs, once `select` is already `["ALL"]` in `pyproject.toml`.**
  The CLI flag overrides the config file's `ignore` list rather than
  adding to it, so it reports every family the config declines as a
  fresh finding. The command that reproduces what `pre-commit`'s
  `ruff-check` hook actually runs is the plain `uvx ruff check
  --preview --statistics .`, with no `--select` override, reading
  `pyproject.toml`'s own `ignore`/`per-file-ignores` as it stands.
- **The extended keys and the WIF in `pyproject.toml`'s `typos` table
  cannot be swapped:** the keys are BIP32's published vectors, and the WIF
  encodes the private key of the Bitcoin wiki's WIF example. `typos` flags
  every BIP32 vector. Re-check with the hook's pinned binary, run
  `--isolated` over each vector's keys from `bip-0032.mediawiki`, since
  `typos` reads `pyproject.toml` from any parent directory.
- **The gates are `uv run` commands over `pyproject.toml`'s groups, and
  only the hooks leave the project out.** They run under
  `--only-group lint`; the notebook gate, the scripts gate, the workbook
  gate and the mypy hook's own entry each get the project with `lint`,
  `notebooks` or `excel`, whichever the gate's own imports need. A
  session that changes how a gate is invoked changes every file spelling
  the command, in the same commit, and
  `git grep -l 'uv run --locked' -- ':!CHANGELOG.md' ':!CLAUDE.md'` is
  what lists them.
- **`uv sync` writes `uv.lock` whether or not it was asked to**, so run
  it as `uv sync --locked` unless moving the lock is the point. That is
  the trap this tree fell into: the lock is tracked because the first
  documented command a session runs would otherwise leave the tree
  dirty.
- **`codespell --version` names no release and `typos --version` does:**
  section 4's spelling bullet of the standard has the mechanism.
  codespell's configuration is its `args:` in `.pre-commit-config.yaml`;
  the only spell checker configuration in `pyproject.toml` is the
  `typos` tables.
- **A notebook carries its outputs, and three of the four are
  transcripts**: `DSA.ipynb`, `SSA.ipynb` and `field_table.ipynb` each
  reproduce every stored output byte for byte when executed, so a cell
  edited without a re-run does not merely leave a figure answering an
  earlier question, it makes the file disagree with itself.
  `PartialHashInversion.ipynb` is the exception and cannot be anything
  else: its first cell calls `input()` twice, so headless it raises
  `StdinNotImplementedError` before computing anything, and what it
  prints is wall clock timings over matplotlib figures. It is an
  illustration, and `ipynb/README.md` is where that is said to a reader.
  `check-json` asks only that a file parses. Whether a transcript
  still reproduces is asked by `.github/scripts/check_notebooks.py`,
  which `lint.yml` runs; whether `PartialHashInversion.ipynb` still
  runs is asked by nothing.
- **The first cell of `DSA.ipynb` and `SSA.ipynb` carries no output on
  purpose**, and executing one is how that gets undone: empty it again
  afterwards. `ipynb/README.md` has why, that being a reader's question
  rather than a session's. Executing also writes an `execution` block of
  wall clock timestamps into each cell's metadata and stamps the running
  interpreter into `language_info`. Strip both, or the file you just
  refreshed stops reproducing itself on the next run.
- **Nor is a notebook a file a diff answers.** `pretty-format-json`
  carries `exclude: \.ipynb$`, so nothing normalises these and they are
  not written alike: `SSA.ipynb` is one line of JSON, and the indent of
  a `source` element is not the same in the others. Each round-trips
  through `json.dumps` losslessly at its own settings, which are not the
  same settings for all of them, so a safe round-trip is one whose
  settings you measured first — more work than a targeted text
  replacement, and silent when you get it wrong. What the replacement
  did is established by parsing both versions and comparing cell by
  cell, which is also how you see that no `outputs` array moved.
- **A rebase conflict on the one-line notebook is the whole file**, and
  markers inside a single line of JSON are not resolvable by anybody.
  Take the new base's copy and re-apply the change to it.
- **`grep` does not measure `ipynb/`**: `grep -c` answers at most 1 on the
  one-line `SSA.ipynb`, and a pattern matches committed images' base64.
  Parse the document.
- **`excel/*.xlsx` are binaries, and a diff of one says nothing** -- but
  the source is `excel/generate.py`, not the workbook, and
  `.github/scripts/check_generated_workbooks.py` gates whether a
  committed workbook is still that script's own output. What no gate
  reads is a chart's own look on screen, so a change to it is still
  verified by opening the workbook.
- **The history is older than this repository**, so the contributor
  graph carries authors who never pushed here. `AUTHORS.md` says so,
  with the command that dates each.

## Conventions to match

Section 9 of [the standard](https://github.com/btclib-org/.github) is the
prose style, and it governs this file too. It is not re-listed here, that
section's own *One fact in one place* being the reason.
`CONTRIBUTING.md`'s *Pull requests* has what a title does with the issue
it closes, and its *The issue tracker* has what belongs here rather than
in the standard's tracker.

What is left to this file is what those cannot say, because it is about a
session rather than about the tree: the worktree rule, the model, the
failure modes in the section that names them, and what this tree is.

## Verifying

Run the command as documented before claiming it works, and read its exit
code rather than its filtered output, for the reason `CONTRIBUTING.md`'s
*This repository in particular* gives. Every claim in this file was
checked against the tree, and the tree changes.
