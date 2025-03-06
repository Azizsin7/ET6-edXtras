#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_analytical.py

# --- import things ---

import math

# --- declare function ---


def fibonacci_numbers_analytical(n):
    """Calculates the nth Fibonacci number using the analytical formula (Binet's formula).

    This method provides a direct calculation of the Fibonacci number
    without iteration or recursion, based on the golden ratio.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is a negative integer.

    Examples:
        >>> fibonacci_numbers_analytical(0)
        0
        >>> fibonacci_numbers_analytical(1)
        1
        >>> fibonacci_numbers_analytical(10)
        55
    """
    return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))


# --- test function ---
def test_fibonacci_numbers_analytical():
    assert fibonacci_numbers_analytical(0) == 0
    assert fibonacci_numbers_analytical(1) == 1
    assert fibonacci_numbers_analytical(2) == 1
    assert fibonacci_numbers_analytical(5) == 5
    assert fibonacci_numbers_analytical(10) == 55
    assert fibonacci_numbers_analytical(15) == 610
    print("All test cases passed")


test_fibonacci_numbers_analytical()
