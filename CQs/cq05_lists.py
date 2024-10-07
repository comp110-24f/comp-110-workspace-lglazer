"""Mutating functions."""

__author__ = "730567393"


def manual_append(int_list: list[int], number: int) -> None:
    # defines a function called manual_append that has two parameters,
    # one list of ints and one additional int, with no return value
    int_list.append(number)
    # adds the number argument to the end of the int_list variable using
    # append
    return


def double(input_list: list[int]) -> None:
    # defines a variable called double that has one parameter, which is a list on
    # ints, and has no return value
    idx: int = 0
    # creates a local variable idx, an int with a value of 0, which will serve
    # for indexing
    while idx < len(input_list):
        # a while loop that should be entered as long as the value of the
        # index variable is less than the length of the list
        input_list[idx] = input_list[idx] * 2
        # goes through each index value of the list and edits it to be
        # equal to twice the original value
        idx += 1
        # adds one to idx, the index variable
    return


list_1: list[int] = [1, 2, 3]
# creates a global variable that is a list of ints 1, 2, and 3
list_2: list[int] = list_1
# creates a second global variable that is a list equal to
# the previous global variable list_1

double(list_2)
# calls function double with argument list_2, the global variable


print(list_1)
print(list_2)
# prints the new values for both list 1 and list 2
