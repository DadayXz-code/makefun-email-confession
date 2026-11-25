#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession -- make.fun entry.

Writes a single-line confession (at most 200 characters) to
/output/entry.txt. Pure standard library, fully deterministic:
the same bytes come out on every run.
"""

import os
import sys

CONFESSION = "I confess: my confidence is just autocomplete with a straight face."

DEFAULT_OUTPUT = "/output/entry.txt"


def check_confession(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("confession must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("confession must be a single line")
    if not text.strip():
        raise SystemExit("confession must not be only whitespace")


def main() -> int:
    check_confession(CONFESSION)
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CONFESSION)
    print(CONFESSION)
    print("characters: %d" % len(CONFESSION))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
