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
- `calc/` and `excel/` — the same spreadsheets in two formats, which is
  why a change to one is a change to both.
- `pyproject.toml` — the whole tool configuration, and `README.md` points
  at the course page the slides live on.

The slides themselves are not here. <http://www.ametrano.net/bbt/> is
where they are, so a question about what the course *says* is not one
this tree can answer.

## The primary checkout is the maintainer's

**Never work in it.** No edit, no `git add`, no commit, no branch switch,
no rebase, no `git stash` — the hooks fix files in place. Reading it is
fine, and so is `git fetch`, which writes refs and leaves the work tree
alone.

**Every session works in a worktree**, its own, from the first edit:

```shell
WT=<scratchpad>/wt<issue>
git worktree add -b <branch> "$WT" origin/main
cd "$WT"                              # uv sync only to run something
# edit, gate and commit here, then
git push origin HEAD:refs/heads/<branch>
git worktree remove --force "$WT"     # removing it is part of finishing
```

**Never `git stash` in a worktree either: `refs/stash` is shared.** A
worktree isolates files, not refs, so `git stash push` pushes onto the
same stack every other session pops from. Commit to your own branch
instead.

**Do not rewrite `refs/heads/main`, or advance it with work that is not
yours.** Your own branch is what you push, and the pull request is what
moves `main`.

## Model

The default model for this repository is Sonnet. Switch to Opus only for
a change that has to weigh an argument — what the material teaches, a
convention this tree and the standard disagree about. Use `/model opus`
for the session, then switch back.

Do not use Fable unless explicitly instructed.

## Non-obvious facts that will otherwise waste a session

- **The scripts do not run against the btclib on PyPI.** They import
  `btclib.ecc.curve`, `btclib.curvegroup`, `btclib.curvegroup2` and
  `btclib.dh`, which are names from its 2020 layout and are not names the
  library answers to now. So a script is source to read, not a command to
  run, until somebody migrates it — and a session that "verifies" one by
  running it will report an ImportError as its own doing.
  `pyproject.toml`'s `[tool.mypy]` carries the measurement and the
  command.
- **`pyproject.toml` is not a distribution's.** `package = false`, no
  build backend and no wheel, so the standard's section 3 describes a
  file this one is not. Its ruff `select` is short *on purpose* and every
  family left out carries the reason and the command: adding one back is
  a claim that the tree now answers zero to it, which is a measurement
  and not an edit.
- **The gate is a `uvx` although `uv.lock` is tracked.** pre-commit is
  in no dependency group, so there is no project environment for
  `uv run --only-group lint pre-commit` to resolve it from. A session
  that moves the gate to the sibling form has also changed what
  `CONTRIBUTING.md` and `lint.yml` say, in the same commit.
- **`uv sync` writes `uv.lock` whether or not it was asked to**, so run
  it as `uv sync --locked` unless moving the lock is the point. That is
  the trap this tree fell into: the lock is tracked because the first
  documented command a session runs would otherwise leave the tree
  dirty.
- **A notebook carries its outputs**, so a cell edited without a re-run
  leaves a figure answering an earlier question. `check-json` asks only
  that the file still parses, and nothing here asks the other question.
- **`calc/` and `excel/` are binaries** and a diff of one says nothing.
  A change to a spreadsheet is verified by opening it.
- **This repository is a fork**, so its history reaches back past the
  fork point and its contributor graph carries authors who never pushed
  here. `AUTHORS.md` says so.

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
