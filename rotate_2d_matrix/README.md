# rotate_2d_matrix

This challenge rotates an `n x n` matrix 90 degrees clockwise, in-place, without allocating a second matrix to hold the result. The approach combines two simple in-place steps: first transpose the matrix by swapping each element `[i][j]` with `[j][i]` across the main diagonal, then reverse every row — the combination of the two produces the rotated matrix using only the original memory.

| File | Description |
|---|---|
| `0-rotate_2d_matrix.py` | `rotate_2d_matrix(matrix)` — rotates the given `n x n` matrix 90° clockwise in-place; returns nothing. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
