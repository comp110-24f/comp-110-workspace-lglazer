"""Splitting a dictionary into two lists"""

__author__ = "730567393"


def get_keys(dict: dict[str, int]) -> list[str]:
    # defines a function get_keys with a dictionary with a string key and an int value
    # as a parameter and returns a list of strings
    if len(dict) == 0:
        return []
    # if the length of the dictionary is 0, meaning it is empty,
    # the function will return an empty list
    list_keys: list[str] = []
    # creates a local variable called list_keys which is a list of strings,
    # it begins as an empty list
    for key in dict:
        list_keys.append(key)
        # creates a for in loop that iterates over every key in the dictionary and
        # appends/adds on each key to the list_keys list variable
    return list_keys  # it then returns the complete list of keys


def get_values(dict: dict[str, int]) -> list[int]:
    # defines a function get_values with one parameter, a dictionary
    # with a string key and an int value, and returns a list of ints
    if len(dict) == 0:
        return []
    # if the length of the dictionary is 0, meaning it is empty,
    # the function will return an empty list
    list_values: list[int] = []
    # creates a local variable called list_values which is a list of ints,
    # set equal to an empty list
    for keys in dict:
        list_values.append(dict[keys])
        # creates a for in loop that iterates over every key in the dictionary and
        # appends/adds on each value associated with that key
        # to the list_value list variable.
        # by calling dict[keys] we are getting the value associated with each key
        # in the dictionary
    return list_values  # returns the complete list of values
