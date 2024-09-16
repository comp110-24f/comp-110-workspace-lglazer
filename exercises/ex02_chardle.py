"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730567393"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 4")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 5")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
