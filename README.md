# Bitcoin and Blockchain Technology

<!-- The badges are what the reader decides with, one property of the
tree per badge, in the fixed order btclib-org/.github's README.md
section 2 gives: the licence, the lint workflow, pre-commit.ci, then
the sentinels this tree runs, in section 10's calendar order -- links,
then scorecard. The OpenSSF Scorecard badge takes its place in that
order like any other: section 10 gives scorecard a day and an hour row,
and the exception that section states for it -- its triggers are the
action's own -- is to the trigger rule rather than to the calendar.
This tree publishes nothing (`package = false`, no
`release.yml`), holds no suite (no `tests/`) and builds no
documentation (no `docs/`), so the version, downloads, development
status, supported Python versions, wheel, implementation,
github/v/release, test, docs and Read the Docs badges have no state to
report. One badge per line keeps a change to one line and every line
inside MD013, whose 80 columns bind only where a space follows
them. -->
[![license](https://img.shields.io/github/license/btclib-org/bbt.svg)](https://github.com/btclib-org/bbt/blob/main/LICENSE)

[![lint workflow status](https://github.com/btclib-org/bbt/actions/workflows/lint.yml/badge.svg)](https://github.com/btclib-org/bbt/actions/workflows/lint.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/btclib-org/bbt/main.svg)](https://results.pre-commit.ci/latest/github/btclib-org/bbt/main)
[![links workflow status](https://github.com/btclib-org/bbt/actions/workflows/links.yml/badge.svg)](https://github.com/btclib-org/bbt/actions/workflows/links.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/btclib-org/bbt/badge)](https://scorecard.dev/viewer/?uri=github.com/btclib-org/bbt)

The course is taught at:

- University of Milano-Bicocca
- Politecnico di Milano
- University of Milano

The latest version of the course slides is available from the course page
at <http://www.ametrano.net/bbt/>.

Other material available in this repo:

- the *calc* folder includes LibreOffice Calc spreadsheets illustrating
  finite fields and elliptic curves
- the *excel* folder includes Excel spreadsheets illustrating finite
  fields and elliptic curves
- the *ipynb* folder includes Jupyter notebooks
- the *py-scripts* folder includes Python scripts: most of them require
  the [btclib](https://github.com/btclib-org/btclib) library, and
  `pyproject.toml` declares which interpreter and which packages the
  environment is built with
- the *regtest-lab* folder includes information for a regtest session
  using Bitcoin Core

There is no release: nothing here is published to an index or cut as a
GitHub release, the material ships by being read here and by being
cloned, and [CONTRIBUTING.md](./CONTRIBUTING.md)'s *A version, and no
release* is what the placeholder version in `pyproject.toml` is for.

## Limitations, not vulnerabilities

These are known and inherent, and each is what the material is *for*.
They are here rather than in a security policy because this repository
publishes nothing and so keeps no `SECURITY.md` of its own: the policy
shown at [security/policy](https://github.com/btclib-org/bbt/security/policy)
is the organization's, and a shared file cannot name what is this tree's.

- **`lab-tutorial/01.md` publishes a private key**, its WIF and the
  address it derives, as the worked example of importing one into a
  wallet. Anybody who reads the page can spend anything sent to that
  address. It is published deliberately, and it is the reason the page
  is a tutorial and not a wallet guide: use a key of your own, generated
  as the page describes, and treat every key printed in this repository
  as somebody else's.
- **The secret scanner does not catch that**, and would not with its
  entropy plugins on either — measured, `detect-secrets scan
  lab-tutorial/01.md` with every plugin enabled reports nothing, a WIF
  key in prose being neither hex nor base64 to it.
  `.pre-commit-config.yaml` says what the scanner is kept for; a key in
  a page is a reader's job to notice, and this section is that notice.
- **`py-scripts/speedup_*.py` seed `random` with a constant**, so the
  scalars they multiply are the same on every run. That is what makes a
  timing comparison a comparison. None of those values is a key, and no
  script that yields one draws it from `random` — `grep -l "import
  random" py-scripts/*.py` names them, all of them `speedup_*`. The
  scripts that *generate* a key use `secrets`; the rest start from a
  published test vector.
- **The scripts print what they compute**, keys included, because
  showing the intermediate value is the whole of the demonstration. A
  terminal history is not a place to leave one.
- **Nothing here has been audited as an implementation.** The point of a
  script that reimplements a curve operation is that a reader can follow
  it, and the version that is easiest to follow is not the version to
  put a key into.

What is worth reporting is narrow for the same reason: a step that
would lose somebody money if they followed it, a key committed that was not
meant to be published, a script that does something other than what its
page says. A defect in what the scripts call is
[btclib's](https://github.com/btclib-org/btclib/security/policy), and a
defect in a wallet, a key generator or a block explorer that
`lab-tutorial/` walks through is its author's — though routing a report
is the maintainers' job, not the reporter's, so report it wherever you
found it.

Working here: [CONTRIBUTING.md](./CONTRIBUTING.md) for how to,
[REVIEWING.md](./REVIEWING.md) for what a pull request is answered
against.
