# Repository configuration

What is set on this repository, as the `gh api` call that reads it back
and the answer that call gives today. A setting recorded as prose alone
is one nobody can check; recorded this way, a drift is one command away
from being seen.

The rules and the settings live *outside* the tree, so this file is the
whole of them: nothing below is recoverable by reading the repository.

**Where a setting has a reason, the reason is in [the standard][std] and
this file links to it.** Two copies of an argument are two things to keep
true. What is here instead is the answer this repository gives —
including where that is not the answer the sibling repositories give,
and there is more of that here than elsewhere.

**This repository is a fork**, which changes nothing above and explains
some of what is below:

```shell
gh api repos/btclib-org/bbt --jq '{fork, parent: .parent.full_name}'
# {"fork":true,"parent":"fametrano/bbt"}
```

## Required checks on main

**There are none.**

```shell
gh api repos/btclib-org/bbt/branches/main/protection \
  --jq 'has("required_status_checks")'
# false
```

`lint.yml` is the workflow that gates, and its `Lint` job is the context
a rule would name — one job, so that job is the context, the [aggregate a
required check needs][s10-check] being what a matrix needs. Until the
rule exists, a red run reports and does not block. `claude-review.yml`'s
job is not a candidate: it is the ack of record and must not become a
branch rule, for the reason its own header gives.

The order is not an oversight and cannot be shortened: a check context
cannot be bound before a workflow has produced it, so the rule is created
after `lint.yml` has run at least once on this repository, and creating
it is not something a pull request can do. The call, for whoever creates
it — a `PUT` sets every field it is given and clears every field it is
not, so this is the whole object rather than the one key being added:

```shell
gh api -X PUT repos/btclib-org/bbt/branches/main/protection \
  --input - <<'JSON'
{"required_status_checks": {"strict": true,
   "checks": [{"context": "Lint", "app_id": 15368}]},
 "enforce_admins": false,
 "required_pull_request_reviews": {"dismiss_stale_reviews": true,
   "required_approving_review_count": 1},
 "restrictions": null,
 "required_linear_history": true,
 "allow_force_pushes": false,
 "allow_deletions": false,
 "required_conversation_resolution": true}
JSON
```

The `checks` array and a JSON body on stdin, never `contexts` and never
`-f`; a later change to the list is a `PATCH` of
`/required_status_checks` rather than a partial `PUT`. `15368` is the
Actions app, and a check bound to it cannot be reported by anything else.

## Branch protection and the rulesets

`main` is the only branch, and everything reaches it through a pull
request. Rules aggregate rather than replace each other, so what holds is
the classic protection *and* the rulesets together:

```shell
gh api repos/btclib-org/bbt/branches/main/protection \
  --jq '{reviews: .required_pull_request_reviews.required_approving_review_count,
         dismiss: .required_pull_request_reviews.dismiss_stale_reviews,
         signatures: .required_signatures.enabled,
         admins: .enforce_admins.enabled,
         linear: .required_linear_history.enabled,
         force: .allow_force_pushes.enabled,
         delete: .allow_deletions.enabled,
         threads: .required_conversation_resolution.enabled}'
# {"admins":false,"delete":false,"dismiss":true,"force":false,
#  "linear":true,"reviews":1,"signatures":true,"threads":true}
```

`enforce_admins: false` is not a relaxation but what makes a solo merge
possible at all, the ruleset bypass below reaching only the ruleset's own
rule.

```shell
gh api repos/btclib-org/bbt/rulesets --jq '.[].id' \
  | xargs -I{} gh api repos/btclib-org/bbt/rulesets/{} \
    --jq '{name, target, enforcement, rules: [.rules[].type],
           bypass: [.bypass_actors[]?.bypass_mode]}'
# {"bypass":[],"enforcement":"active","name":"main-integrity",
#  "rules":["required_signatures","required_linear_history",
#           "non_fast_forward","deletion"],"target":"branch"}
# {"bypass":["pull_request"],"enforcement":"active",
#  "name":"main-self-merge","rules":["pull_request"],"target":"branch"}
# {"bypass":[],"enforcement":"active","name":"tag-integrity",
#  "rules":["required_signatures"],"target":"tag"}
```

