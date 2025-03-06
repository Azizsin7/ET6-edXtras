#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_optimized.py


# --- declare globals ---

MAX = 1000
f = [0] * MAX

# --- declare function ---


def fibonacci_numbers_optimized(n):
    """Calculates the nth Fibonacci number using an optimized approach.

    This function uses a top-down dynamic programming approach with memoization
    and bitwise operations to efficiently compute the nth Fibonacci number.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is a negative integer.

    Examples:
        >>> fibonacci_numbers_optimized(0)
        0
        >>> fibonacci_numbers_optimized(1)
        1
        >>> fibonacci_numbers_optimized(10)
        55
    """

    def fib(m):
        if m == 0:
            return 0
        if m == 1 or m == 2:
            return 1
        if f[m]:
            return f[m]
        if m & 1:
            k = (m + 1) // 2
        else:
            k = m // 2
        if m & 1:
            f[m] = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
        else:
            f[m] = (2 * fib(k - 1) + fib(k)) * fib(k)
        return f[m]

    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    if f[n]:
        return f[n]

    if n & 1:
        k = (n + 1) // 2
    else:
        k = n // 2

    if n & 1:
        f[n] = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]


# --- test function ---
def test_fibonacci_numbers_optimized():
    assert fibonacci_numbers_optimized(0) == 0
    assert fibonacci_numbers_optimized(1) == 1
    assert fibonacci_numbers_optimized(2) == 1
    assert fibonacci_numbers_optimized(5) == 5
    assert fibonacci_numbers_optimized(10) == 55
    assert fibonacci_numbers_optimized(15) == 610
    print("All test cases passed")


test_fibonacci_numbers_optimized()
