# Repository configuration

What is set on this repository, as the `gh api` call that reads it back
and the answer that call gives today. A setting recorded as prose alone
is one nobody can check; recorded this way, a drift is one command away
from being seen.

The rules and the settings live *outside* the tree: nothing below is
recoverable by reading the repository. What this file covers is the
settings [the standard][std] asks about — the ones [section 16's
checklist][s16] sets on a new repository, and the ones a section of it
states a rule for — together with whatever a call quoted for one of
those answers alongside it. Where that scope ends is *What this file
passes over*, at the foot.

**Where a setting has a reason, the reason is in [the standard][std] and
this file links to it.** Two copies of an argument are two things to keep
true. What is here instead is the answer this repository gives —
including where that is not the answer the sibling repositories give,
and there is more of that here than elsewhere.

**This repository is not a fork**, which is no setting of this file's
but a property the standard reads a sentinel's bar off:

```shell
gh api repos/btclib-org/bbt --jq '{fork, parent: .parent.full_name}'
# {"fork":false,"parent":null}
```

Public and not a fork is the bar the `scorecard` sentinel asks, and
clearing it leaves a tree able to run the sentinel rather than owing it:
[the record of which trees carry which sentinel][s10-carries] does not
name this repository, so there is no `scorecard.yml` here and no
Scorecard badge in `README.md`. Nothing else here turns on the answer:
the divergences from the sibling repositories recorded further down each
carry their own reason where they are read back, and no parent
repository is in any of them.

## Required checks on main

**`Lint`, and nothing else.**

```shell
gh api repos/btclib-org/bbt/branches/main/protection \
  --jq '.required_status_checks | {strict, checks}'
# {"checks":[{"app_id":15368,"context":"Lint"}],"strict":true}
```

`lint.yml` is the workflow that gates, and its `Lint` job is the context
the rule names — one job, so that job is the context, the [aggregate a
required check needs][s10-check] being what a matrix needs. Renaming that
job leaves the context reporting nothing, which blocks every pull
request, so the name belongs to the rule as much as to the file.

No other workflow here is a candidate, and each is out for a reason of
its own. `claude-review.yml` is the ack of record and must not become a
branch rule, for the reason its own header gives. `links.yml` reports
whether somebody else's host is answering, which is not a fact about this
tree and not one a landing should wait on.

`15368` is the Actions app, and a check bound to it cannot be reported by
anything else. Changing the list is a `PATCH` of
`/required_status_checks`, never a `PUT` of the protection object: a
`PUT` sets every field it is given and clears every field it is not, and
this check is the one rule here no ruleset carries a copy of. The
signatures, the linear history and the approving review survive a partial
`PUT` in `main-integrity` and `main-self-merge`, read back in the next
section; `Lint` would not.

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

`COMMIT_OR_PR_TITLE` is the subject — the pull request's title, or the
subject of the single commit where a branch has one. `COMMIT_MESSAGES`
is the branch's own commit messages as the body.

`allow_update_branch` is false, so the *Update branch* button is not
offered; a stale branch is rebased from a checkout instead.

## Features

```shell
gh api repos/btclib-org/bbt \
  --jq '{wiki: .has_wiki, projects: .has_projects, issues: .has_issues,
         discussions: .has_discussions, pages: .has_pages,
         visibility: .visibility, topics: .topics}'
# {"discussions":false,"issues":true,"pages":false,"projects":true,
#  "topics":["bitcoin","bitcoin-core","blockchain","course-materials",
#            "cryptography","digital-signatures","elliptic-curves",
#            "jupyter-notebook","lecture-notes","regtest","spreadsheet",
#            "teaching"],
#  "visibility":"public","wiki":true}
```

The wiki and the projects board are on, and the standard states no rule
about either, so each is this repository's own answer rather than a
divergence from one. `btclib-benchmarks` is the sibling that turns both
off, its own `REPOSITORY.md` giving the reason under *Features that are
off*.

**The topics are `pyproject.toml`'s `keywords`**, which is what [the
standard asks][s3]; the call above sorts them, where that file orders
them by relevance and says why. Half the pair is a repository setting
and half a tracked file, so no command here reads both and a drift
between them is caught by somebody comparing the two.

## Token permissions

```shell
gh api repos/btclib-org/bbt/actions/permissions/workflow
# {"default_workflow_permissions":"read",
#  "can_approve_pull_request_reviews":false}
```

`read`, which is what `lint.yml` needs: it checks the tree out and runs
hooks over it, and pushes nothing back.

A job that needs more elevates there and not in this default.
`claude-review.yml` is the only workflow here whose jobs do, and its
review job and its mention job take the same pair: `pull-requests:
write` to post the comment, and `id-token: write` for the OIDC token
the action mints during its own startup.

```shell
gh api repos/btclib-org/bbt/actions/permissions
# {"enabled":true,"allowed_actions":"all","sha_pinning_required":false}
```

