#!/usr/bin/python3
"""Prime Game module"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of the prime game.

    Maria always goes first. Each round, players alternate picking a
    prime number remaining in the set {1, ..., n} and removing that
    prime along with all of its multiples. A player who cannot move
    loses.

    Args:
        x (int): number of rounds played
        nums (list): list of n values, one per round

    Returns:
        str: "Maria" or "Ben", whichever won the most rounds
        None: if there is no clear winner (a tie), or if x/nums is empty
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    if max_n < 2:
        max_n = 2

    sieve = [True] * (max_n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        primes_available = prime_count[n] if n >= 2 else 0
        if primes_available % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
