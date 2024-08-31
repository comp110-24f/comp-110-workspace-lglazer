"""Planning a Tea Party: Exercise 1"""

__author__: str = "730567393"


def main_planner(guests: int) -> None:
    """Calls the other function definitions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


# main planner function defined to call each of the following functions
# and produce the printed outputs by calling each of the functions and
# calculating the outputs based on the number of guests
# the outputs had to be turned from an int into a str


def tea_bags(people: int) -> int:
    """Calculate number of teabags needed based on number of party goers"""
    return people * 2


# defined function tea_bags by describing the parameters
# and telling it to give me back 2x number of people


def treats(people: int) -> int:
    """Calculate number of treats needed based on number of teas a guest drinks"""
    return int(tea_bags(people=people) * 1.5)


# defined function treats by describing the parameters
# and telling it to return the function tea_bags with the input being equal
# to the input of treats. then we multiply the number of teabags by 1.5 and turn that into an integer


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of total number of treats and tea bags"""
    return tea_count * 0.5 + treat_count * 0.75


# defined function cost by describing the parameters
# as tea_count which is the number of tea bags needed and
# treat_count which is the number of treats needed
# then, taking into account the cost of each item, we multiply tea_count by .5
# and multiply treat_count by .75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
