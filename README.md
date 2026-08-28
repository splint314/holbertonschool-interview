# holbertonschool-interview

🧩 Classic technical-interview algorithm challenges, solved in Python.

> 🎓 Part of the Software Engineering curriculum at **Holberton School Toulouse**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-Data%20Structures-informational?style=flat)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)

## 📖 About

This repository is a collection of standalone Python solutions to classic whiteboard-style interview problems, each tackled in its own directory with a single focused script. The exercises span graph reachability, combinatorics, number theory, streaming data processing, in-place matrix manipulation, and bitwise encoding validation. Each solution favors clarity and correct edge-case handling over cleverness, matching what an interviewer typically expects.

## 📂 Project Structure

| Challenge | Problem it solves |
|---|---|
| `lockboxes/` | Given a set of numbered boxes each containing keys to other boxes, determine if every box can eventually be unlocked starting from box 0. |
| `log_parsing/` | Read HTTP access log lines from stdin, accumulate total file size and status-code counts, and print a running summary every 10 lines. |
| `minimum_operations/` | Starting from a single `"H"` on screen, find the minimum number of copy-all/paste operations needed to reach exactly `n` characters. |
| `pascal_triangle/` | Build Pascal's triangle up to `n` rows, where each value is the sum of the two values above it. |
| `primegame/` | Simulate a two-player game where players alternately remove a prime and its multiples from `{1..n}`; determine who wins across multiple rounds. |
| `rotate_2d_matrix/` | Rotate an `n x n` matrix 90 degrees clockwise, in-place, without allocating a second matrix. |
| `utf8_validation/` | Given a list of integers representing bytes, determine whether they form a valid UTF-8 encoded sequence. |

## 🧠 Cheat Sheet

- **Reachability (lockboxes)** — starting from one open box, keep collecting keys and opening whatever they unlock, tracking what's been reached. Like an escape room: you start with one key, open a drawer, find another key inside, and keep going until nothing new opens.
- **Streaming aggregation (log_parsing)** — process input line by line, keeping running totals in memory instead of loading everything at once. Like a cashier keeping a running total on the register tape as items are scanned, printing a receipt every so often rather than waiting until the store closes.
- **Prime factorization (minimum_operations)** — the fewest copy/paste steps to reach `n` equals the sum of `n`'s prime factors. Like buying eggs: to get 12 eggs cheaply you buy a box of 12 (or 2×6, or 3×4) rather than 12 single eggs — breaking the target into its "cheapest" repeated building blocks.
- **Pascal's triangle recurrence** — each entry is the sum of the two entries directly above it, with the triangle edges always equal to 1. Like a pinball dropping through a triangular pegboard (a Galton board): the count at each peg is the sum of the paths that could arrive from the two pegs above it.
- **Sieve of Eratosthenes (primegame)** — cross out multiples of each prime to quickly find all primes up to `n`. Like circling a number on a hundred-chart, then crossing out every multiple of it — whatever survives uncrossed is prime.
- **Prefix counts + parity (primegame)** — precompute how many primes exist up to each number, then use whether that count is odd or even to decide the winner without replaying the game. Like knowing in advance who gets the last slice of pizza just by counting how many slices there are — odd means the first person to cut also gets the last piece.
- **In-place transpose + reverse (rotate_2d_matrix)** — a 90° rotation is achieved by flipping the matrix across its diagonal, then reversing each row, with no extra matrix allocated. Like folding a physical map along its diagonal crease and then flipping each strip end-to-end to get the rotated view, all on the same sheet of paper.
- **Bitmasking (utf8_validation)** — inspect the leading bits of each byte to know how many continuation bytes should follow, then check each continuation byte starts with `10`. Like reading airport signage: the first sign tells you how many more directional signs to expect, and each of those must match the expected format or your route is invalid.

## 📬 Contact

- 💬 Discord: kevin_rigal
- 📧 Email: kevinrigal.contact@gmail.com
- 🐙 GitHub: [@sharingankid](https://github.com/sharingankid)
