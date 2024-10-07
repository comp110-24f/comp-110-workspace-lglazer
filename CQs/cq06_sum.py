"""Summing the elements of a list using different loops"""

__author__ = "730567393"


def w_sum(vals: list[float]) -> float:
    # defines a function w_sum with one parameter, vals, which
    # is a list of floats and returns a float
    idx: int = 0
    # creates a local index int variable beginning with a value of 0
    sum: float = 0.0
    # defines a local float variable called sum with a value of 0.0
    while idx < len(vals):
        # while loop that continues while the index variable is less than the length
        # of the list of floats
        sum += vals[idx]
        # adds the value of the list at that index to the sum variable
        idx += 1
        # adds one to the index variable so loop can continue to iterate through
        # each value of the list and add each to the sum variable
    return sum


def f_sum(vals: list[float]) -> float:
    # defines a function f_sum with one parameter, vals, which
    # is a list of floats and returns a float
    sum: float = 0.0
    # defines a local float variable called sum with a value of 0.0
    for elem in vals:
        # uses a for in loop to go through each item/element in the list
        sum += elem
        # adds each element of the list to the sum variable
    return sum


def f_range_sum(vals: list[float]) -> float:
    # defines a function f_range_sum with one parameter, vals, which
    # is a list of floats and returns a float
    sum: float = 0.0
    # defines a local float variable called sum with a value of 0.0
    for index in range(0, len(vals)):
        # uses a for in loop that defines a range from 0 index to the length of list,
        # vals, but does not include the end point
        sum += vals[index]
        # this adds the list value at each index to the sum variable and
        # continues using the loop until all items in list have been added
    return sum
