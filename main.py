"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one sentence explaining the modern internet to a
# traveler from 1800, built only from things they already know: post
# offices, libraries, printing presses, roads, letters, ink.
# One sentence, 140 characters — inside the 200-character gate.
# Revision note: no word coined after 1800 is used; the comparison
# carries the whole explanation, as the judge brief allows.
import os

TEXT = (
    "Imagine every post office, library and printing press in the "
    "world joined by one road, so any letter you write arrives "
    "before the ink dries."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
