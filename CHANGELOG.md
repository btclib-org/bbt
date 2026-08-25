# Changelog

What changed in this repository, and why. Nothing here is released —
`CONTRIBUTING.md`'s *A version, and no release* says what that means and
what it costs — so the entries are grouped by subject rather than by
version, and there are no release notes for this file to be the record
behind.

## Unreleased

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
