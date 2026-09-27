# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Execute the transcript notebooks and compare them with what is committed.

`ipynb/README.md` promises that executing one of them gives back every
output stored in it, and this is what holds that promise: each is run in
the environment `uv.lock` pins, and every code cell's outputs and
execution count are compared with the committed file's.

What execution rewrites and this does not compare is the notebook's own
`language_info`, which describes the running interpreter, and each cell's
`execution` metadata, which is wall clock. Comparing either would make a
notebook stop reproducing itself on the very next run.

Everything it reads it names, and it fails where it reads nothing: a
gate that opened no file is silent in exactly the way a gate that found
no defect is.
"""

import difflib
import json
import sys
from pathlib import Path
from typing import Any

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "ipynb"

# `PartialHashInversion.ipynb` is an illustration rather than a
# transcript: its first cell calls `input()` twice, so headless it raises
# `StdinNotImplementedError` before computing anything. It is named here
# rather than detected, and a name that is not there is a failure, so
# that renaming a notebook cannot quietly leave it unchecked.
ILLUSTRATIONS = ("PartialHashInversion.ipynb",)

# The line that makes a code cell provisioning. It is neither run nor
# compared, and one reason covers both, `ipynb/README.md` giving it:
# what that line prints describes the reader's machine rather than the
# material. Not running it also keeps the notebooks off the network, so
# what they are compared against is the btclib `uv.lock` pins.
PROVISIONING = "!pip install"


def source_text(cell: Any) -> str:
    """Return a cell's source as one string, however the cell was parsed."""
    source = cell["source"]
    return source if isinstance(source, str) else "".join(source)


def is_provisioning(cell: Any) -> bool:
    """Say whether a code cell installs the library rather than teaching."""
    return any(
        line.startswith(PROVISIONING) for line in source_text(cell).splitlines()
    )


def code_cells(document: Any) -> list[Any]:
    """Return a parsed notebook's code cells, in document order."""
    return [cell for cell in document["cells"] if cell["cell_type"] == "code"]


def executed(path: Path) -> Any:
    """Run a notebook and return what `nbformat` would write for it.

    The result is parsed back from that serialisation rather than read off
    the objects: `nbformat` holds every `text/*` entry of a result's or a
    display's data, and an SVG's, as one string in memory and as a list of
    lines on disk, so comparing the committed file against the objects
    reports every cell carrying one as differing.
    """
    # nbformat ships `py.typed` and leaves `read` and `writes` unannotated,
    # so each call carries its own ignore rather than a [tool.mypy] setting
    notebook = nbformat.read(path, as_version=4)  # type: ignore[no-untyped-call]
    for cell in code_cells(notebook):
        if is_provisioning(cell):
            cell.source = "\n".join(
                line
                for line in source_text(cell).splitlines()
                if not line.startswith(PROVISIONING)
            )
    NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    ).execute()
    return json.loads(nbformat.writes(notebook))  # type: ignore[no-untyped-call]


def transcript(cell: Any) -> str:
    """Return what a reader of the committed notebook sees of one cell."""
    return json.dumps(
        {
            "execution_count": cell.get("execution_count"),
            "outputs": cell.get("outputs"),
        },
        indent=2,
        sort_keys=True,
    )


def departure(name: str, index: int, was: Any, now: Any) -> str:
    """Say which cell departed from the committed notebook, and how."""
    delta = difflib.unified_diff(
        transcript(was).splitlines(),
        transcript(now).splitlines(),
        fromfile="committed",
        tofile="fresh",
        lineterm="",
    )
    lines = source_text(was).splitlines()
    heading = lines[0] if lines else ""
    return "\n".join([f"  {name} code cell {index}, {heading!r}", *delta])


def merged_streams(cell: Any) -> Any:
    """Return a cell whose consecutive same-name streams are one output.

    The kernel may deliver one print's text in two stream messages, and
    nbclient stores each message as an output of its own, so where the
    boundary falls depends on the machine rather than on the notebook.
    Joining the text of consecutive outputs of one stream, on both sides,
    compares what a reader sees rather than where the messages broke.
    """
    outputs: list[Any] = []
    for output in cell.get("outputs") or []:
        if output.get("output_type") != "stream":
            outputs.append(output)
            continue
        text = output["text"]
        text = text if isinstance(text, str) else "".join(text)
        last = outputs[-1] if outputs else None
        if (
            last is not None
            and last.get("output_type") == "stream"
            and last["name"] == output["name"]
        ):
            last["text"] += text
        else:
            outputs.append({**output, "text": text})
    # back into lines, so that a departure diffs line by line
    for output in outputs:
        if output.get("output_type") == "stream":
            output["text"] = output["text"].splitlines(keepends=True)
    return {**cell, "outputs": outputs}


def departures(path: Path, name: str) -> list[str]:
    """Report every code cell whose fresh run departs from the committed one."""
    committed = code_cells(json.loads(path.read_text(encoding="utf-8")))
    fresh = code_cells(executed(path))
    found = []
    for index, (read, ran) in enumerate(zip(committed, fresh, strict=True)):
        if is_provisioning(read):
            continue
        was, now = merged_streams(read), merged_streams(ran)
        outputs_agree = was.get("outputs") == now.get("outputs")
        counts_agree = was.get("execution_count") == now.get("execution_count")
        if not (outputs_agree and counts_agree):
            found.append(departure(name, index, was, now))
    return found


def raised(name: str, error: Exception) -> str:
    """Say which notebook's execution raised, and with what error."""
    return "\n".join([f"  {name} raised executing a cell:", str(error)])


def main() -> int:
    """Check every transcript notebook, and name every file it reads."""
    failures = []
    transcripts = [
        path
        for path in sorted(NOTEBOOK_DIR.glob("*.ipynb"))
        if path.name not in ILLUSTRATIONS
    ]
    if not transcripts:
        failures.append("  ipynb/: no transcript notebook, so nothing was read")
    for path in transcripts:
        name = path.relative_to(ROOT).as_posix()
        # a cell that raises is a departure like any other: collected and
        # not left to abort the run, or every notebook after it goes
        # unread and unreported. Blind on purpose: nbclient's own
        # execution can raise more than one exception type, and a
        # narrower except would leave exactly those doing what this
        # function exists to prevent
        try:
            found = departures(path, name)
        except Exception as error:  # noqa: BLE001
            print(f"{name}: raised executing a cell")
            failures.append(raised(name, error))
            continue
        print(f"{name}: {'differs from' if found else 'reproduces'} its outputs")
        failures.extend(found)
    for name in ILLUSTRATIONS:
        if (NOTEBOOK_DIR / name).exists():
            print(f"ipynb/{name}: illustration, not executed")
        else:
            failures.append(f"  ipynb/{name}: named an illustration and not there")
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