`sha_pinning_required` is false and every action a workflow here uses
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

`.github/dependabot.yml` watches what Dependabot can move here: the
actions the workflows pin by SHA, and `uv.lock`, which the `uv-lock`
hook keeps in step with `pyproject.toml` without moving what it resolves
to. Weekly on Thursday, grouped and with the seven-day cooldown, as
[section 11][s11-deps] asks; the file's own header says why no sentinel
pre-validates what it opens. A pre-commit `rev:` is what an autoupdate
moves, and pre-commit.ci runs one weekly, per the `ci:` block of
`.pre-commit-config.yaml`. A version pinned in a hook's
`additional_dependencies` is reached by neither, an autoupdate
rewriting `rev:` lines and nothing else, so a hand edit is what moves
it. The gate runs
`check-dependabot` over the file, since `check-yaml` alone reads it as
yaml and not as what it is.

```shell
gh api repos/btclib-org/bbt/private-vulnerability-reporting
# {"enabled":true}
```

**Private vulnerability reporting is on**, so *Report a vulnerability* on
this repository's Security tab opens an advisory only the maintainers
see. [The standard gives the policy file to tier 1 and this setting to
every tier][s2-root], and this tree carries no `SECURITY.md` of its own:
the policy its Security tab shows is `btclib-org/.github`'s, and the
button that file sends a reporter to is what this setting puts there.

## What is not configured, and why

- **No publishing and no release workflow.** `CONTRIBUTING.md`'s *A
  version, and no release* is the whole of that answer and carries the
  commands behind it. There is no `pypi` environment and no trusted
  publisher:
  `gh api repos/btclib-org/bbt/environments --jq .total_count` answers
  `0`.
- **No Pages and no Read the Docs.** There is no documentation build:
  what this repository ships is read on github.com or cloned.
- **No suite and no coverage.** [Section 8's ratchet][s8] is a claim
  about a package's own code and this tree ships none. What replaces a
  test here is that a script exits 0, that a transcript notebook
  reproduces its committed outputs, and that what a script prints is
  what the material says it prints; `lint.yml` automates the first two,
  minus the exclusions `CONTRIBUTING.md` names, and the third is a
  person reading what a script printed.

## What this file passes over

*What is not configured, and why* above records what this repository
decided against. This section is the other edge of the scope at the top:
what the API answers for and no section here reaches.

**What no call sets.** `gh api repos/btclib-org/bbt` answers the whole
repository document, most of which is URLs, counts and state GitHub
derives from the tree. None of that is a setting, and nothing here reads
it back.

**A facility nobody reached for.** Actions secrets and variables,
Dependabot secrets, self-hosted runners, webhooks, deploy keys,
autolinks and custom property values each answer empty here, and an
empty answer records no decision. Whichever of them a workflow needs one
day arrives with the section that uses it.

**A field the standard states no rule about, and no call above answers
alongside one it does.** `allow_forking`, `has_downloads`, `is_template`
and `web_commit_signoff_required` are in the repository document and in
none of the `--jq` objects here:

```shell
std=$(gh api repos/btclib-org/.github/contents/README.md --jq .content \
  | base64 -d)
for f in allow_forking has_downloads is_template \
         web_commit_signoff_required; do
  printf '%s %s\n' "$f" "$(printf '%s' "$std" | grep -c "$f")"   # 0 each
done
printf '%s' "$std" | grep -c 'default branch'   # not 0, so those zeros
                                                # are absences
```

Recording a field on no rule grows this file with GitHub's API rather
than with the standard. `merge_commit_title` and `merge_commit_message`
are that case read from the other end: they compose a merge commit
*Merge methods* above reads back as a button this repository does not
offer.

What the scope costs is a silent flip. A change to any of the above
shows up in nothing here, and what would find it is somebody reading the
repository document against this file rather than a command.

[std]: https://github.com/btclib-org/.github
[s2-root]: https://github.com/btclib-org/.github#root-files
[s3]: https://github.com/btclib-org/.github#3-pyprojecttoml-is-the-configuration
[s8]: https://github.com/btclib-org/.github#8-coverage-at-100
[s10]: https://github.com/btclib-org/.github#what-every-workflow-does
[s10-check]: https://github.com/btclib-org/.github#the-aggregate-job-and-the-required-check
[s10-carries]: https://github.com/btclib-org/.github#which-trees-carry-which-sentinel
[s11-deps]: https://github.com/btclib-org/.github#dependabot-and-pre-commitci
[s11-merge]: https://github.com/btclib-org/.github#merge-method
[s11-sigs]: https://github.com/btclib-org/.github#signatures
[s11-tokens]: https://github.com/btclib-org/.github#tokens-publishing-scanning
[s16]: https://github.com/btclib-org/.github#16-checklists
