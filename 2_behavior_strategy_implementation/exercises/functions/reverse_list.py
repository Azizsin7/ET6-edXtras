#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

# --- declare function ---


def a(b: list) -> list:
    """Creates a reversed copy of a list"""
    c = []
    for item in b:
        c.insert(0, item)
    return c


# --- test function ---


def test_a():
    assert a([1, 2, 3]) == [3, 2, 1]
    assert a(["a", "b", "c"]) == ["c", "b", "a"]
    assert a([]) == []
    print("All test cases passed")


test_a()
