"""Rename the Planet -- make.fun one-liner entry.

The line renames Mercury "Mood Swings". The joke turns on the one
thing Mercury is famous for among the planets: the wildest daily
temperature swing in the solar system, from about -180C at night to
about 430C by day, because it has almost no atmosphere to hold the
heat. The name is a human personality label, and the why makes the
planet sound like a person who is freezing one minute, boiling the
next, and -- the second beat of the joke -- never once apologizes
for the whiplash. The reason only fits Mercury: no other planet
swings that far, that fast, every single day.
"""

import os

# The entry: Mercury gets a new name that fits its extreme daily
# temperature swing -- freezing nights, scorching days, zero remorse.
LINE = 'Mercury is now "Mood Swings": it swings from -180C at night to 430C by day and never once apologizes.'


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()

