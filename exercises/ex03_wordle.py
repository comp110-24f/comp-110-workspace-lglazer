"""Wordle for EX03"""

__author__ = "730567393"


def input_guess(secret_word_len: int) -> str:
    input_word: str = input(f"Enter a {secret_word_len}-character word: ")
    # creates a global variable called word that takes an input after
    # prompted with a message to enter a word of a specific length
    while len(input_word) != secret_word_len:
        input_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # while loop that ensures that the length of inputted guess word is
        # equal to the length of the secret word
    return input_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    # defines a function that takes two parameters, the secret word and
    # then the guess character (one single letter)
    """Checks a character of the inputted word with the secret word."""
    assert len(char_guess) == 1
    # the assert function ensures that the char_guess argument is only
    # one character
    idx: int = 0
    # creates a local index variable that has an int value of 0 to be used to
    # index through each of the letters in the secret word
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        # the while loop has an if statement contained inside that goes through
        # the secret word and checks each character of the secret word to see if
        # it matches the guessed character
        idx += 1
        # we iterate through the entire word checking each character by adding 1
        # to the index value after each check. the while loop allows us to
        # evaluate each of the letters in the secret word to check for matches
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# these lines create 3 global variables that are strings equivalent to emojis!
# each emoji can be expressed as a specific string code


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    # defines a function that takes two string parameters guess and secret
    # the assert function is used to ensure that the guess argument and the
    # secret argument are of equal lengths
    emoji_str: str = ""
    num_char: int = 0
    while num_char < len(secret):
        # while loop that continues while the index variable called
        # number of characters is less than the length of the secret word
        if contains_char(secret, guess[num_char]) == True:
            # an if statement that calls the contains_char function
            # with the secret word and the guess word as the arguments
            # it checks if the character in the secret word is equal to
            # the corresponding character in the guess word
            if guess[num_char] == secret[num_char]:
                emoji_str += GREEN_BOX
                # within the previous if statement, i created an additional
                # if statement that adds a Green box emoji to the originally empty
                # emoji string variable if the guess character at a particular index
                # is the same as the secret character at that index
                # (for example: if a is the second letter in both the guess word and secret word)
            else:
                emoji_str += YELLOW_BOX
            num_char += 1
            # the corresponding else statement adds a Yellow box emoji to the emoji string variable
            # if the guess character is in the secret word but in a different place
            # then it adds one to the index variable to iterate through each character of the word
        else:
            emoji_str += WHITE_BOX
            num_char += 1
            # an else statement is used if the guess character is not found in the secret word,
            # meaning if the contains_char is == False
    print(emoji_str)
    return emoji_str
    # this is the return statement that prints the completed emoji string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1
    # creates a variable N that starts at 1 and counts the number of turns
    while N <= 6:
        print(f"=== Turn {N}/6 ===")
        # creates a while loop that first prints a statement saying which turn the user is on
        guess: str = input_guess(len(secret))
        # defines a local variable that takes the value of the input of the function input_guess
        emojified(guess, secret)
        # calls the emojified function with the inputted guess
        # adds one to the variable counting the number of turns after
        # completing the function calls which check for character matches
        # in the inputted guessed word and the defined secret word
        if guess == secret:
            print(f"You won in {N}/6 turns!")
            return
            # the if statement checks to see if the guessed word is the same as the secret word
            # if that is true and the inputted guess matches the secret word, it prints a statement
            # saying that the user won in a specific number of turns using the N variable that
            # was used to count turns. then the program is exited
        N += 1
    print("X/6 - Sorry, try again tomorrow!")
    # in the case where the inputted guess is not the secret word after 6 tries,
    # the function prints a statement to share that their guesses were not correct


if __name__ == "__main__":
    main(secret="codes")
