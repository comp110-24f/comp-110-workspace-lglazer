"""While Loops for Challenge Question 03"""

__author__ = "730567393"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    print(count)
    return count


# defined a function num_instances that takes two parameters, phrase and search_char
# which are both strings and returns an int. then i defined two local variables index
# and count. index is the variable to signify which letter of the phrase will be
# compared to the search character. count is the variable which counts the number
# of times the character is in the word. i use a while loop to continue while the number
# index is less than the length of the phrase. then,i use an if-else statement. if that letter of the phrase is the
# same as the search_char, then, we add 1 to count and 1 to index so we move to check the next
# letter in the phrase. if not, we still add one to the index so we can check the next letter
# but we do not add anything to count. then, we print the resulting count and return count.
