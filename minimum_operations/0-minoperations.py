#!/usr/bin/python3

def minOperations(n):
    """Calculate the minimum number of operations to reach n 'H' characters."""

    if n <= 1:
        return 0

    operations = 0
    current_length = 1

    while current_length < n:
        if n % current_length == 0:
            operations += 1  # Copy All
            current_length *= 2
    else:
        operations += 1  # Paste

    return operations
