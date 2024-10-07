"""Lists for EX 04"""

__author__ = "730567393"


def all(int_list: list[int], number: int) -> bool:
    # defines a function, all, that has 2 parameters, one list of ints and
    # one int, and returns a bool
    """Returns True if all values of the list are equal to the inputted int"""
    idx: int = 0
    # creates an index int variable with a starting value of 0
    if len(int_list) == 0:
        return False
        # if statement to return False if the list of ints is empty
    while idx < len(int_list):
        # while loop to iterate through each value of the list as
        # long as the index variable is less than the length of the
        # list
        if int_list[idx] == number:
            idx += 1
            # if statement that runs through each value in the int list and sees
            # if it is equal to the value of the number argument
            # if so, it adds one to the index variable and continues through the loop
        else:
            return False
        # in the case that the value of the element in the list is not
        # equal to number, it returns False which exits the function call
    return True
    # in the case where each element of the list is equal to the number
    # variable, it returns True


def max(max_list: list[int]) -> int:
    # defines a function, max, with one parameter, a list of ints,
    # and returns an int
    """Returns the max value in the list of ints"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    # if statement to raise an error message if the list is empty
    idx_max: int = 0
    # creates local int variable to serve as an index
    max_value: int = max_list[idx_max]
    # creates local int varianble that takes on the max
    # value of the elements in the list.
    # it begins equal to the first element and is replaced if the next
    # element is greater
    while idx_max < len(max_list):
        # while loop that continues while the index variable
        # is less than the length of the list.
        if max_list[idx_max] > max_value:
            max_value = max_list[idx_max]
            idx_max += 1
        # if statement for when the element of the list at that index is
        # greater than the current value of the max_value variable.
        # then it adds one to the index variable to continue to iterate
        # through the list elements
        else:
            idx_max += 1
        # else statement which does not replace the current max_value when
        # the element at that index in the list is not greater than the current
        # max_value
    return max_value


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    # defines a function is_equal with 2 parameters, each a list of ints,
    # and returns a bool
    """Compares two lists and returns True if they are equal"""
    idx_list: int = 0
    # creates a local index variable with a starting value of 0
    if len(list_a) != len(list_b):
        return False
    # if statement to return False if the lists are not of equal lengths
    while idx_list < len(list_a) and idx_list < len(list_b):
        # while loop that makes sure the index value is less than the length of
        # each list
        if list_a[idx_list] == list_b[idx_list]:
            idx_list += 1
            # if statement which checks if the value of list_a is equal to the
            # value of list_b at a certain index. then, it adds one to the index
            # variable to continue to iterate through each element of both lists
        else:
            return False
        # returns False in the case that the two lists do not have elements that match
        # at each index
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    # defines a function, extend, that has two int list parameters, and
    # returns nothing
    """Adds list 2 values to the end of list 1"""
    idx_list_2: int = 0
    # creates a local int variable, idx_list_2, with a value of 0
    # to serve as the index
    while idx_list_2 < len(list_2):
        # while loop to continue while the index is less than the length
        # of the list_2
        list_1.append(list_2[idx_list_2])
        # adds the value of list_2 at the specific index (idx_list_2) to the end of
        # list_1 using append
        idx_list_2 += 1
        # adds one to the index variable to continue to iterate through and
        # add each of the elements of list_2 to the end of list_1
    return
