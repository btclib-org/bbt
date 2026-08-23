# Releasing

**Nothing here is released.** This repository publishes to no index and
cuts no GitHub release: what it ships, it ships by being read on
github.com and by being cloned. There is no artifact for a version to
name, and `pyproject.toml` declares `package = false` and a placeholder
version for that reason.

Measured rather than asserted, and re-derivable:

```shell
gh api repos/btclib-org/bbt/releases --jq 'length'   # 0
gh api repos/btclib-org/bbt/tags --jq 'length'       # 0
git tag                                              # nothing
```

So this file is not a procedure with a step missing. It is the answer to
the question the standard's section 12 asks of every repository, and the
answer is that the machinery that section describes — calendar
versioning, a signed tag checked against `pyproject.toml`, a reproducible
build, `twine check`, a trusted publisher, a smoke test against the
published wheel — has nothing here to act on.

## What would have to be true first

Recorded so that a later decision to publish is a decision and not a
discovery:

- **There would have to be something to publish.** The tree is
  notebooks, spreadsheets, a regtest walk-through and scripts run from a
  checkout. None of it is imported, so a wheel of it would be a wheel
  nobody installs; what a reader wants is the file, not the package.
- **The scripts would have to run.** They import a btclib layout that no
  longer exists — `pyproject.toml`'s `[tool.mypy]` carries the
  measurement — so a distribution of them would ship code that fails at
  import against its own declared dependency.
- **A version would have to mean something.** Section 12's `YYYY.M.D`
  says when a release was cut, which answers a question a consumer of a
  library has. Course material is dated by the course, and
  <http://www.ametrano.net/bbt/> is where the current slides are.

## The tag rule that already exists

`main` is not the only thing a ruleset covers here:

```shell
gh api repos/btclib-org/bbt/rulesets --jq '.[].id' \
  | xargs -I{} gh api repos/btclib-org/bbt/rulesets/{} \
    --jq 'select(.target=="tag") | {name, conditions, rules: [.rules[].type]}'
# {"conditions":{"ref_name":{"exclude":[],"include":["refs/tags/v*"]}},
#  "name":"tag-integrity","rules":["required_signatures"]}
```

It matches `refs/tags/v*` and there is no such tag, so it enforces
nothing today. That is not a defect to remove: it is the rule being in
place before the first tag rather than after it, which is the order the
required-check rule in `REPOSITORY.md` could not take. Whoever cuts a
first tag here signs it, and finds that out from the push rather than
from this file.
