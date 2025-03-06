#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers.py

# --- declare function ---


def fibonacci_numbers(n):
    """
    Calculate the nth Fibonacci number using recursion.

    This function calculates the nth Fibonacci number using a recursive approach.
    It is simple to understand but inefficient for larger values of n due to
    repeated calculations.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        AssertionError: If n is a negative integer.

    Examples:
        >>> fibonacci_numbers(0)
        0
        >>> fibonacci_numbers(1)
        1
        >>> fibonacci_numbers(10)
        55
    """
    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)


# --- test function ---


def test_fibonacci_numbers():
    assert fibonacci_numbers(0) == 0
    assert fibonacci_numbers(1) == 1
    assert fibonacci_numbers(2) == 1
    assert fibonacci_numbers(5) == 5
    assert fibonacci_numbers(10) == 55
    assert fibonacci_numbers(15) == 610
    print("All test cases passed")


test_fibonacci_numbers()
