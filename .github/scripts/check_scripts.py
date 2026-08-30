# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Run every demonstration script and require it to exit 0.

The failure course material has is that it stops running: `py-scripts/`
imports `btclib`, so a release renaming something breaks a demonstration
and the exit code is what says so. Each script is run in the environment
`uv.lock` pins.

The `speedup_*.py` benchmarks are among them on purpose, and their
timing output is ignored. What breaks a benchmark here is not becoming
slow, it is the same `AttributeError` a renamed `btclib` gives any other
script, and that the benchmark still runs is what a shared runner can
honestly answer.

What a script prints is compared with nothing. This asks whether a
script runs, where `.github/scripts/check_notebooks.py` asks whether a
notebook still reproduces the outputs committed in it; `py-scripts/`
commits no transcript for that second question to be put to it.

The scripts are discovered rather than listed, so one added tomorrow is
gated without an edit here. What is written down is what a script needs
beyond being run: an exclusion, with its reason beside it, and the stdin
`hash_puzzle.py` reads.

Everything it reads it names, and it fails where it reads nothing: a
gate that opened no file is silent in exactly the way a gate that found
no defect is.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = ROOT / "py-scripts"

# What a script gets before it is called hung. Every one of them prints
# and exits well inside this; the ceiling is here so that a script that
# waits forever is reported by name rather than by the job hitting its
# own timeout with nothing said about which script it was in.
CEILING_SECONDS = 300

# Excluded by name, and a name that is not there is a failure, so that
# renaming a script cannot quietly leave it ungated.
EXCLUSIONS = {
    "ec_explorer.py": (
        "it searches every (a, b) of a fixed range against every x below "
        "each prime it lists, and overruns the ceiling above rather than "
        "merely being slow"
    ),
}

# What a script reads from stdin. `hash_puzzle.py` calls `input()` twice
# and each prompt documents the default an empty line takes, so two
# newlines run the search the material describes.
STDIN = {"hash_puzzle.py": "\n\n"}

# `hash_puzzle.py` calls `plt.show()`, which blocks until a window is
# closed on any interactive backend, so without this it is the ceiling
# above that ends the script rather than the script. It is set for every
# run because it is read by whatever imports matplotlib and by nothing
# else.
BACKEND = "Agg"


def environment() -> dict[str, str]:
    """Return the environment a script is run in."""
    return {**os.environ, "MPLBACKEND": BACKEND}


def ran(path: Path, name: str) -> str:
    """Run one script and say what is wrong with it, or nothing."""
    try:
        # the interpreter is the one running this file, and its
        # argument is a path globbed out of py-scripts/ in this
        # checkout: S603 asks after untrusted input, and no element of
        # this argument list comes from outside the tree
        completed = subprocess.run(  # noqa: S603
            [sys.executable, str(path)],
            input=STDIN.get(path.name, ""),
            capture_output=True,
            encoding="utf-8",
            cwd=ROOT,
            env=environment(),
            timeout=CEILING_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return f"  {name} did not finish in {CEILING_SECONDS} seconds"
    if completed.returncode == 0:
        return ""
    detail = [f"  {name} exited {completed.returncode}"]
    detail.extend(
        stream for stream in (completed.stdout, completed.stderr) if stream
    )
    return "\n".join(detail)


def main() -> int:
    """Run every script that is not excluded, and name every file read."""
    failures = []
    scripts = [
        path
        for path in sorted(SCRIPT_DIR.glob("*.py"))
        if path.name not in EXCLUSIONS
    ]
    if not scripts:
        failures.append("  py-scripts/: no script, so nothing was read")
    for path in scripts:
        name = path.relative_to(ROOT).as_posix()
        failure = ran(path, name)
        # flush=True because the ceiling above is only half the promise.
        # A run: step's stdout is a pipe, so print block-buffers, and a
        # job that hits its own timeout-minutes mid-loop dies with the
        # buffer unwritten -- naming no script, which is the outcome the
        # ceiling exists to prevent. Flushed, the log names every script
        # that finished before the job ran out.
        print(f"{name}: {'failed' if failure else 'ran'}", flush=True)
        if failure:
            failures.append(failure)
    for name, reason in EXCLUSIONS.items():
        if (SCRIPT_DIR / name).exists():
            print(f"py-scripts/{name}: not run, {reason}")
        else:
            failures.append(f"  py-scripts/{name}: excluded and not there")
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
