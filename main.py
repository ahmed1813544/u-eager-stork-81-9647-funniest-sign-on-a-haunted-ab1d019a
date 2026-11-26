"""Write the funniest sign for the door of a haunted server room.

Reads the output directory from MAKEFUN_OUTPUT_DIR (falling back to
/output) and writes the single sign line to entry.txt.
"""

import os

SIGN = (
    "SERVER ROOM: IF YOU HEAR TYPING AND NO ONE IS HERE, "
    "IT'S DAVE. HE NEVER LOGGED OUT."
)


def main() -> None:
    # The gate requires 1-120 characters of non-whitespace text.
    assert 1 <= len(SIGN) <= 120, "sign must be 1-120 characters"
    assert SIGN.strip(), "sign must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SIGN)


if __name__ == "__main__":
    main()
