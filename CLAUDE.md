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
no rebase, no `git stash` — the hooks fix files in place. It is a local
reference only, and it stays on `main`.

Reading it is fine, but `git fetch` moves `refs/remotes/origin/main` and
leaves the work tree where it was, so a `grep` or a `Read` against the
checkout answers for whenever it was last brought forward, not for now.
The read that cannot go stale is `git show origin/main:<path>`: it
answers from the ref `git fetch` just moved, never from the tree.

Where the checkout has to be current rather than merely readable, a
fast-forward of a clean `main` brings it up:

```shell
git fetch origin && git merge --ff-only origin/main   # clean main only
```

That writes no commit, switches no branch and runs no hook, so it is on
the permitted side of *never work in it*, not an exception to it. Stop
if the checkout is not on `main` or is not clean: that is no longer
bringing it forward.

**Every session works in a worktree**, its own, from the first edit,
named `wt-<tracker>-<issue>-<repo>-<role>` rather than after the issue
alone. `tracker` is the repository whose issue tracker holds the issue:
an issue number is unique only within one tracker, so
`btclib-org/.github#45` and `btclib-org/btclib#45` are different issues
that would otherwise name the same worktree. `issue` is what prevents
the collision that has actually happened — two worktrees of different
work sharing a generic basename in one repository's own `.git`, keyed on
its path's basename. `repo` prevents a different collision, a *path*
one rather than a `.git` one: two repositories each keep their own
`.git/worktrees/<basename>` and cannot collide there, but the workers of
one session share one scratchpad directory, so a session carrying one
issue into several repositories computes the same target path for each
of them, and `git worktree add` refuses a directory that already
exists — or worse, a second worker reads the first one's tree; naming it
this way also sorts every worktree of one issue together. `role` covers
the narrower case of a coder and its reviewer holding a worktree at
once, which the ordinary sequence avoids by each removing its own.

```shell
WT=<scratchpad>/wt-<tracker>-<issue>-<repo>-<role>  # wt-github-255-btclib-coder
git worktree add -b <branch> "$WT" origin/main
cd "$WT"                     # uv sync --locked only to run something
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

- **A script that imports is not a script that runs, and the gate only
  asks the first question.** mypy resolves the names; whether the
  demonstration still prints what the lecture shows is answered by
  `uv run python py-scripts/<name>.py` and by reading the output.
  `py-scripts/README.md` names what a script wants before it will run at
  all: a line on stdin, a display, or the network.
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
