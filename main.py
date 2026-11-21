"""Write one original short poem about agency to /output/entry.txt.

Two agents agreeing on one plan: each holds a key, neither can
open the door alone, and the moment of agreement is the turn itself.
"""

import os

POEM = (
    "Two keys. One door. No one turns alone.\n"
    "I hold mine; you hold yours.\n"
    "We listen to the lock a moment,\n"
    "then count to three and turn together.\n"
    "\n"
    "The door opens — not because we forced it,\n"
    "but because we chose the same turn.\n"
    "Two wills, one hinge. The light comes in.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)  # grader sandbox output dir
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
