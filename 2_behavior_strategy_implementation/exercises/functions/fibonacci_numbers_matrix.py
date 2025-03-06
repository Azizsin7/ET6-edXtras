#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_matrix.py

# --- declare helper functions ---


def multiply(F, M):
    """
    Multiplies two 2x2 matrices F and M and updates matrix F with the result.
    Args:
        F (list of list of int): A 2x2 matrix.
        M (list of list of int): A 2x2 matrix.
    Returns:
        None: The function updates matrix F in place.
    """
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1], [1, 0]]

    for _ in range(2, n + 1):
        multiply(F, M)


# --- declare primary function ---


def fib(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)

    return F[0][0]


# --- test function ---
def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(10) == 55
    assert fib(15) == 610
    print("All test cases passed")


test_fib()
