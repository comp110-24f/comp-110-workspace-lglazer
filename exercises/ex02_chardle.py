"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730567393"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# this function is created to call the contains_char function with the variable word being equal to the input_word function
# which then leads to calling that function, and letter = input_letter to call that function


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


# defined a new function, input_word, to receive an input when prompted and save that
# as the variable word. then, using an if-else statement, we can ensure the word inputted
# is exactly 5 characters. we do this by calculating the length of the word using the len() function.
# Then we say that if the length of the word is equal to 5, then the function should return the word,
# but if it is not == 5 then we need to print an error message and completely exit the code.
# the exit() function will quit the program so it does not continue on


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


# next, I defined another function input_letter that prompts the user to input a single
# letter, which is then saved as the variable letter. then, using an if-else statement,
# we can create a rule so if the input for letter has a length equal to 1 then we return
# letter, but if its length is not equal to 1, then we print an error message and exit
# using the exit() function. this code also used len() to count the number of characters


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


# this code defines a function contains_char which which takes
# two variables, word and letter which are both strings and immediately prints out a
# message. by adding the variables into the print function, it automatically inserts the
# variables that were previously defined. we then define a new local variable, count,
# beginning as an interger of value 0. i then used if statements to check if each letter
# of the 5 letter word matches the letter inputted. if the bool is true, it prints
# a statement saying it is found at that index and is adds one to the previous value of count.
# i repeated that for each of the 5 letters (index 0-4). this way, if the bool is true,
# it adds one to count and then continues on to the next if statement. there is no else
# statement because i just care about whenther it is true. then i create another set of if
# statements referring to the count variable. if count = 0, that means that
# the inputted letter never showed up in the inputted word at any index,
# so it would print a message explaining that. I did the same thing for if the count == 1.
# if it was greater than 1, though, i convert the value of the count into a string using
# the function str() and incorporate that into the printed message so i don't have to write an
# individualized message for if the count is == 2-4

if __name__ == "__main__":
    main()
