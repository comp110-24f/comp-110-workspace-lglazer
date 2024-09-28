"""Coordinates for Challenge Question 04"""

__author__ = "730567393"


def get_coords(xs: str, ys: str) -> None:
    idx_x: int = 0
    # creates new variable with value 0
    while idx_x < len(xs):
        # creates while loop that checks to ensure the index variable is less than the
        # length of the string
        idx_y: int = 0
        # creates an additional new variable with value 0
        while idx_y < len(ys):
            print("(" + xs[idx_x] + ", " + ys[idx_y] + ")")
            # prints a string that goes through a character of the string arguments
            # according to the number of the index variable and adds them together
            idx_y += 1
            # adds 1 to the value of the y-index variable so it can continue the while
            # loop until it reaches the end of the string
        idx_x += 1
        # adds 1 to the value of the x-index variable so it can continue the while loop
        # until it reaches the end of the string


# defines a function get_coords with two parameters and goes through
# each character of the parameter strings and matches each character of
# one string with the other.
