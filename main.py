#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence -- a roast of lawmakers who would regulate
AI, crypto or the internet but cannot convert a file to PDF -- to
/output/entry.txt. Stdlib only, deterministic.
"""

import os

# The roast, composed for this bounty: it sets up the lawmakers' authority
# (a 412-page law to govern artificial intelligence) and undercuts it with
# the file they cannot convert -- they have to email their own staff to
# ask how to turn the law itself into a PDF. The punch lands on the last
# few words, and the specific detail (a 412-page law) beats the worn
# tech-illiteracy cliches the judge is told to discount.
ROAST = (
    "Congress wrote a 412-page law to govern artificial intelligence, "
    "then emailed its own staff to ask how to turn the law itself into a PDF."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 320:
        raise ValueError("roast must be 1-320 characters")
    if "\n" in ROAST or ROAST != ROAST.strip():
        raise ValueError("roast must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
