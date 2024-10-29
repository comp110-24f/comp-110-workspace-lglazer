"""Function Writing for Unit Test Challenge Question"""

__author__ = "730567393"


def find_and_remove_max(list_input: list[int]) -> int:
    # defines a function find_and_remove_max with one parameter,
    # a list of ints, and returns an int
    if len(list_input) == 0:
        return -1
    # if statement that says if the list is empty
    # return -1
    idx: int = 0
    # creates an int variable for the index set to 0
    max_element: int = list_input[0]
    # creates a local int variable for the max value
    # beginning with the value equal to the first element in the list
    while idx < len(list_input):
        # while loop that continues while the index is less than the length
        # of the list
        if max_element < list_input[idx]:
            max_element = list_input[idx]
        # if statement that says if the max_element variable is less than the current
        # element of the list at the index value, replace max_element with the value
        # of the current element
        idx += 1
        # then it adds one to the index so we iterate through the list
    idx_2: int = 0
    # creates a second index variable with a value of 0
    while idx_2 < len(list_input):
        # while loop to allow us to iterate through each element
        # in the list while the index is less than the length of the list
        if max_element == list_input[idx_2]:
            list_input.pop(idx_2)
        # if statement that claims if the max_element is equal to the value
        # of the list element at the particular index, delete that value from the list.
        # this is so that we can remove the max value from the list
        else:
            idx_2 += 1
        # if not matching add one so we can check each element in the list and remove all
        # elements that are the max value. it must be in else so that we recheck the
        # new element at the index after deleting the max value.
    return max_element


# we then return the max_element which would be the list element with the largest value
