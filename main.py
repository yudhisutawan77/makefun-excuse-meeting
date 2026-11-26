"""One-line excuse for skipping a pointless meeting.

Writes the entry text to the output location the grader expects,
resolving ENTRY_OUT, then MAKEFUN_OUTPUT_DIR, then /output/entry.txt,
with the working directory as a last resort. No trailing newline.
"""

import os
from pathlib import Path


def entry_text():
    return (
        "Can't join \u2014 I'm in a support group for people who attend "
        "too many meetings. It meets at the same time. Every week."
    )


def resolve_output_path():
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        target = Path(entry_out)
        if target.is_dir() or entry_out.endswith(os.sep):
            return target / "entry.txt"
        return target
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path("/output/entry.txt")


def write_entry(target):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(entry_text(), encoding="utf-8")


def main():
    try:
        write_entry(resolve_output_path())
    except OSError:
        write_entry(Path.cwd() / "entry.txt")


if __name__ == "__main__":
    main()
