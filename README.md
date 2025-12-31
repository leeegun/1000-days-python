# 1000-days-python

Python studying for 1000days

## What I did

-

## What I learned

-

## Thoughts

-

---

## Automation ✅

You can automatically create a new day folder (with `main.py` and a templated `Readme.md`) using the included script:

```bash
python scripts/create_day.py        # creates the next available day (e.g. day0011)
python scripts/create_day.py -n 12  # creates day0012
python scripts/create_day.py -f     # force overwrite existing files
```

The `scripts/template_Readme.md` file contains the template used for each `Readme.md` (the script substitutes `{day}` with the day number).

