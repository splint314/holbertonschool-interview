# 🧠 Cheat Sheet

Quick-reference explanations of the core idea behind each challenge in this repo, paired with a real-world analogy to make the concept stick.

## Reachability traversal — `lockboxes`

**Concept.** Starting from box `0` (the only box open at the start), repeatedly collect the keys found inside every box you can already open and use them to unlock new boxes. Keep a running list of reached boxes and keep scanning until no new box gets added. All boxes are unlockable if, and only if, that list ends up covering every box.

**Analogy.** Like an escape room: you start with one key on the table, open the drawer it fits, find another key inside, open the next lock with it, and so on — you win only if that chain eventually opens every drawer in the room.

## Streaming aggregation — `log_parsing`

**Concept.** Instead of loading an entire file into memory, read input one line at a time, parse each line, and update a small set of running totals (total size, per-status-code counts). A summary is printed at a fixed interval (every 10 lines) and again at the end, so the program never needs to hold more than "the current totals" in memory.

**Analogy.** Like a cashier keeping a running total on the register tape as items are scanned: the total is updated item by item, and a subtotal gets printed periodically, rather than waiting to add everything up only once the store closes.

## Prime factorization — `minimum_operations`

**Concept.** Starting from a single `"H"`, the only operations are "copy all" then "paste" any number of times. The minimum number of keystrokes to reach exactly `n` characters equals the sum of the prime factors of `n` (with multiplicity) — repeatedly divide `n` by its smallest factor, adding that factor to the operation count each time.

**Analogy.** Like buying a dozen eggs: to get 12 eggs cheaply you reach for a box of 12 (or two boxes of 6, or three of 4) instead of buying 12 single eggs — the cheapest path always breaks the target down into its smallest repeated building blocks, which is exactly what prime factors are.

## Pascal's triangle recurrence — `pascal_triangle`

**Concept.** Each row starts and ends with `1`; every other entry is the sum of the two entries directly above it in the previous row. Building the triangle row by row, and computing each new value from the row already stored, avoids recomputing anything from scratch.

**Analogy.** Like a pinball dropping through a triangular pegboard (a Galton board): the number of ways a ball can land on a given peg equals the sum of the ways it could have arrived from the two pegs directly above it.

## Sieve of Eratosthenes — `primegame`

**Concept.** To know which numbers up to `n` are prime, start by assuming they all are, then walk through the numbers in order and, for every one still marked prime, cross out all of its multiples. Whatever is never crossed out is prime — no trial division of individual numbers needed.

**Analogy.** Like circling `2` on a hundred-chart and crossing out every second number, then circling `3` and crossing out every third number, and so on: whatever survives uncrossed at the end is prime.

## Prefix counts + parity — `primegame`

**Concept.** Once primes up to the largest needed `n` are known, precompute for every value how many primes lie at or below it (a running/prefix count). Two players alternately remove a prime and its multiples from `{1..n}`; the number of primes below `n` determines the winner without simulating the game, because each move removes exactly one prime from play, so parity (odd/even count) decides who runs out of moves first.

**Analogy.** Like knowing in advance who gets the last slice without watching anyone cut the pizza: if you know there's an odd number of slices and everyone takes exactly one turn per slice, the first person to cut is guaranteed to also take the last piece.

## In-place transpose + reverse — `rotate_2d_matrix`

**Concept.** A 90° clockwise rotation of an `n x n` matrix can be done without allocating a second matrix: first transpose the matrix (swap element `[i][j]` with `[j][i]` across the main diagonal), then reverse each row. The two cheap, in-place steps combined produce the same result as a full rotation.

**Analogy.** Like folding a physical paper map along its diagonal crease, then flipping each resulting strip end-to-end: two simple folds on the same sheet of paper produce a rotated map, with no second sheet needed.

## Bitmasking on byte prefixes — `utf8_validation`

**Concept.** A UTF-8 code point is encoded as 1 to 4 bytes; the leading bits of the *first* byte of a sequence announce how many continuation bytes should follow (`0…` = 1 byte total, `110…` = 2 bytes, `1110…` = 3 bytes, `11110…` = 4 bytes), and every continuation byte must start with the bits `10`. Validating a byte stream means reading each byte's top bits, tracking how many continuation bytes are still expected, and rejecting the sequence the moment a byte breaks the pattern.

**Analogy.** Like reading airport connecting-flight signage: the first sign tells you exactly how many more directional signs to expect before you reach your gate, and every one of those follow-up signs must match the expected format — if one doesn't, you know your route is invalid.

---

⬅ back to [README.md](README.md)
