# Repository instructions

Follow [CONTRIBUTING.md](./CONTRIBUTING.md) for issues, pull requests,
local gates, and worktree setup and cleanup. Use
[REVIEWING.md](./REVIEWING.md) for reviews and read
[REPOSITORY.md](./REPOSITORY.md) before changing workflows or repository
settings.

Work in a worktree of your own, never in the primary checkout: it is the
maintainer's. Follow CONTRIBUTING.md for setup and cleanup.

Choose the least capable model that can reliably complete the task: use a fast
model for straightforward execution, a reasoning-focused model for multi-step
work, and the most capable available model for difficult or ambiguous problems.
Increase capability if progress stalls.

This repository is course material, read or cloned rather than released.
`py-scripts/` holds demonstrations, `ipynb/` holds notebooks with committed
outputs, and `excel/generate.py` generates the spreadsheets. Read the
repository-specific section of REVIEWING.md before changing those materials.