- `main-integrity` — required signatures, required linear history, no
  force pushes, no deletions — with **no bypass actor at all**, which is
  what makes every one of those true of an administrator too.
- `main-self-merge` — a pull request, an approving review, stale reviews
  dismissed on push, conversations resolved, and `squash` as the only
  merge method it accepts — bypassed by the maintainer in
  **`pull_request` mode**. That mode against `always` is the whole of the
  design: `always` would mean a direct push to `main` had become
  possible, which is the drift the `bypass` field above is read for.
- `tag-integrity` — required signatures on `refs/tags/v*`, and there is
  no such tag. `CONTRIBUTING.md`'s *A version, and no release* is where
  that is explained rather than removed.

```shell
gh api repos/btclib-org/bbt/rulesets --jq '.[].id' \
  | xargs -I{} gh api repos/btclib-org/bbt/rulesets/{} \
    --jq '.rules[] | select(.type=="pull_request") | .parameters'
# {"allowed_merge_methods":["squash"],
#  "dismiss_stale_reviews_on_push":true,
#  "dismissal_restriction":{"allowed_actors":[],"enabled":false},
#  "require_code_owner_review":false,
#  "require_extra_approval_for_unattributed_changes":true,
#  "require_last_push_approval":false,"required_approving_review_count":1,
#  "required_review_thread_resolution":true,"required_reviewers":[]}
```

## Signed commits

```shell
gh api repos/btclib-org/bbt/commits/main \
  --jq '.commit.verification | {verified, reason}'
# {"reason":"valid","verified":true}
```

`required_signatures` refuses an unsigned commit at the push rather than
noticing it afterwards, and with an empty bypass list it refuses one from
everybody. What the call answers is the signature on whatever landed
last, and [the rule asks for a valid signature and not for a particular
signer][s11-sigs] — a squash composed by GitHub carries its web-flow key
and satisfies it.

What no rule covers is a commit before it is pushed:
`git log -1 --format='%G? %GS'`, an `N` being a defect to fix rather than
to explain.

## Merge methods

```shell
gh api repos/btclib-org/bbt \
  --jq '{squash: .allow_squash_merge, merge: .allow_merge_commit,
         rebase: .allow_rebase_merge, auto: .allow_auto_merge,
         update_branch: .allow_update_branch,
         delete_on_merge: .delete_branch_on_merge,
         title: .squash_merge_commit_title,
         message: .squash_merge_commit_message}'
# {"auto":true,"delete_on_merge":true,"merge":false,
#  "message":"COMMIT_MESSAGES","rebase":false,"squash":true,
#  "title":"COMMIT_OR_PR_TITLE","update_branch":false}
```

[Squash is the only method the standard enables][s11-merge], and the
`main-self-merge` ruleset names it too, so the constraint holds even if
this repository setting is flipped back.

`COMMIT_OR_PR_TITLE` with `COMMIT_MESSAGES` is what makes [a pull
request's title the landing commit's subject][s11-title] and the branch's
own messages its body.

`allow_update_branch` is false, so the *Update branch* button is not
offered; a stale branch is rebased from a checkout instead.

## Features

```shell
gh api repos/btclib-org/bbt \
  --jq '{wiki: .has_wiki, projects: .has_projects, issues: .has_issues,
         discussions: .has_discussions, pages: .has_pages,
         visibility: .visibility, topics: .topics}'
# {"discussions":false,"issues":true,"pages":false,"projects":true,
#  "topics":[],"visibility":"public","wiki":true}
```

The wiki and the projects board are on, where the sibling repositories
turn both off. The standard states no rule about either, so this is a
divergence rather than a decision, and closing it is a settings change
with no diff to review.

**`topics` is empty**, where [the standard has the topics answer to what
the tree holds][s3] and be the same names as `pyproject.toml`'s
`keywords`. Neither exists here: this tree ships no package, so there is
no keyword list for the topics to be read against, and what a reader
searching GitHub for a Bitcoin course finds is nothing.

