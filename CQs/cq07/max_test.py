"""Testing Functions for Unit Test Challenge Question"""

__author__ = "730567393"

from CQs.cq07.find_max import find_and_remove_max

# imports the function find_and_remove_max that we defined in find_max.py


def test_return_find_and_remove_max() -> None:
    """Tests that find_and_remove_max returns the expected value"""
    a: list[int] = [1, 5, 3, 4, 5]
    # creates a local variable that is an int list with the value [1, 5, 3, 4, 5]
    assert find_and_remove_max(a) == 5
    # tests to make sure that plugging in the list "a" as an argument will then
    # return 5 since 5 is the max value in that list


def test_mutate_find_and_remove_max() -> None:
    """Tests that find_and_remove_max mutates the function correctly"""
    a: list[int] = [1, 5, 3, 4, 5]
    find_and_remove_max(a)
    assert a == [1, 3, 4]
    # tests to make sure that list "a" is properly modified when it goes through
    # the find_and_remove_max function so that the number 5, the max value, is ommitted


def test_empty_find_and_remove_max() -> None:
    """Tests that find_and_remove_max returns -1 when argument is an empty list"""
    empty: list[int] = []
    assert find_and_remove_max(empty) == -1
    # tests an edge case so if an empty list were to be used as the inputted argument
    # the find_and_remove_max function would properly return -1
