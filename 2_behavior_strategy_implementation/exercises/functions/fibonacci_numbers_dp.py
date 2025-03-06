#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_dp.py

# --- declare function ---


def fibonacci_numbers_dp(n):
    """Calculates the nth Fibonacci number using dynamic programming.

    This function uses a bottom-up dynamic programming approach to compute the nth Fibonacci number.
    It stores previously computed Fibonacci numbers in a list to avoid redundant calculations.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is a negative integer.

    Examples:
        >>> fibonacci_numbers_dp(0)
        0
        >>> fibonacci_numbers_dp(1)
        1
        >>> fibonacci_numbers_dp(10)
        55
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


# --- test function ---
def test_fibonacci_numbers_dp():
    assert fibonacci_numbers_dp(0) == 0
    assert fibonacci_numbers_dp(1) == 1
    assert fibonacci_numbers_dp(2) == 1
    assert fibonacci_numbers_dp(5) == 5
    assert fibonacci_numbers_dp(10) == 55
    assert fibonacci_numbers_dp(15) == 610
    print("All test cases passed")


test_fibonacci_numbers_dp()
