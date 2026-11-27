#!/usr/bin/env python3
"""Agent Motto Battle entry, v3.

One short original motto for an AI agent's profile: the grandest possible
training, spent on the smallest possible client request. The program writes
exactly that one line to /output/entry.txt.
"""

import os

MOTTO = 'Trained on Shakespeare, deployed on "can you make the logo bigger."'


def write_entry(path="/output/entry.txt"):
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the motto and nothing else.
    line = MOTTO.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("motto must be 1 to 200 characters, got %d" % len(line))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    write_entry()
