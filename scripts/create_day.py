"""Create a day folder with a templated Readme.md and a starter main.py.

Usage:
  python scripts/create_day.py            # create next available day (day0001, day0002...)
  python scripts/create_day.py --number 12   # create day0012
  python scripts/create_day.py --force     # overwrite files if they exist
"""

import argparse
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).resolve().parent / "template_Readme.md"

DAY_DIR_RE = re.compile(r"^day(\d{4})$")


def find_next_day(root: Path) -> int:
    max_n = 0
    for p in root.iterdir():
        if p.is_dir():
            m = DAY_DIR_RE.match(p.name)
            if m:
                n = int(m.group(1))
                if n > max_n:
                    max_n = n
    return max_n + 1


def format_day_name(n: int) -> str:
    return f"day{n:04d}"


def create_day(n: int, force: bool = False) -> Path:
    name = format_day_name(n)
    day_path = ROOT / name
    day_path.mkdir(parents=True, exist_ok=True)

    main_py = day_path / "main.py"
    readme = day_path / "Readme.md"

    if not main_py.exists() or force:
        main_py.write_text(
            """# {name} - 

if __name__ == '__main__':
    print('Hello from {name}')
""".format(
                name=name
            )
        )

    if TEMPLATE.exists():
        tmpl = TEMPLATE.read_text()
    else:
        tmpl = "# Day {day}\n\n## What I did\n\n-\n\n## What I learned\n\n-\n\n## Thoughts\n\n-\n"

    content = tmpl.format(day=n)

    if not readme.exists() or force:
        readme.write_text(content)

    return day_path


def main():
    p = argparse.ArgumentParser(description="Create day folder with template Readme.md")
    p.add_argument(
        "--number", "-n", type=int, help="Day number to create (e.g. 12 -> day0012)"
    )
    p.add_argument(
        "--force", "-f", action="store_true", help="Overwrite existing files"
    )
    args = p.parse_args()

    if args.number:
        day_no = args.number
    else:
        day_no = find_next_day(ROOT)

    day_path = create_day(day_no, force=args.force)
    print(f"Created {day_path}")


if __name__ == "__main__":
    main()
