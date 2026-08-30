# Changelog

What changed in this repository, and why. Nothing here is released —
`CONTRIBUTING.md`'s *A version, and no release* says what that means and
what it costs — so the entries are grouped by subject rather than by
version, and there are no release notes for this file to be the record
behind.

## Unreleased

### The sentinel goes with its badge, and `links` follows the calendar

- **`.github/workflows/scorecard.yml` is gone** (issue
  btclib-org/.github#492). Section 10 of the standard records which
  trees carry which sentinel, and the badge and the workflow are one
  membership rather than two: the `scorecard` entry does not name this
  repository, and `README.md` carries no Scorecard badge.
- **`REPOSITORY.md` reads no obligation off this repository being no
  fork** (issue btclib-org/.github#492). Public and not a fork is the
  bar that sentinel asks rather than what gives a tree one, so what the
  answer settles here is that the record's silence is the whole of the
  reason; neither *Required checks on main* nor *Token permissions*
  names a workflow the tree does not hold.
- **`REPOSITORY.md`'s *Token permissions* names both elevations
  `claude-review.yml`'s jobs take** (issue btclib-org/.github#492).
  `pull-requests: write` posts the comment and `id-token: write` is for
  the OIDC token the action mints during its own startup.
- **`README.md`'s badge comment gives section 2's three groups, and
  which sentinels this tree carries is read off the record** (issue
  btclib-org/.github#492). The badge order over the sentinels is the
  calendar order, so the row and the schedule are one decision.
- **`.github/workflows/links.yml` carries the day and the hour section
  10 gives `links`, at this repository's own minute** (issue
  btclib-org/.github#480).
- **`.lycheeignore`'s Stack Overflow entry weighs the cadence rather
  than the weekday** (issue btclib-org/.github#480). What would teach a
  reader to stop reading `links.yml`'s output is a rot report every
  week, whichever day the calendar puts it on.

### The keywords are the GitHub topics, in a tree that publishes nothing

- **`pyproject.toml` declares `keywords`, and they are this
  repository's GitHub topics** (closes #2). Section 3 of the standard
  has the two lists be the same names in the same lowercase spelling.
  It writes no publishing condition on that, where it writes one
  explicitly for `name` and for `license-files`, so the reading taken
  here is that a tree with nothing to upload owes the list all the same
  — a reading, and btclib-org/.github#465 is where the standard is
  asked to say so in as many words. The comment above
  the block gave no upload as the reason there were no keywords, and
  gives instead what the topics do, which is let a reader of
  github.com/btclib-org find course material.
- **`REPOSITORY.md`'s *Features* reads the topics back and records no
  divergence in them** (closes #2). The reason it gave for the empty
  array — that a tree shipping no package has no keyword list for the
  topics to be read against — is gone rather than moved, since it is the
  reason the standard's rule does not take; what nothing being shipped
  still decides is the classifiers, the urls and the license expression,
  and that sits in `pyproject.toml` beside the keywords.

### The review job's fork condition argues from what the secret turns on

- **`.github/workflows/claude-review.yml`'s job header gives a ground
  for comparing `full_name` that does not turn on this repository being
  a fork** (closes #3). What withholds the secret is the head repository
  not being this one, where `.fork` asks whether the head repository has
  a parent; the two part on a repository that is itself a fork, whose
  own branches are handed the secret and answer `.fork` true, and
  `gh api repos/btclib-org/bbt --jq .fork` answers `false`, so here they
  decide alike and a swap between them would show up in no run. The
  lines this replaces are the ones every copy of that workflow carries —
  `grep -c 'itself a fork'` answers 1 in each of the eight — which is
  what makes the restated ground a question for all of them and not
  only for this tree (issue btclib-org/.github#456).

### The fork prose is replaced or dropped, and reporting is read back

- **`AUTHORS.md` explains the contributor graph from the age of the
  history rather than from a fork point** (issue #3). The graph carries
  authors who never pushed here because the history is older than the
  repository — `git log --format=%ad main | tail -1` dates the first
  commit and `gh api repos/btclib-org/bbt --jq .created_at` dates the
  repository — where the call the file handed a reader,
  `gh api repos/btclib-org/bbt --jq .parent.full_name`, exits `0` and
  prints an empty line.
- **`CLAUDE.md`'s bullet states that same fact and keeps its pointer at
  `AUTHORS.md`** (issue #3). The two move together, one holding the
  commands and the other the pointer.
- **`lint.yml`'s concurrency comment keeps the design and drops the
  example under it** (issue #3). Keying the group on the pull request's
  number rather than on `github.head_ref` is what survives two pull
  requests whose head branches carry one name, which the sentence above
  the example gives; what the example added was how ordinary that
  collision is here, and the design does not turn on how ordinary it is.
- **`links.yml` keeps its pointer at `lint.yml`'s group and drops the
  half it repeated** (issue #3). A pointer is the whole of what that
  comment needs, the reason being one file's to state.
- **`REPOSITORY.md`'s *Secret scanning and Dependabot* reads private
  vulnerability reporting back** (closes #4). `gh api
  repos/btclib-org/bbt/private-vulnerability-reporting` answers
  `{"enabled":true}`; the standard gives the policy file to tier 1 and
  this setting to every tier, and this tree carries no `SECURITY.md` of
  its own, so the button the organization's policy sends a reporter to
  is what this setting puts on the Security tab here.
- The fifth place issue #3 names,
  `.github/workflows/claude-review.yml`, is not touched here and that
  issue stays open. Its comment prefers `full_name` to `.fork` from an
  example that has retired, so the ground for the preference wants
  restating rather than deleting, and the same comment is in every copy
  of that workflow — tracking issue: btclib-org/.github#456.

### This repository is not a fork, so it runs the Scorecard sentinel

- **`.github/workflows/scorecard.yml` runs the OpenSSF Scorecard on
  every push to `main` and on Saturday at 03:32 UTC** (issue #2).
  Section 10 of the standard keys that sentinel on a repository that is
  public and is not a fork, and `gh api repos/btclib-org/bbt --jq
  '.fork, .private'` answers `false` to both; the day and the hour are
  the `scorecard` row of that section's calendar and the minute is this
  repository's row of the table beside it. The workflow carries no
  `workflow_dispatch` and no `pull_request`, its triggers being
  `ossf/scorecard-action`'s own, which is the one exception section 10
  states to its own trigger rule.
- **`README.md`'s badge row gains the OpenSSF Scorecard badge, after
  `links`** (issue #2). The sentinels sit in section 10's calendar
  order, where the `links` row is Monday and the `scorecard` row is
  Saturday.
- **`REPOSITORY.md` reads the fork answer back as `false` and says what
  that decides here** (issue #2). It decides the sentinel above and
  nothing else: the divergences from the sibling repositories recorded
  further down — the wiki, the projects board, the empty `topics` —
  are each argued from what this tree holds, where a parent repository
  was never part of the argument. *Required checks on main* names
  `scorecard.yml` as a workflow no branch rule could require, `push`
  and `schedule` being its only triggers, which is a reason of a
  different kind from the two that section already carries; and *Token
  permissions* names the analysis job's `id-token: write` and
  `security-events: write` beside `claude-review.yml`'s
  `pull-requests: write`, the elevation-per-job rule now having more
  than one instance to point at.
- One of the issue's checkboxes is a setting rather than a file and
  stays open here: `gh api repos/btclib-org/bbt --jq '.topics | length'`
  answers `0`, which is the divergence `REPOSITORY.md` records with its
  own reason — an argument that the divergence is justified, not that
  the box is ticked. So the entry above cites that issue and does not
  close it.

### `REVIEWING.md` converges on the standard's current verdict, with `NACK`

- **`REVIEWING.md`'s *The verdict* converges on the standard's current
  text, with `NACK` as a third verdict alongside `ACK` and
  `CHANGES REQUESTED`** (issue #98). The ack of record is posted as a
  review of type COMMENT, never a forge approval; this tree's own copy
  argued only from the refusal of a self-approval, which never covered
  the workflow's own verdict. The issue's other checkbox, the
  workflow's own ack becoming a review, stays open here:
  `anthropics/claude-code-action` cannot submit an approving review by
  design, and the credential such a step would need is an
  organization-level decision outside this tree.

### `lint.yml` and `CLAUDE.md` name what actually pins each hook

- **`lint.yml`'s cache-key comment says what pins each pre-commit
  environment: a `rev:` for most of them, `additional_dependencies` for
  the two `typos` hooks** (closes #110). The comment argued from `rev:`
  alone, which the `typos` hooks left behind when they converged onto
  `repo: local`; the cache key itself already hashes
  `.pre-commit-config.yaml` whole, so what it keys on does not change.
- **`CLAUDE.md`'s codespell-version bullet points at the standard's
  section 4 for the mechanism, rather than restating it** (closes
  #100). The mechanism is pre-commit's own fetch strategy and not this
  tree's; what stays here is this tree's own `[tool.codespell]` block
  and `typos` word table, re-derived by running the checker.

### What moves each pin is named by category, not counted

- **`.github/dependabot.yml`'s header and `REPOSITORY.md`'s Dependabot
  paragraph say what Dependabot moves, what an autoupdate moves, and
  that a version pinned in a hook's `additional_dependencies` is
  reached by neither** (issue btclib-org/.github#422). `autoupdate`
  walks every `repo:` entry except `local` and `meta`, so the version
  the two `typos` hooks pin moves when a hand edit moves it, which is
  what `CLAUDE.md` says of that pin.
- **Neither text counts what this tree pins.** An ordinal census — two
  things watched, a third somebody else's job — takes an edit for every
  pin written outside a `rev:`, where naming the categories takes none.

### The `typos` hooks are `repo: local`, pinned through `additional_dependencies`

- **`.pre-commit-config.yaml`'s two `typos` hooks no longer name
  `repo: https://github.com/crate-ci/typos` with a `rev:`; both sit
  under `repo: local` and pin the version through
  `additional_dependencies: [typos==1.49.0]`.** `autoupdate` walks every
  `repo:` entry except `local` and `meta`, so a local hook is the one
  shape it cannot reach, where a mirror entry is reachable by the moving
  `v1` alias `crate-ci/typos` re-tags onto each release's commit (issue
  btclib-org/.github#399).
- **Both hooks restate upstream's `stages`**, a local hook inheriting no
  manifest to take them from. Without them the hooks run at every stage,
  and the first of the two carries `--write-changes`: at `commit-msg`
  that is a spell checker rewriting the commit message, where the mirror
  form answers that it has no hook for that stage.
- **`CLAUDE.md`'s two references to the hook's `rev:` name the
  `additional_dependencies` pin instead**, there being no `rev:` left to
  point at, and say that the pin moves only when a hand edit moves it.

### `claude-review.yml`'s `mention` job refuses in its own words

- **The step guarding `mention` is `Refuse to answer without a
  credential` and its message ends `this workflow answers nothing`** —
  that job answers an `@claude` comment and reviews nothing
  (issue btclib-org/.github#402).
- **The comment above that step points at the review job's reason
  rather than restating it** (issue btclib-org/.github#410). The
  restatement narrated a measurement made on the review job — a token
  found empty, a review reported successful — inside the job that
  reviews nothing. Both strings are `portanode`'s, read from its blob.

### `claude-review.yml`'s `claude_args` comment names the subcommands used

- **The comment above `claude_args` names `diff`, `review` and `view`**,
  which is what `grep -n 'gh pr ' .github/workflows/claude-review.yml`
  answers (issue btclib-org/.github#398).

### `claude-review.yml` matches the organization's current copy

- **The `review` and `mention` jobs now run only when the organization
  variable `CLAUDE_REVIEW_ENABLED` is `true`.** The gate sits on each
  job rather than on a step, so a switched-off review skips cleanly
  instead of leaving a red check behind a runner line no step wrote
  (issue btclib-org/.github#364).
- **The guard step that runs after the review step reads
  `api_error_status`, `stop_reason` and the SDK's own `result` text out
  of the execution file** before reporting that the step's outcome was
  not `success`, rather than reporting the outcome alone with the cause
  hidden inside the action's own sanitized log
  (issue btclib-org/.github#385).
- **The verdict is posted as a pull request review of type `COMMENT`**
  (`gh pr review --comment`), never `--approve` or `--request-changes`,
  and the guard that checks for an ack now reads
  `repos/<owner>/<repo>/pulls/<n>/reviews` instead of the issue's own
  comments, matched against the head sha the same way as before. A
  `NACK <sha>` verdict is a third case the guard now reports distinctly
  from `CHANGES REQUESTED <sha>` (issue btclib-org/.github#340).

### `.pre-commit-config.yaml`'s ruff comment says `select = ["ALL"]`

- **The comment above the `ruff-check` hook no longer describes a short,
  zero-finding selection** (closes btclib-org/bbt#104). It names
  `pyproject.toml`'s `select = ["ALL"]` and where each exclusion is
  argued instead.

### `CLAUDE.md` names two traps `select = ["ALL"]` and the union merge left behind

- **`uvx ruff check --select ALL .` on the command line is not what the
  gate runs.** The CLI flag overrides `pyproject.toml`'s own `ignore`
  list rather than adding to it; the command that reproduces the pinned
  `ruff-check` hook is the plain `uvx ruff check --preview --statistics
  .`, with no `--select` override.
- **`CHANGELOG.md` carries no `markdownlint-disable` directive**, so
  `markdownlint-cli2 --fix` repairs the blank line a rebase's
  `merge=union` join eats between two headings, with nothing to restore
  by hand.
- **The `pyproject.toml` bullet in *Non-obvious facts* now says
  `select = ["ALL"]`**, matching what btclib-org/bbt#99 and one checkbox
  of btclib-org/bbt#98 landed.

### `check_notebooks.py` reads every notebook, a raised cell included

- **A code cell that raises no longer stops the run**
  (closes btclib-org/bbt#94). Each notebook's execution sits in its own
  `try`, so a raised cell is collected the way a drifted output is: the
  notebook is reported `raised executing a cell`, next to what raised,
  and the notebooks after it are still read.

- **The `ILLUSTRATIONS` check that reports a missing illustration now
  runs after the transcripts loop**, so it is reported whether or not a
  notebook raised.

### `README.md`'s head carries a badge row, one badge per property

- **The licence, the lint workflow, pre-commit.ci and the `links`
  sentinel, in that order** (issue #98). This tree publishes nothing,
  holds no suite and builds no documentation, so it owes none of the
  badges those properties earn, and `links` is the only sentinel it
  runs. The issue's other checkboxes — `pyproject.toml`'s `select`
  list, `claude-review.yml`'s ack of record and `REVIEWING.md`'s own
  sentence about it — stay open here.

### `pyproject.toml` selects every ruff rule family, not a hand-picked list

- **`select = ["ALL"]`, per section 5 of the organization's standard,
  with every exclusion moved into `ignore` or a `per-file-ignores`
  entry and argued beside it** (issue btclib-org/bbt#98). A hand-picked
  list rots the day ruff ships a family nobody has looked at yet; `ALL`
  brings a new one in on the pull request that bumps ruff's own pinned
  revision instead.

- **The `select` comment no longer claims `D` is left out, or that no
  site carries a docstring** (closes btclib-org/bbt#99). Both halves
  were false: `D` has been selected, and every public module, script
  and notebook cell already carries one, since `01b67d6`. `select =
  ["ALL"]` retires the comment block that line lived in.

- **What `ALL` newly surfaces and does not fit teaching material is
  declined by name, each with the reason beside it**: `print` because a
  script's or a notebook cell's output is the point, `assert` because a
  walkthrough asserts what it just computed, `implicit-namespace-package`
  because no file here is part of a package, `commented-out-code`
  because what it flags is kept for the reader on purpose, `TD` because
  unfinished work belongs in the tracker and none is here, and the
  crypto and Bitcoin notation `pep8-naming` already argues for
  elsewhere in the organization. `py-scripts/ellipticcurves.py`'s table
  of curve literals and the notebooks' own untyped functions each get a
  narrower `per-file-ignores` entry instead.

- **What `ALL` surfaces and is a real finding is fixed where it is
  found**: a bare `except Exception` narrowed to the `ValueError`
  `mod_sqrt_var` actually raises, `requests.get` given an explicit
  timeout, a boolean parameter made keyword-only, and every mixedCase
  name that was not crypto notation renamed to what PEP 8 asks.

### The suppressed spell-checker strings have no substitute

- **`CLAUDE.md` says what fixes the extended keys and the WIF under
  `[tool.typos.default.extend-identifiers]`** (closes btclib-org/bbt#96).
  `py-scripts/bip32_testvector1.py` and `bip32_testvector3.py` are named
  for the BIP32 vectors they walk, their seeds are the ones the BIP
  publishes and every string they assert is a key of that vector; the
  two WIF scripts start from the private key the Bitcoin wiki page they
  cite works through. A different key leaves a script deriving what no
  published document confirms.

- **Nor is a cleaner vector available.** The extended keys of each test
  vector `bip-0032.mediawiki` publishes, taken a vector at a time
  through the pinned `typos` binary, are reported for every vector. That
  the extraction gives back the extended keys `pyproject.toml` already
  suppresses is the control on it.

### The transcript notebooks are executed and compared, not only parsed

- **`lint.yml` runs `.github/scripts/check_notebooks.py`, which executes
  each transcript notebook and compares every code cell's outputs and
  execution count with what is committed** (closes btclib-org/bbt#78).
  `ipynb/README.md` promises that a reader's own run gives those outputs
  back byte for byte, and `check-json` asks only that the file still
  parses. A cell edited without a re-run fails the gate, named with its
  notebook, its index and a diff of the two. A cell that raises rather
  than drifting — a btclib API removed under it — aborts the run there,
  so the notebooks after it go unread and what is printed is the
  traceback rather than that report.

- **The executed notebook is compared after `nbformat` has serialised
  it.** A stream output's `text` is one string in memory and a list of
  lines on disk, so reading the committed file as JSON and comparing it
  against the executed objects reports every cell carrying an output as
  differing, the cells that reproduce exactly included. Outside the
  comparison are the notebook's `language_info` and each cell's
  `execution` metadata, which execution rewrites with the running
  interpreter and with wall clock.

- **`ipynb/PartialHashInversion.ipynb` is named rather than detected,
  and not executed**, its first cell calling `input()` twice. The run
  fails where that name is not there, and where the directory holds no
  transcript at all, so neither a rename nor a move leaves the gate
  reading nothing and passing.

- **The `!pip install` line is stripped and the rest of the cell run,
  and the cell itself is not compared**, which is one treatment for the
  reason `ipynb/README.md` already gives: what that line prints describes
  the machine. The cell runs because it carries the imports the notebook
  needs and the execution count every later cell's is counted from. Not
  running the line also keeps the notebooks off the network, so what they
  are compared against is the btclib `uv.lock` pins.

- **`nbclient` and `nbformat` arrive through `uv run --with`** and are
  in no dependency group, nothing this tree ships importing either.
  `CONTRIBUTING.md`'s last section documents the command an author runs
  first, and the `mypy` hook reads `.github/scripts` beside `py-scripts`
  so that the script is type checked like the rest.

- **`CLAUDE.md` and `pyproject.toml` describe this gate and the
  directories the `mypy` hook names** (closes btclib-org/bbt#89).
  `CLAUDE.md`'s notebook bullet says that
  `.github/scripts/check_notebooks.py` is what asks whether a transcript
  still reproduces, and that whether `PartialHashInversion.ipynb` runs
  is asked by nothing. The comment above `[tool.mypy]`'s `strict` names
  `.github/scripts` beside `py-scripts` and keeps `git ls-files '*.py'`,
  which is what says whether those are still the whole of the tree's
  tracked Python.

- **`claude-review.yml`'s prompt names what `lint.yml` executes**
  (closes btclib-org/bbt#92), that prompt being the whole of what the
  reviewing model is told about this tree before it opens
  `REVIEWING.md`: a review told that nothing runs the material does not
  ask what an executed comparison covers, and
  `ipynb/PartialHashInversion.ipynb` is where a reader's own eye is the
  only check there is. The action refuses to run where that file differs
  from the copy on the default branch, so the pull request editing it
  gets no review of record; the file's own comment is where that is
  called deliberate and where it says the job gates nothing.

### `codespell --version` is a sha where `typos --version` is a release

- **`CLAUDE.md` carries why the two spell checkers answer that question
  differently** (closes btclib-org/bbt#84). pre-commit's first strategy
  fetches one named ref and checks out `FETCH_HEAD`, so the clone holds
  no local ref for `setuptools_scm` to describe and codespell reports
  `0.1.dev1+g<sha>` where its `rev:` names a release; `typos` installs a
  released package rather than building its clone and reports that
  release. Of the two checkers configured side by side, only one's
  version string is usable as evidence of which version ran.

- **The sha is what answers the question for codespell.** The field
  after `+g` abbreviates the commit the clone sits on, and that commit
  is the one `codespell-project/codespell`'s pinned tag points at, so
  the string that appears to contradict the pin is what shows it
  honoured. The bullet carries the commands that map a pin to its
  clone, read the clone's `HEAD` and resolve the tag at the remote.

### The by-hand ECDSA script recovers the public key too

- **`py-scripts/dsa_example2.py` prints a `4. Recover keys` step**
  (closes btclib-org/bbt#81), the step `py-scripts/dsa_example1.py`
  shows as a call to `recover_pub_keys` and this one writes out: the
  verification equation K = s^-1 (c G + r Q) solved for Q rather than
  for K, over each candidate K that r admits. It is built from
  `btclib.curves.curve` and `btclib.number_theory` like the rest of the
  script, which imports nothing from `btclib.ecc.dsa`.

- **What it prints is what `recover_pub_keys` returns, in the same
  order.** Measured outside the script, the script's own printed
  `(r1, s1)` handed to `recover_pub_keys(msg1, Sig(r1, s1))`: the two
  lists agree pair by pair, and the public key step 0 prints is among
  them. The rest of the script prints byte for byte what it printed
  before, `git show origin/main:py-scripts/dsa_example2.py` run and
  diffed against it.

- **A section of this script rather than a script of its own, and it
  recovers for the first signature only.** The script is where the
  by-hand arithmetic already is, so a separate script would carry a
  second copy of the key generation and the signing to reach it; the
  second signature is there for what an ephemeral key reused across two
  messages exposes, and recovering from it again would print the same
  candidate K, its r being the same r.

### Every spell-checking exception names a string or one file

- **`[tool.typos.default.extend-words]` and `[tool.codespell]
  ignore-words-list` are gone** (closes btclib-org/bbt#83). A word entry
  stops its checker reporting that token in every file of the tree,
  where what each of them protected is a fixed string in one script:
  `ser32(i)`, BIP32's serialization function, named in the comment above
  `child_number`; the base58 extended keys `bip32_testvector1.py` and
  `bip32_testvector3.py` assert against; and the WIF
  `prvkey2wif_compressed.py` asserts against. Each is named whole under
  `[tool.typos.default.extend-identifiers]` instead, which matches an
  identifier before the checker splits it into words, so the string is
  protected and the fragment read inside it stays spell checked
  everywhere else. A base58 key is a long thing to keep in
  `pyproject.toml`, and that is the trade: this tree is course material
  whose prose is the product, and an exception blinding both checkers to
  a real word in every file of it costs more than the key length.

- **What the suppression cost is measured with a file rather than
  argued.** A markdown file holding those fragments as prose is reported
  by `typos` and by `codespell --builtin clear` under this
  configuration, and by neither under the one it replaces, while
  `git ls-files | typos --file-list - --force-exclude` and the same list
  through `codespell --builtin clear` exit zero over the tree either
  way.

- **`CPY` is the exception that stays, and it is narrowed to
  `CHANGELOG.md` rather than to a string.** ruff's name for the
  copyright rule is a whole word to `typos`, which offers `COPY` and
  `CPU` for it, so no identifier entry reaches it; and the file naming
  the rule is append-only, so those occurrences cannot be removed
  either. `[tool.typos.type.changelog]`, a file type whose glob is that
  one file, is what carries it, so the same token written in a script or
  in any other markdown of this tree is still reported.

### One reduction mod `ec.n`, written one way

- **`py-scripts/dsa_example2.py` and `py-scripts/ssa_example2.py`
  assigned the same variable twice at four places** (btclib-org/bbt#75),
  `int.from_bytes(x, "big") % ec.n` immediately overwritten by
  `int_from_bits(x, ec.nlen) % ec.n`, with nothing saying whether the
  second corrected the first or the first was left over. Each is one
  line now, `int_from_bits`, and both scripts print byte for byte what
  they printed before.

- **The one that is kept is the one that is right on any curve.**
  `int_from_bits` is SEC 1 v.2 §4.1.3(5)'s transformation: it drops the
  bits by which the digest is longer than the group order. Over
  secp256k1 and SHA256 it drops none, so the two spellings are the same
  number — measured over 20000 random digests, zero disagreements — and
  they are not the same number where the order is shorter than the
  digest. That is sixteen of btclib's `CURVES` entries and fourteen
  curves: `nistp192` and `secp192r1` are one curve under two names, and
  so are `nistp224` and `secp224r1`.

- **`ipynb/SSA.ipynb` keeps its own spelling and the script says so.**
  The notebook computes the BIP340 challenge with
  `int.from_bytes(t, "big") % ec.n`, which btclib-org/bbt#16 made the
  reference for that arithmetic; the script's `challenge` now carries
  the sentence that reconciles them, rather than leaving a reader to
  find one formula written two ways.

### The spell checkers read the notebooks and do not write to them

- **`codespell` and `typos` correct in place everywhere but `\.ipynb$`,
  and a second entry of each reads those files without writing**
  (btclib-org/bbt#73). A correction inside a notebook is an edit to a
  cell's `source` that leaves that cell's committed `outputs` where they
  are, and `ipynb/README.md` names the notebooks whose stored output a
  reader's own run reproduces byte for byte, so such an edit makes the
  file contradict itself and nothing in the diff says the output has
  stopped answering the cell. Excluding the notebooks from the checkers
  is the other way to stop it and is what `pyproject.toml`'s typos
  comment refuses: what is dropped here is the writing, not the reading.

- **A misspelling in a cell fails the gate and is named**, rather than
  being repaired into the file for its author to accept as a lint fix.
  Measured with a control put into a cell's `source` of
  `ipynb/field_table.ipynb` and into `ipynb/README.md` beside it: over
  `uvx pre-commit run --all-files` the notebook came out byte for byte
  the file that went in, the markdown was repaired in place, and the
  reporting entry failed naming the file, the line and the word. What
  the notebooks are still owed is a check that a cell's output answers
  the cell, which is btclib-org/bbt#78's.

- **`aecLiCr2dNIz`, the Colab cell id of one cell of `ipynb/DSA.ipynb`
  and of the same cell in `ipynb/SSA.ipynb`, is named under
  `[tool.typos.default.extend-identifiers]`.** That entry matches the
  whole identifier, so the two-letter fragment `typos` reads inside it
  is spell checked again everywhere else in the tree.
  `[tool.codespell] ignore-words-list` drops the same word: that list
  admits only keys of the typos word table, and the word is not one
  `codespell --builtin clear` reports anywhere.

### Nothing is carried where nothing reads it

- **The root `TODO` is gone** (btclib-org/bbt#70). Twenty bytes,
  `jupyter for scripts`, tracked since 2019-01-23 and named by no
  document: not `README.md`'s list of folders, not `CLAUDE.md`'s
  *Architecture*, not `CONTRIBUTING.md`, not `.gitignore`. A file called
  `TODO` at the root of a repository whose material is the product reads
  as a statement about the course rather than a note to its author, and
  seven years is long enough to answer whether it named anything anybody
  wanted.

- **`py-scripts/dsa_example2.py` carried two notes and now carries
  neither.** `# TODO implement pubkey recovery` is btclib-org/bbt#81: it
  is real work, `dsa_example1.py` showing recovery with the library
  while its by-hand twin shows none, and `CONTRIBUTING.md`'s *The issue
  tracker* says a finding is filed rather than carried.
  `# TODO crack private key` is not work at all — `ipynb/DSA.ipynb`'s
  last cell sets exactly that as the reader's exercise, so a script that
  answered it would spend it. The comment there now says so, which is
  the other half of what the issue asked for: a note is an issue or a
  sentence saying why the comment is the right place.

- **`py-scripts/ssa_example2.py` says it too.** It stops one step short
  of `ipynb/SSA.ipynb`'s exercise for the same reason and said nothing
  about it, so the two twin scripts would otherwise have explained
  themselves differently. Its note was already gone, removed by
  btclib-org/bbt#67; what was missing was the sentence.

### The regtest walk-through's transaction samples say they are samples

- **`regtest-lab/README.md` showed the output of `gettransaction` as a
  screenshot of a 2019 run** (btclib-org/bbt#54), while the setup pages
  beside it install 31.1. Measured against v31.1.0 on a node in a
  scratch datadir, a reader now sees four keys the page never
  mentioned: `wtxid`, `mempoolconflicts`,
  `lastprocessedblock` — an object of `hash` and `height` — and, in the
  confirmed sample only, `blockheight`. Nothing a reader typed was
  wrong; there was simply no way to tell a version difference from a
  mistake.

- **The two blocks are illustrations now, and say so.** Every value only
  the reader's own run produces is written `...` — the txid, the wtxid,
  the raw `hex`, the two unix timestamps and the block hash — and the
  sentence under each says what is left is worth comparing and why: the
  amounts are the same on any machine that followed these pages, because
  `-fallbackfee=0.0002` in the setup command is what fixes the fee. The
  two that vary anyway are named rather than left to puzzle over,
  `vout` being whichever of the two outputs the wallet put first.

- **The keys are in the order Core prints them, indented the way Core
  indents them.** The old blocks were neither: they put every key at
  column zero, which no Core that prints these keys does.

### The notebooks say which of them a reader can reproduce

- **`ipynb/DSA.ipynb` carried the outputs of a 2020 session**
  (btclib-org/bbt#19), and one of them had gone wrong rather than merely
  stale: btclib renamed the cofactor in its curve dump, so the committed
  output read `h = 1` where the library now prints `cofactor = 1` —
  and `ipynb/SSA.ipynb`, which has the same source cell, already printed
  the new one. Two notebooks in one directory disagreed about the output
  of identical code. Every other value was still correct: executed
  against btclib 2026.8.21, fourteen of its sixteen code cells
  reproduced their committed output byte for byte.

- **It is executed and its outputs are the run's**, its execution counts
  now 1 to 16 rather than the `5, 22, 25, 8, …` of a notebook run out of
  order — a sequence in which 18 appeared twice, which one kernel cannot
  produce. `ipynb/field_table.ipynb` needed no new outputs, its three
  cells already reproducing exactly, but carried counts starting at 66
  and a `language_info` naming Python 3.8.

- **The `!pip install` cell carries no output**, which is what
  `ipynb/SSA.ipynb` already did. It answers a download transcript on
  Colab, `Requirement already satisfied` under `pip` and
  `command not found: pip` in the environment `uv sync` builds, so what
  was stored there described a machine that no longer exists. The Colab
  `outputId` and `colab` receipts of that session are gone from the cell
  metadata for the same reason.

- **`ipynb/README.md` now says which notebooks are transcripts and which
  one is an illustration.** `ipynb/PartialHashInversion.ipynb` cannot be
  a transcript and the reader is told so rather than left to find out:
  its first cell calls `input()` twice, so headless it raises
  `StdinNotImplementedError` before computing anything, and what it
  prints is how long the search took on one machine.

### `pyproject.toml` names the oldest uv that may read `uv.lock`

- **`[tool.uv] required-version` is declared, at the ceiling rather than
  safely below it** (btclib-org/bbt#68). What a floor refuses is an
  older uv rewriting the committed lock in a format the runners then
  fail to read, so one below the ceiling is safe and buys nothing beyond
  where it sits.

- **The ceiling is the uv Dependabot's own bundled updater ships**, a
  floor above it making every lock update that updater attempts a silent
  no-op. Section 1 of the standard has the argument and section 15 the
  command that re-derives the ceiling.

### `py-scripts/ssa_example2.py` signs the way BIP340 says

- **The script left the even-`y` requirement on the ephemeral point out
  of both the signing and the verification** (btclib-org/bbt#67). It
  normalised the public key onto its even root and not the ephemeral
  point, and its verification compared x coordinates alone; the two
  omissions agreed with each other, so it printed `True` for signatures
  `btclib.ecc.ssa.verify_` rejects. It negates `k` where `K` lands on
  the odd root, and prints the parity of the recovered point alongside
  the x comparison. `ssa.verify_` answers `True` for both signatures it
  produces and `False` for `(r, n - s)`, and the values it prints agree
  with `ipynb/SSA.ipynb`'s committed outputs.

- **The challenge is computed here rather than imported from
  `btclib.ecc.ssa`**: the tagged hash is written out, the way
  `ipynb/SSA.ipynb` writes it. A script demonstrating ECSSA by hand
  imports nothing from the module that implements it.

### The union driver's damage repairs itself

- **`CHANGELOG.md` turned MD022 and MD032 off for itself**
  (btclib-org/bbt#66), because a rebase of a `merge=union` file joins two
  `###` blocks and drops the blank line between them, and the rule
  reported a gap it would not close. The markdown hook runs with `--fix`,
  so that gap is now its own repair: the directive is gone and both rules
  apply here again. Measured by doing the damage and running the hook —
  it puts the line back, where with the directive in place it did not.

- **`codespell` corrects in place**, joining the hooks that fix rather
  than report. The flag went on against a measurement and not on
  principle: a spell checker's repairs are guesses where a formatter's
  are deterministic, and this one rewrites nothing in the tree today,
  proved against a control file of misspellings it does report.

- The other two hooks the issue names needed nothing. `markdownlint-cli2`
  already carried `--fix`, and `typos` already declared
  `--write-changes --force-exclude` with the comment saying why it
  restates them rather than inheriting them.

### No script under `py-scripts/` writes outside this tree

- **`curves.py` and `rfc6979.py` demonstrated nothing: they generated
  data files for btclib-org/btclib and wrote them into
  `../../btclib/btclib/data` and `../../btclib/btclib/tests/test_data`**
  (btclib-org/bbt#17), paths that repository does not have, so each
  exited 1 with `FileNotFoundError`. They are deleted. The issue
  reserved the decision of where that data belongs and the maintainer
  took it; btclib-org/btclib carries the curve parameters at
  `btclib/curves/_data/` and the RFC 6979 vectors at
  `tests/ecc/_data/rfc6979.json`, whose provenance its own
  `tests/_data/README.md` records as a transcription of the RFC.
  `gh api "repos/btclib-org/btclib/git/trees/main?recursive=1"` is what
  says which paths that repository has, and
  `grep -rn 'open(\|\.\./\|dirname(__file__)' py-scripts/*.py` that
  nothing left here reaches past the repository root.

- **`py-scripts/README.md` no longer carries the exception they
  needed**, its list being what a reader has to know before running a
  script.

### `ipynb/SSA.ipynb` signs with Schnorr

- **The notebook was titled Schnorr and demonstrated ECDSA**
  (btclib-org/bbt#16). Its own section headings said `Signature (DSA)`
  and `Signature verification (DSA)`, and its signing cell computed
  `s = k⁻¹(h + r*q)`, which is ECDSA's. It was `DSA.ipynb`'s lesson
  section for section — the malleation section and the closing exercise
  included — with ECDSA's arithmetic under a Schnorr title. A student
  following the SSA lecture with it was shown the wrong scheme.

- **It now computes what BIP340 specifies**: an x-only public key taken
  on its even root, a challenge
  `c = tagged_hash("BIP0340/challenge", x_K || x_Q || m)` over a message
  that stays bytes, an ephemeral point taken on its even root too, and
  `s = k + c*q` — an addition where ECDSA has an inverse. Verification
  solves `s*G - c*Q = K`. The tagged hash is written out in the notebook
  rather than imported, which is what the rest of the material does with
  the arithmetic it teaches.

- **What the sections now teach is the difference rather than the same
  lesson twice.** Malleation was ECDSA's `(r, n - s)`; the notebook
  shows that signature failing, because BIP340's check is linear in `s`
  and a different `s` gives a different point. The reused-ephemeral-key
  section keeps its subject and gains a symptom visible before any
  arithmetic: the same ephemeral key returns the same `r`. The exercise
  is one modular inverse, `q = (s - s2)(c - c2)⁻¹`, where ECDSA's needed
  the hashes as well.

- **Every output was regenerated by running the notebook**, the
  committed ones having answered cells that no longer exist. The Colab
  `executionInfo`, `outputId` and display hints came off with them: they
  recorded a 2019 run by a named user, which is not the run these
  outputs are from. btclib-org/bbt#19 stays open for the notebooks whose
  outputs are still the 2020 ones.

### `CONTRIBUTING.md`'s shared half is the organization's copy

- **Everything above `## This repository in particular` is
  `btclib-org/.github`'s copy of it, byte for byte** (btclib-org/bbt#61).
  Section 14 of the standard names this file as the same in every
  repository up to that heading, and `tests/verbatim_test.py` there
  compares the copies over what precedes that marker. What arrives with
  the port is *The landing queue*, under *Pull requests*: which of
  several already open pull requests is carried to `main` next, CI
  throughput as the reason rather than the ack a waiting pull request
  keeps, cheapest and least contended first, and the bounded exception
  the maintainer may declare. The `[s9]` and `[s11]` link definitions
  live in that half and come with it. Everything below the marker is
  this tree's own and the port does not reach it.

- **The paragraph in *Documentation and comments* on a commit message
  cites the rule that fixes the merge method** rather than restating it,
  and says the message is read on `main` as the landing commit's body.

### `CLAUDE.md` says how a notebook is edited, not only what it carries

- **The section that names this tree's failure modes said one thing
  about `ipynb/`, and it was the thing a session needs after it has
  managed to edit a notebook** (btclib-org/bbt#64). Editing one is the
  part that costs the session: `pretty-format-json` carries
  `exclude: \.ipynb$`, so nothing normalises these files and they are
  not written alike, `SSA.ipynb` being one line of JSON. Each of them
  round-trips through `json.dumps` losslessly at its own settings, which
  are not the same settings for all of them, so a round-trip is safe
  only where those settings were measured first and silent where they
  were not — more work than the targeted replacement it would replace.
  A diff of the result answers nothing either way, which leaves the
  parse as what establishes that no `outputs` array moved. The bullet
  divides into the shape of an edit that works, the parse that verifies
  it, and the rebase conflict on the one-line notebook, which is the
  entire file.

- **`grep` was worth its own bullet beside it.** An unanchored pattern
  reaches the base64 of a committed image, which is how a `grep` of
  `ipynb/` came to report a match in a notebook whose cells had none
  during btclib-org/bbt#26; the conclusion drawn from it was published
  before it was caught. `grep -c` counting lines is the second half and
  the quieter one: on a notebook written on one line it cannot answer
  more than 1 however many occurrences there are, and cannot say that it
  could not.

### Every notebook carries the licence this repository ships

- **`ipynb/PartialHashInversion.ipynb`'s first code cell opened with
  btclib's pre-MIT header** (btclib-org/bbt#27), shebang included. It
  stated a restriction `LICENSE` does not impose, a year range neither
  licence file carries, and that the file is part of `btclib`, which this
  tree is not — the three claims btclib-org/bbt#15 removed from the
  scripts, measured against the same two files: `LICENSE` is MIT and
  `COPYRIGHT` names the holder without a year. The cell carries
  `COPYRIGHT`'s three lines instead, and the shebang went with the
  header — a cell is not a file and nothing execs it.

- **The other three notebooks carried no notice at all**, and now carry
  those same three lines at the top of their first code cell. The issue
  left two questions open and they have different answers. *Where* a
  notice goes is measured rather than chosen: `CPY001` reads the first
  code cell, so a notice that satisfies the rule has to open the first
  cell a reader runs and cannot sit in a markdown header they scroll
  past. *Whether* one goes there at all was a choice, and the ground it
  was taken on is one the tree had already written down — the per-file
  ignore's own comment said btclib-org/bbt#27 "is the issue this line
  comes off with", so its coming off is what the file said would happen,
  and this is the change that does it. A reader who would rather it had
  not is looking for that sentence, and it is in `pyproject.toml`'s
  history rather than in anybody's judgement here.

- **`pyproject.toml`'s per-file `missing-copyright-notice` ignore is
  gone**, which is the thing it was written to come off for. `CPY` gates
  `ipynb/` the way it gates `py-scripts/` now, with nothing excluded from
  it, so the tree answers zero to that family with the ignore removed
  rather than with it in place.

- Nothing computed changes. Four comment lines were added at the top of
  four cells, so the outputs these notebooks carry still answer them.

### ruff reads every notebook, and every notebook answers zero

- **`DSA.ipynb`, `SSA.ipynb` and `PartialHashInversion.ipynb` declared no
  language, so ruff skipped them as files** (btclib-org/bbt#26). Asked
  for every rule ruff has, three of the four notebooks answered nothing
  at all and `field_table.ipynb` answered, and the difference was in the
  metadata rather than in the cells: only `field_table.ipynb` carried
  `language_info`. A skipped file and a clean file both print
  nothing, so every family `pyproject.toml`'s `select` names was inert on
  three of the four and nothing in the configuration said so. Each of the
  three now declares `"language_info": {"name": "python"}` — which is
  what Jupyter writes whenever it saves a notebook, so the day one of
  them was opened and saved those rules would have started reporting
  anyway, against cells nobody had edited.

- **What ruff found once it could read them is fixed in the same
  change**: two trailing spaces in `DSA.ipynb`'s exercise cell, two
  statements written after the colon of their `if`, and four comments
  past the 80 columns `max-doc-length` sets. Whitespace, comment wrapping
  and two statements moved onto their own line — nothing computed
  changes, `ast.parse` giving the same tree before and after each split,
  so the outputs these notebooks carry still answer the cells above them.
  `uvx ruff check .` exits 0. One of the rewrapped comments named an `s1`
  that `SSA.ipynb` does not have and never had, its variable being `s`;
  the word is corrected on the line being rewrapped rather than filed.

- **`pyproject.toml`'s per-file `missing-copyright-notice` ignore
  described a tree where one notebook was read.** All four are read now,
  so without that line selecting `CPY` would ask a notice of every one of
  them rather than of the one whose metadata happened to name a language;
  the comment says that, and names the command that counts four. The line
  itself still comes off with btclib-org/bbt#27, the issue that decides
  where a notice belongs in a notebook.

### The gate's comments sit beside what they explain, and name what it found

- **`pyproject.toml`'s `PLR2004` comment called `2` and `3` the SEC
  prefixes of a compressed point** (btclib-org/bbt#20). The command the
  comment itself names puts them in `py-scripts/ec_explorer.py`'s
  `isprime`, where they are the two primes a primality test settles
  before dividing by anything; no SEC prefix appears in the rule's output
  at all, `py-scripts/pubkey2address.py` building its prefix from bytes
  literals, which the rule does not read. The justification an `ignore`
  entry carries is what decides whether the entry still earns its place,
  so it now separates the numbers a specification assigns from the two
  that are arithmetic.

- **`.pre-commit-config.yaml`'s paragraph on the ruff selection sat above
  the `uv-lock` hook** (btclib-org/bbt#39), two entries before the one it
  is about, so a reader arriving at `ruff-pre-commit` found no reason
  beside it and a reader arriving at `uv-pre-commit` found two
  paragraphs, the first about another tool. It sits above
  `ruff-pre-commit`, which is where every other comment in the file sits
  relative to what it explains. No hook is added, removed or
  reconfigured.

### Two scripts do what they say when they are run

- **`hash_puzzle.py` raised `IndexError` where it had a sentence
  prepared** (btclib-org/bbt#38). It asked whether a nonce was found by
  subscripting the counter list at the number of zeros requested, and a
  search that exhausts never grows that list to reach it, so the failure
  path of a script demonstrating proof of work was an unhandled
  exception and `nonce not found` could not print. It asks `nonce`
  instead, with `None` for the sentinel rather than `0` — which is a
  nonce the search can return, and as the sentinel turned a search
  succeeding on its first attempt into `nonce not found`. The bar chart
  took the number of zeros for its x axis, where the counter list is the
  only length that always matches it: shorter when the search exhausts,
  which `plt.bar` refuses, and longer when the winning hash carries more
  zeros than were asked for, which `plt.bar` accepts by broadcasting and
  draws at one tick.

- **`speedup_curvemult.py` benchmarked windows it did not label**
  (btclib-org/bbt#23). Four call sites passed a literal where the branch
  beside them passed `w`: the row labelled *Sliding window 4* measured
  five, and *wNAF 5* measured four. They pass `w`.

### `links.yml` reads each page once

- **It passed lychee `"*.md"` and `"**/*.md"`, and the second already
  resolves everything the first does** (btclib-org/bbt#55), `**/` matching
  zero directories as well as any number of them, so every root file was
  read twice. The report counted each occurrence in one twice and printed
  each failure in one twice, at the same `file:line` — which invites the
  question of whether there are two problems. The workflow gates nothing,
  so being readable is the whole of what it is for.

### The command that builds the environment is `uv sync --locked`

- **`py-scripts/README.md` told a reader to build it with a bare
  `uv sync`** (btclib-org/bbt#21), where `CONTRIBUTING.md` documents
  `uv sync --locked` and says what the flag buys: a lock out of step with
  `pyproject.toml` becomes a failure rather than a silent re-resolution.
  It is the first command a reader of that directory runs.

- **`CLAUDE.md`'s worktree recipe spelled it bare too**, in the comment
  beside `cd "$WT"`, above the entry in the same file asking for the
  flag.

### The regtest lab runs on a current Bitcoin Core

- **`regtest-lab/linux.md` and `mac-os.md` downloaded Core from
  `bitcoin.org/bin`, which answers 404** (btclib-org/bbt#50), so the
  first executable step of two of the three setup pages could not be
  completed and the failure surfaced one step later, at `tar`, as a
  corrupt archive. The three pages named three different versions
  besides. They now name one, from the host `windows.md` already used,
  and `mac-os.md` names the build for the machine, `osx64` having been
  replaced by an Apple silicon and an Intel archive.

- **`windows.md` described a layout the archive does not have.** The zip
  holds `bin`, `libexec` and `share`; the page named `include` and `lib`,
  and called the GUI executable `bitcoinqt`.

- **A node no longer makes a wallet by itself**, so the lab's first
  command reaching an address failed with *A default wallet is no longer
  automatically created*. `regtest-lab/README.md` gains the
  `createwallet` step, and names `loadwallet` for a later start.

- **`sendtoaddress` failed with *Fee estimation failed. Fallbackfee is
  disabled***, that being Core's regtest default. Every place the lab
  starts a node passes `-fallbackfee=0.0002` — the three setup pages and
  the three Windows launchers.

- **The command list linked documentation for a version the site no
  longer builds that way.** It names the newest the site publishes.
  `generatetoaddress` loses its link rather than gaining a stale one: no
  `generate` RPC is documented there, and the command below it is what
  prints the help.

### `links.yml` checks the addresses this tree asks a reader to follow

- **Nothing measured whether a link still resolved** (btclib-org/bbt#22),
  which in a tree that is documentation almost entirely is one of the few
  defects it can have — and the launcher links in
  `regtest-lab/windows.md` answered 404 until somebody read them.
  `links.yml` runs lychee over the markdown weekly, on the day and hour
  section 10's grid gives `links` and the minute it gives this
  repository, and on a pull request that touches the workflow or the
  ignore list beside it. It gates nothing: a link rots on somebody else's
  schedule, so a red merge would be a run to repeat rather than a thing
  to fix.

- **`.lycheeignore` carries what a checker can only ever misreport.**
  Stack Overflow answers a runner 403 whatever the request looks like,
  measured with a current browser user agent and an `Accept: text/html`
  header, while the page it names is live.

### `REPOSITORY.md` and `lint.yml` said `main` had no required check

- **Both said the rule did not exist, and `Lint` was bound**
  (btclib-org/bbt#49). `REPOSITORY.md`'s *Required checks on main* opened
  with *There are none* and printed the command answering `false`;
  `gh api repos/btclib-org/bbt/branches/main/protection` answers with
  `Lint` bound to app `15368` and `strict`. `lint.yml` contradicted
  itself on the same command, its header denying the rule that its job's
  own comment described. The section now reads the rule back from the
  endpoint, and says why neither `claude-review.yml` nor `links.yml` is a
  candidate for a second one; the instructions for creating a rule that
  exists are gone, and what survives of them is that changing the list is
  a `PATCH` rather than a `PUT` of the whole protection object, `Lint`
  being the one rule here no ruleset carries a copy of.

- **`CONTRIBUTING.md` stated the same thing a third time**, in the
  paragraph that defers to `REPOSITORY.md` for it. *What gates a merge,
  and what only reports* now says `Lint` is the required check, in the
  sentence that already names the job, and names `links.yml` in the
  enumeration of what CI does to a pull request.

### `regtest-lab/` and `README.md` link what this tree holds

- **The tree linked itself and btclib under `dginst`, the owner both
  lived under before `btclib-org`, and `regtest-lab/` linked its own
  pages under the repository's former names and `master`**
  (btclib-org/bbt#31). `README.md`'s btclib link now names the owner
  that answers it, and the pages `regtest-lab/README.md` and
  `regtest-lab/windows.md` link inside this tree are relative, a
  redirect through a renamed organization, a renamed repository and a
  renamed default branch being three redirects where a relative link is
  none. The Windows launchers were the case where the redirect had
  already stopped resolving: `dginst/BitcoinBlockchainTechnology` is the
  name btclib redirects from, not bbt, so those links answered 404 —
  and the paths they named are not paths this tree has, the launchers
  living in `regtest-lab/windowsbat/` under
  `regtest-<port>-<action>-<name>.bat`.

- **`regtest-lab/windows.md` named the nodes one apart from the files it
  links.** The page called 18444 the server, 18555 Alice's node and
  18666 Bob's; the batch files pass `-uacomment=Alice` on 18444, `Bob`
  on 18555 and `Carol` on 18666. The page now names them as the files
  do.

### `REPOSITORY.md` names both sources of the landing commit's subject

- **The `COMMIT_OR_PR_TITLE` paragraph named the pull request's title as
  the landing commit's subject, without the condition the setting
  carries** (btclib-org/bbt#44), citing the standard's *What a pull
  request says it is* rather than its *Merge method*, which is the
  subsection deciding which text lands. The setting takes the commit's
  own subject where a branch has one commit and the pull request's title
  where it has more, and the paragraph says so now. The `[s11-title]`
  definition goes with the citation, that paragraph having been its only
  user.

### `CLAUDE.md` names the worktree `wt-<tracker>-<issue>-<repo>-<role>`

- **The recipe named the worktree after the issue alone, `wt<issue>`**
  (btclib-org/.github#292). A worktree's administrative directory lives
  in the `.git` of the repository `git worktree add` was run from, one
  per repository, so two repositories cannot collide there; what the
  recipe left uncovered was a same-repository collision, between two
  worktrees of different work sharing a generic basename, and a *path*
  collision across repositories, since the workers of one session share
  one scratchpad directory and a session carrying one issue into several
  repositories computed the same target path for each. The recipe now
  names the worktree `wt-<tracker>-<issue>-<repo>-<role>`, most general
  part first: `tracker` because an issue number is unique only within
  one tracker, `issue` against the same-repository collision, `repo`
  against the cross-repository path collision, and `role` against a
  coder and its reviewer holding a worktree at once.

### CLAUDE.md's primary-checkout paragraph names the read that cannot go stale

- **The paragraph said reading the checkout was fine and so was `git
  fetch`, without saying `git fetch` moves `refs/remotes/origin/main`
  and leaves the work tree where it was** (btclib-org/.github#255), so a
  `grep` or a `Read` against the checkout answered for whenever it was
  last brought forward. It now names `git show origin/main:<path>` as
  the read that does not go stale, and gives the fast-forward that
  brings a clean checkout forward without working in it.

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

### `REPOSITORY.md`'s *Features* answers what the endpoint answers

- **The wiki and the projects board are this repository's own answer,
  not a divergence from the family** (closes btclib-org/.github#507).
  `gh api repos/btclib-org/$r --jq '[(.has_wiki|tostring),
  (.has_projects|tostring)]'` answers `true` twice for every sibling but
  `btclib-benchmarks`, so the sentence had the direction backwards: this
  repository was agreeing with the family, and `btclib-benchmarks` is
  the one that turns both off. `btclib-org/btclib-node`'s copy already
  read the same call correctly.

### `[project].authors` names the collective, not a per-tree literal

- **`pyproject.toml` gains
  `authors = [{ name = "The btclib developers", email = "devs@btclib.org" }]`**
  (issue btclib-org/.github#534). The name and address are `COPYRIGHT`'s,
  the same pair the publishing trees already carry in their own
  `[project]` tables, and the key lands here too though `package = false`
  and this tree ships nothing.

### `REPOSITORY.md` says what it covers, and what it passes over

- **The claim that this file is the whole of what is set outside the
  tree is gone** (issue btclib-org/.github#551). Section 11 of the
  standard bounds a `REPOSITORY.md` at the settings the standard asks
  about — section 16's checklist, and the sections that state a rule for
  a setting — and rejects the blanket claim, which no command checks.
- **A *What this file passes over* section says what falls outside that
  scope** (issue btclib-org/.github#551). The repository document's
  fields no section here quotes, the facilities that answer empty, and
  `allow_forking`, `has_downloads`, `is_template` and
  `web_commit_signoff_required`, about which the standard states no
  rule; the price is that a change to any of them shows up here in
  nothing.

### The scripts are run, and each exclusion says why

- **`lint.yml` gains a step that runs every script under `py-scripts/`
  it does not exclude, and requires exit 0** (issue
  btclib-org/.github#301). What course material fails at is not an
  untested line: `py-scripts/` imports `btclib`, so a release renaming
  something breaks a demonstration, and the exit code is what says so.
  `.github/scripts/check_scripts.py` is what the step runs, beside the
  notebook step and for the reason that one's comment gives.
- **The scripts are discovered rather than listed** (issue
  btclib-org/.github#301). One added later is gated without an edit, one
  removed leaves no dangling name, and the script fails where it reads
  none — a gate that opened no file is otherwise silent in exactly the
  way a gate that found no defect is.
- **The `speedup_*.py` benchmarks are among them, for their exit code
  alone** (issue btclib-org/.github#301). What breaks a benchmark is the
  same `AttributeError` a renamed `btclib` gives any other script, rather
  than its becoming slow, so the timing output is ignored: a shared
  runner cannot honestly answer how fast one is.
- **`py-scripts/getutxo.py` and `py-scripts/ec_explorer.py` are excluded
  by name, each with its reason beside it** (issue
  btclib-org/.github#301). The first queries a third party's block
  explorer, so a red there would be that service's maintenance rather
  than this tree's defect; the second searches every `(a, b)` of a fixed
  range against every `x` below each prime it lists, and overruns the
  ceiling the gate gives a script rather than merely being slow. An
  excluded name that is not there is a failure, so a rename cannot
  quietly leave a script ungated.
- **`py-scripts/hash_puzzle.py` is fed two newlines and run under
  `MPLBACKEND=Agg`** (issue btclib-org/.github#301). Each of its two
  prompts documents the default an empty line takes, and its
  `plt.show()` calls block until a window is closed on any interactive
  backend, so without it the script does not terminate and what ends it
  is the gate's ceiling.
- **`CLAUDE.md` and `CONTRIBUTING.md` name the new gate** (issue
  btclib-org/.github#301). mypy resolving the names a script imports is
  no longer the whole of what is asked of `py-scripts/`, and the command
  an author runs before pushing sits beside the notebook one.
- **`REPOSITORY.md` and `REVIEWING.md` say what the gate answers and
  what is left to a person** (issue btclib-org/.github#301). *What is
  not configured, and why* counts running a script among what `lint.yml`
  automates, and `REVIEWING.md`'s question about a script a diff touched
  asks the reviewer for what the gate does not read: whether the output
  is what the material says.
- **`pyproject.toml`'s `print` ignore names `.github/scripts/` rather
  than one file in it** (issue btclib-org/.github#301). Both checkers
  there print, and `uvx ruff check --preview --select T201 .` is what
  lists the sites the entry covers.
- **`claude-review.yml`'s prompt says what runs a script** (issue
  btclib-org/.github#301). That prompt is the whole of what the
  reviewing model is told about this tree before it opens
  `REVIEWING.md`, and a review told that nothing runs a script does not
  ask what an exit code covers: the step reads nothing a script prints,
  and there is where a reviewer's own reading starts.

### `py-scripts/getutxo.py` is gone

- **The script and its `EXCLUSIONS` entry in
  `.github/scripts/check_scripts.py` are removed** (closes #15).
  [btclib-org/.github#301](https://github.com/btclib-org/.github/issues/301)
  reserved a question for `getutxo.py` — run it on a schedule, run it
  under a named switch, or write down that it runs nowhere — and this
  closes it by deleting the script instead. A schedule would answer
  whether blockchain.info still shapes its reply the way the script
  expects, not whether the script's own printed output still teaches
  what the material claims, and that second question — the one a reader
  answers for every other script here — was never measured for this
  one.
- **`pyproject.toml` drops the `requests` dependency**, imported by
  nothing else under `py-scripts/` or `ipynb/`, and `uv.lock` moves with
  it.
- **`py-scripts/README.md`, `CONTRIBUTING.md` and the
  `commented-out-code` ignore's justification in `pyproject.toml` no
  longer mention the script.**

### The verbatim files are the standard's copies, byte for byte

- **`.gitattributes` states the union price as section 9 of the
  standard does** (issue btclib-org/.github#423): the driver is a
  checkout's and the forge does not apply it, so a pull request whose
  `CHANGELOG.md` overlaps its base is reported `CONFLICTING` however
  cleanly the pair merges locally, and a rebase on a checkout is what
  clears it.
- **`.markdownlint.jsonc` points at section 14 of the standard for who
  carries it** (issue btclib-org/.github#316), in place of an
  enumeration of trees.
- **`CONTRIBUTING.md`'s shared half is btclib-org/.github's** (issue
  btclib-org/.github#281): the half is replaced whole rather than each
  change applied by hand, a hand-written list of them being what comes
  up short. Among them, *The landing queue* points at `REPOSITORY.md`'s
  *Plan-gated settings* for the ceiling's figure (issue
  btclib-org/.github#412).
