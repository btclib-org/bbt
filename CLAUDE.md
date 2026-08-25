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
- **`codespell --version` names no release, and `typos --version` names
  one.** pre-commit's first strategy fetches one named ref and checks
  out `FETCH_HEAD`, so the clone carries no local ref for
  `setuptools_scm` to describe and codespell falls back to
  `0.1.dev1+g<sha>`; its fallback fetches `--tags`, and a clone made
  that way has the tag to describe. The field after `+g` abbreviates the
  commit `rev:` resolved to, so that string is evidence of the sha
  rather than of the version, and the pin it appears to contradict is
  honoured. `typos` installs a released package rather than building its
  clone, so of the two spell checkers configured side by side only that
  one says which version ran. What codespell's string does not say, the
  sha does: `sqlite3 ~/.cache/pre-commit/db.db 'select * from repos'`
  maps every pinned `rev:` to its clone, `git -C <clone> rev-parse HEAD`
  is the sha that ran, and the sha the pin names is the last line's
  first field from
  `git ls-remote --exit-code --tags <url> '<ref>' '<ref>^{}'`, whose
  second pattern is what an annotated tag needs and whose `--exit-code`
  makes a ref that is not there a non-zero exit rather than an empty
  answer. Read that last field by eye rather than piping it: a
  `tail`/`cut` pipeline exits zero whatever `ls-remote` did.
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
  `check-json` asks only that a file parses, and nothing here asks
  either of the other two questions.
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
- **`grep` does not measure `ipynb/`.** `grep -c` counts lines, so on a
  notebook written on one line it answers at most 1 however many
  occurrences there are, and cannot say that it could not. An unanchored
  pattern matches the base64 of a committed image as readily as it
  matches code, which is the half that has already produced a wrong
  answer here. Parse the document.
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
