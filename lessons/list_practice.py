"""Basic syntax of lists"""

# creating an empty list
grocery_list: list[str] = []  # literal
# empty list of strings
my_numbers: list[float] = list()  # constructor
# empty list of floats

grocery_list.append("bananas")

my_numbers.append(1.5)

# literal [] or constructor list() work the same way


# creating an already populatied list:
game_points: list[int] = [102, 86, 94]

# modifying to replace 86 with 72
game_points[1] = 72
game_points.append(102)
# appending with an additional item that is a duplicate is allowed


len(game_points)
# len tells us the length of the list. it starts with 1

game_points.pop(1)

print(game_points)

# function name: display
# parameter: list of integers
# RV: None
# print every element in the input list


def display(int_list: list[int]) -> None:
    print(list)


print(["Kris", "Kaki", "Alyssa"][1])
