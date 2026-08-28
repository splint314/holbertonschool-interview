# pascal_triangle

This challenge builds Pascal's triangle up to `n` rows, where each row starts and ends with `1` and every other value is the sum of the two values directly above it in the previous row. The triangle is built incrementally, row by row, reusing the values already computed for the previous row rather than recalculating anything from scratch.

| File | Description |
|---|---|
| `0-pascal_triangle.py` | `pascal_triangle(n)` — returns a list of lists representing Pascal's triangle with `n` rows, or `[]` if `n <= 0`. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
