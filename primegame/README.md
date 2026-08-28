# primegame

Maria and Ben play a game on the set `{1, ..., n}`: they alternate turns (Maria first), each picking a remaining prime number and removing it along with all of its multiples from the set, until a player has no valid move left and loses. This challenge determines the overall winner across `x` rounds, each played with a different `n` from `nums`. Rather than simulating each round, the solution builds a Sieve of Eratosthenes up to the largest `n` needed, precomputes a running count of primes below each value, and uses the parity of that count (odd/even) to decide the winner of each round in constant time.

| File | Description |
|---|---|
| `0-prime_game.py` | `isWinner(x, nums)` — returns `"Maria"`, `"Ben"`, or `None` (tie/no rounds), based on who wins the most of the `x` rounds. |
| `main_0.py` | Sample driver script exercising `isWinner` on a couple of round configurations. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
