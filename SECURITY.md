# Security policy

## Reporting a vulnerability

If you have found a security vulnerability, please do not open a GitHub
issue: an issue is public from the moment it is filed, and so is the
window between filing it and a fix landing.

Report it privately instead, by
[opening a security advisory](https://github.com/btclib-org/bbt/security/advisories/new).
Only the maintainers can see it, and the discussion stays private until
an advisory is published.

If you have no GitHub account, or would rather not use it for this,
responsible disclosure by email to *security at btclib dot org* is
equally welcome.

## What belongs here, and what belongs upstream

This repository is course material: notebooks, spreadsheets, a regtest
walk-through and scripts that each demonstrate one thing. Nothing in it
is installed, imported or run by anything other than a reader following
along. So what belongs here is narrow, and it is worth saying which half
is which, because the interesting failure of teaching material is that
somebody follows it.

What belongs here:

- **a step that would lose somebody money if they followed it** — a
  script or a page that generates a key a reader might use for real, an
  instruction that puts a live key somewhere it can be read, a
  walk-through that says mainnet where it means regtest;
- **a key that was not meant to be published** committed to this tree;
- **a script that does something other than what its page says it does.**

What does not:

- **what btclib does.** The scripts call it; a defect in the library is
  [btclib's](https://github.com/btclib-org/btclib/security/policy).
- **what a third-party tool does.** `lab-tutorial/` walks a reader
  through a wallet, a key generator and a block explorer, none of them
  this project's. Report those to whoever wrote them.

Report it wherever you found it, though: routing a report is the
maintainers' job, not the reporter's.

## Supported versions

There are no versions. Nothing here is released — `RELEASING.md` carries
the commands that say so — so there is no supported release and nothing
to backport to. `main` is the material, and a fix is a commit on it.

## Limitations, not vulnerabilities

These are known and inherent, and each is what the material is *for*.

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
