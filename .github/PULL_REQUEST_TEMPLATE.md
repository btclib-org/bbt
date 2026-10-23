<!-- markdownlint-disable-next-line first-line-heading -->
## What this changes

<!-- What the code does now that it did not do before, and why.
     Link the issue it closes, if there is one: "Closes #123". -->

## How it was verified

<!-- The test that covers it, the vector it reproduces, the command you
     ran. New behaviour without a test is the usual reason a pull request
     waits. -->

## Checks

<!-- CI runs the gates below, in the locked forms CONTRIBUTING.md
     gives, and rejects the pull request if one fails: the point of
     running them locally is not to wait for CI to tell you. -->

- [ ] the lint gate is clean: `uv run --locked --only-group lint
      pre-commit run --all-files`
- [ ] the transcript notebooks reproduce: `uv run --locked --group
      notebooks python .github/scripts/check_notebooks.py`
- [ ] the scripts still run: `uv run --locked python
      .github/scripts/check_scripts.py`
- [ ] the committed workbooks are generate.py's own output: `uv run
      --locked --group excel python
      .github/scripts/check_generated_workbooks.py`
- [ ] I have read and understood every line of this change, and can
      answer a review of it without the model

## Anything the reviewer should know

<!-- A decision you are unsure of, an alternative you rejected, a
     specification that is ambiguous, a follow-up you left out on
     purpose. Delete the section if there is none. -->
