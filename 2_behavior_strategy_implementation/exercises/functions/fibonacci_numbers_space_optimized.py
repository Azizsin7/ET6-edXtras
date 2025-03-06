#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_space_optimized.py


# --- declare function ---


def fibonacci_numbers_space_optimized(n):
    """
    Calculate the nth Fibonacci number using space optimization.

    This function calculates the nth Fibonacci number using an iterative approach
    that only stores the two most recent Fibonacci numbers, thus optimizing
    space complexity.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        AssertionError: If n is a negative integer.

    Examples:
        >>> fibonacci_numbers_space_optimized(0)
        0
        >>> fibonacci_numbers_space_optimized(1)
        1
        >>> fibonacci_numbers_space_optimized(10)
        55
    """
    a = 0
    b = 1

    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# --- test function ---


def test_fibonacci_numbers_space_optimized():
    """
    Test the fibonacci_numbers_space_optimized function.

    This function includes several assertions to verify that
    fibonacci_numbers_space_optimized returns the correct values
    for various inputs.
    """
    assert fibonacci_numbers_space_optimized(0) == 0
    assert fibonacci_numbers_space_optimized(1) == 1
    assert fibonacci_numbers_space_optimized(2) == 1
    assert fibonacci_numbers_space_optimized(5) == 5
    assert fibonacci_numbers_space_optimized(10) == 55
    assert fibonacci_numbers_space_optimized(15) == 610
    print("All test cases passed for space optimized version")


test_fibonacci_numbers_space_optimized()
