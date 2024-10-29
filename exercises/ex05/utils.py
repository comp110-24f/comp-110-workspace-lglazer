"""Writing Functions for EX05"""

__author__ = "730567393"


def only_evens(input: list[int]) -> list[int]:
    # defines a function only_evens which has one parameter,
    # a list of ints, and returns another list of ints
    even_list: list[int] = []
    # creates a local variable even_list which is an empty int list
    for element in input:
        # creates a for in loop to go over every element in the
        # input list
        if element % 2 == 0:
            even_list.append(element)
            # if the element is even, which we test by seeing if there is
            # no remainder "%" when divided by 2, we append the new list with
            # the element, which means we add the even element to the end of the
            # new list
    return even_list  # we then return the even list


def sub(int_list: list[int], idx_start: int, idx_end: int) -> list[int]:
    # defines a function sub which has 3 parameters, one int list, and two ints,
    # and returns an int list
    if idx_start < 0:
        idx_start = 0
        # in the case that the starting index is negative, we treat it as if
        # the starting index is 0 so we begin at the start of the list
    if idx_end > len(int_list):
        idx_end = len(int_list)
        # in the case that the ending index is greater than the length of the
        # input list, we treat the end index as the length of the list so
        # we continue until the end of the list
    if len(int_list) == 0:
        return []
        # in the case that the list is empty, we return the empty list
    if idx_start >= len(int_list):
        return []
        # in the case that the starting index is greater or equal to the
        # length of the list, we return an empty list
    if idx_end < 0:
        return []
        # in the case that the ending index is negative, we return an empty list
    new_list: list[int] = [int_list[idx_start]]
    # we define a new local variable that is an int list with the only element
    # being the element of the input list argument at the starting index
    idx: int = idx_start + 1
    # we define a new local int variable that is equal to the value of the starting
    # index + 1
    while idx < idx_end:
        # we create a while loop to continue until our index variable reaches
        # the index end
        new_list.append(int_list[idx])
        # we append the new list with the value of the input list at the index.
        # this will add values to the end of the new list and creates a list
        # with the original inputted list elements from the starting point
        # until the ending index
        idx += 1
        # we then add one to the index to iterate through each element until reaching
        # the end idex
    return new_list


def add_at_index(input_list: list[int], element: int, idx: int) -> None:
    # defines a function which has 3 parameters, one int list, and two ints,
    # and returns none
    if idx < 0 or idx > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
        # in the case that the inputted index is negative or greater than
        # the length of the input list, we raise an error
    input_list.append(0)
    # we add 0 to the end of the input list as a place holder
    move_int: int = len(input_list) - 1
    # creates a local int variable with the value of 1 less than
    # the length of the input list
    while move_int > idx:
        # a while loop that continues while our move_int is less
        # than the inputted index argument
        input_list[move_int] = input_list[move_int - 1]
        # takes the inputted list element at the move_int index and
        # makes it equal to the inputted list element at the index prior.
        # this shifts each value by one until idx
        move_int -= 1
        # we then subtract one from the move_int variable to move through
        # each element in the list until the declared idx
    input_list[idx] = element
    # at the desired index, we can now insert the element without erasing any
    # previous values as we shiffted everything over to make room for the new input