## Token permissions

```shell
gh api repos/btclib-org/bbt/actions/permissions/workflow
# {"default_workflow_permissions":"read",
#  "can_approve_pull_request_reviews":false}
```

`read`, which is what `lint.yml` needs: it checks the tree out and runs
hooks over it, and nothing here publishes, attests or writes back.
`claude-review.yml` posts a comment, and the `pull-requests: write` that
takes is elevated in that job alone rather than in this default.

```shell
gh api repos/btclib-org/bbt/actions/permissions
# {"enabled":true,"allowed_actions":"all","sha_pinning_required":false}
```

`sha_pinning_required` is false and every action the two workflows use
is pinned to a SHA anyway, which is [what the standard asks of the
workflow][s10] rather than of the setting. The setting would refuse a tag
outright; leaving it off is the sibling repositories' answer too, so this
is not a divergence.

**What these calls cannot say is whether a value is this repository's own
or the organization's**, there being no endpoint that answers. Nobody has
recorded an override here, which is weaker than knowing there is none.

## Secret scanning and Dependabot

```shell
gh api repos/btclib-org/bbt --jq '.security_and_analysis'
# {"dependabot_security_updates":{"status":"enabled"},
#  "secret_scanning":{"status":"enabled"},
#  "secret_scanning_non_provider_patterns":{"status":"disabled"},
#  "secret_scanning_push_protection":{"status":"enabled"},
#  "secret_scanning_validity_checks":{"status":"disabled"}}
```

[The standard asks for secret scanning, its push protection and
Dependabot security updates][s11-tokens], and the call answers `enabled`
to each. What answers `disabled` is plan-gated rather than declined, so
this call reports the setting and not the request.

`.github/dependabot.yml` watches the two things this tree pins and
nothing else moves: the actions `lint.yml` and `claude-review.yml` pin
by SHA, and `uv.lock`, which the `uv-lock` hook keeps in step with
`pyproject.toml` without moving what it resolves to. Weekly on Thursday,
grouped and with the seven-day cooldown, as [section 11][s11-deps]
asks; the file's own header says why no sentinel pre-validates what it
opens. The pre-commit revisions are the third thing pinned here and have
pre-commit.ci's weekly autoupdate instead, per the `ci:` block of
`.pre-commit-config.yaml`. The gate runs `check-dependabot` over the
file, since `check-yaml` alone reads it as yaml and not as what it is.

## What is not configured, and why

- **No publishing and no release workflow.** `CONTRIBUTING.md`'s *A
  version, and no release* is the whole of that answer and carries the
  commands behind it. There is no `pypi` environment and no trusted
  publisher:
  `gh api repos/btclib-org/bbt/environments --jq .total_count` answers
  `0`.
- **No `links.yml`.** It gates nothing anywhere, and it does not exist
  here. It would have a subject — this tree's markdown points at a
  course page, a wallet, a block explorer and a key generator, and one
  of those links rotting is a step a reader cannot follow.
- **No Pages and no Read the Docs.** There is no documentation build:
  what this repository ships is read on github.com or cloned.
- **No suite and no coverage.** [Section 8's ratchet][s8] is a claim
  about a package's own code and this tree ships none. What replaces a
  test here is that a script can be run, which nothing automates.

[std]: https://github.com/btclib-org/.github
[s3]: https://github.com/btclib-org/.github#3-pyprojecttoml-is-the-configuration
[s8]: https://github.com/btclib-org/.github#8-coverage-at-100
[s10]: https://github.com/btclib-org/.github#what-every-workflow-does
[s10-check]: https://github.com/btclib-org/.github#the-aggregate-job-and-the-required-check
[s11-deps]: https://github.com/btclib-org/.github#dependabot-and-pre-commitci
[s11-merge]: https://github.com/btclib-org/.github#merge-method
[s11-sigs]: https://github.com/btclib-org/.github#signatures
[s11-title]: https://github.com/btclib-org/.github#what-a-pull-request-says-it-is
[s11-tokens]: https://github.com/btclib-org/.github#tokens-publishing-scanning
