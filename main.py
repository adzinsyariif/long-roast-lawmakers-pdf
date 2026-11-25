#!/usr/bin/env python3
"""Write one satirical sentence to /output/entry.txt (UTF-8, no trailing newline)."""

import os

SENTENCE = (
    "Lawmakers who want to license every AI model, ban every crypto wallet "
    "and rewrite the internet still call their 22-year-old staffer "
    "to turn a .docx into a PDF."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(SENTENCE.encode("utf-8"))


if __name__ == "__main__":
    main()
