"""Entry program for "The Painfully Honest Out-of-Office".

Writes a single painfully honest but still polite out-of-office
auto-reply to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = (
    "Thank you for your email \u2014 I am away until Monday, and I filed "
    "41 requests with my sandbox just to ask permission to reply, so "
    "please allow a few days for my own approval."
)


def main() -> None:
    # Gate: UTF-8 text, 1-200 characters, one sentence, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry is only whitespace"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
