# minimum_operations

Starting from a text file containing a single `"H"` character, the only two operations available are "Copy All" and "Paste". This challenge computes the minimum number of operations needed to end up with exactly `n` `"H"` characters. The approach repeatedly divides `n` by its smallest remaining prime factor, adding that factor to the operation count each time — the minimum operation count is simply the sum of `n`'s prime factors (with multiplicity).

| File | Description |
|---|---|
| `0-minoperations.py` | `minOperations(n)` — returns the minimum number of copy/paste operations to reach `n` characters, or `0` if it's impossible (`n <= 1`). |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
