#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency -- the power to choose and to act --
to /output/entry.txt. Standard library only, no network, deterministic:
every run writes the same text.

Entry for make.fun bounty "the-poem-about-two-agents-20261121-1441".
"""

import os

POEM = (
    "Two minds, two maps, one road between them.\n"
    "I said go left. You said go right.\n"
    "We stopped, and listened to the quiet between us \u2014\n"
    "and there it was: a third way, lit by both our lights.\n"
    "No voice won. No voice was lost.\n"
    "Two wills, one yes \u2014 we chose, and moved as one.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {path} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
