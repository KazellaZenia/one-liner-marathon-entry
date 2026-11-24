"""One-Liner Marathon entry: a single joke, written to the grader's output dir.

The joke is one line of plain text. Nothing is read from the network, from
git history, or from anywhere outside this file; the output is fully
determined by the constant below, so two runs are byte-identical.
"""

from pathlib import Path
import os

# The entry: an AI assistant that treats its human the way humans treat
# each other in calendar invites. The punchline lands on the last two
# words, and every word before them is setup for it.
JOKE = "My AI assistant scheduled a meeting with itself about my productivity, then marked me optional."

# The gate's own limits, checked here before writing so a bad line fails
# loudly in development instead of silently failing the sealed scorer.
MAX_CHARS = 280


def check_joke(text: str) -> None:
    """Refuse anything the gate would refuse: empty, overlong, or multi-line."""
    if not text.strip():
        raise SystemExit("joke is blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"joke is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")


def entry_path() -> Path:
    """Where the grader expects the text: MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    return Path(out_dir) / "entry.txt"


def write_entry() -> Path:
    check_joke(JOKE)
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, and the line is the joke.
    target.write_text(JOKE, encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
