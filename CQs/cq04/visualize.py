"""Visualize for Challenge Question 04"""

__author__ = "730567393"


from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# these lines are importing functions that were defined in different docs
# you explicitly need to say where they can find the definition

x: str = "123"
y: str = "abc"

# these lines create two new global variable

print(concat(x, y))
get_coords(x, y)

# calling functions and using global variables as arguments
