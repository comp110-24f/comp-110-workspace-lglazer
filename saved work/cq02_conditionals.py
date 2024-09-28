"""Conditionals for Challenge Question 02"""

__author__ = "730567393"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number:"))
    print("Your guess was " + str(guess) + ".")
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


# this code creates a new function that has no paramater and no output
# i created a local variable called secret which is an int with a value of 7
# next, i created a local variable called guess which takes on the value of the input
# to receive this input value, it firsts gives instructions: "Guess a number:"
# the depending on the input value it prints a different message using the if elif and else functions

if __name__ == "__main__":
    guess_a_number()
