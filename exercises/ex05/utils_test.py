"""Testing Functions for EX05"""

__author__ = "730567393"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_returns() -> None:
    """Tests that only_evens returns the expected value"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    assert only_evens(a) == [2, 4]
    # asserts, or makes sure, that when the function only_evens
    # is called with list a as the argument, it returns [2, 4]
    # this tests that the function is doing its job and returning
    # a list of only the even elements of the original list

def test_only_evens_mutate() -> None:
    """Tests that only_evens does not mutate the list"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable that is an int list with the value
    # [1, 2, 3, 4, 5]
    only_evens(a)
    # calls only_evens function with list a as the argument
    assert a == [1, 2, 3, 4, 5]
    # asserts, or makes sure that the only_evens function does not mutate
    # or modify the input list


def test_only_evens_edge_case() -> None:
    """Tests that only_evens returns the expected value"""
    b: list[int] = [3, 5, 7, 9]
    # creates a local variable, b, that is an int list with the value
    # [3, 5, 7, 9]
    assert only_evens(b) == []
    # tests an edge case to make sure that in the case that the input
    # list has no even elements, the function will return an empty list


def test_sub_return() -> None:
    """Tests that sub returns the expected value"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    assert sub(a, 1, 3) == [2, 3]
    # asserts, or makes sure, that the sub function works properly
    # by returning the expected output based on the argument inputs


def test_sub_mutate() -> None:
    """Tests that sub does not mutate input list"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4, 5]
    # asserts, or makes sure that the sub function does not mutate
    # or modify the input list


def test_sub_edge_case() -> None:
    """Tests that sub returns empty list if input list is empty"""
    c: list[int] = []
    # creates a local variable, c, that is an empty int list
    assert sub(c, 1, 3) == []
    # tests an edge case to make sure that in the case that the input list
    # argument is an empty list, the sub function returns an empty list


def test_add_at_index_returns() -> None:
    """Tests that add_at_index returns nothing"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    assert add_at_index(a, 2, 0) == None
    # asserts, or makes sure that the add_at_index function does not
    # return anything


def test_add_at_index_mutate() -> None:
    """Tests that add_at_index mutates the input list"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    add_at_index(a, 2, 0)
    assert a == [2, 1, 2, 3, 4, 5]
    # asserts, or makes sure that the add_at_index function
    # works as hoped and modifies the inputted list


def test_add_at_index_edge_case() -> None:
    """Tests that add_at_index raises an error if index is out of range"""
    a: list[int] = [1, 2, 3, 4, 5]
    # creates a local variable, a, that is an int list with the value
    # [1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(a, 2, 10)
    # test to make sure that in the case that the inputted index value is
    # out of range, an index error is raised
