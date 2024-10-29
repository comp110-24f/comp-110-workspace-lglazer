""""Practice with Dictionaries for EX06"""

__author__ = "730567393"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    # defines a function called input_dict that takes a dict[str, str] as a parameter and
    # returns a dict[str, str]
    inverted_dict: dict[str, str] = {}
    # defines a local variable, inverted_dict, which is a dict[str, str]
    for key in input_dict:
        # for in loop that goes through every key in the inputted dict
        if input_dict[key] in inverted_dict:
            # if the value is already found as a key in the inverted_dict,
            # we raise an error
            raise KeyError("You have duplicate keys!")
        inverted_dict[input_dict[key]] = key
        # if the value has not been added yet, this line of code
        # adds the value associated with the key of the inputted dict, as they key of the
        # new inverted dict and sets the value as the key
        # this inverts the dictionary so the previous keys become the values and the values become the keys
    return inverted_dict


# we then return the new, inverted dictionary we have created


def favorite_color(color_dict: dict[str, str]) -> str:
    # defines a function, favorite_color, with a single parameter, color_dict, which is
    # a dict[str, str] and returns a string
    if color_dict == {}:
        return ""
    # this if statement returns an empty string in the case that the inputted
    # dictionary argument was an empty dictionary
    count_color: dict[str, int] = {}
    # defines a local variable,count_color, which is a dict[str, int] that
    # is currently empty
    for name in color_dict:
        # creates a for in loop that goes through every key in the inputted dict
        # the keys are associated with the names of each person and the values
        # are their favorite colors
        if color_dict[name] not in count_color:
            # if statement that is entered if the favorite color
            # (the value associated with the name of the person), is not yet in the
            # count_color dictionary
            count_color[color_dict[name]] = 1
            # this adds a key of the favorite color to the count_color dictionary
            # which is then assigned a value of 1, to count that one person said it
            # was their fave color
        else:
            count_color[color_dict[name]] += 1
            # else statement entered in the case that the color is already
            # entered into the count_color dictionary
            # we add one to the key value for that color to count the additional
            # person who said that it was their favorite color
    popularity: int = 0
    # creates a local variable called popularity that is an int assigned a value of 0
    most_popular: str = ""
    # creates a local variable called most_popular that is a str, currently empty
    for color in count_color:
        # for in loop to iterate over each of the colors in the new count_color
        # dictionary
        if count_color[color] > popularity:
            # if statement that is entered when the value associated with the color key
            # is greater than the most popular color
            popularity = count_color[color]
            # in this case, popularity is assigned the value associated with that color key
            # this allows us to replace the current popularity number with the highest
            # number, meaning the color that was the largest number of people's
            # favorite color
            most_popular = color
            # this also replaces the string most_popular to be updated with the color
            # that was the largest number of people's favorite color
        elif count_color[color] == popularity:
            return most_popular
        # if there is a tie and there are two colors that are equally popular
        # this elif statement returns the color that was first
    return most_popular


# finally, it returns the color that is the most popular


def count(input_list: list[str]) -> dict[str, int]:
    # defines a function, count, that has one list of strings as the parameter
    # and returns a dict[str, int]
    count_dict: dict[str, int] = {}
    # defines a local variable, count_dict, that is a dict[str, int], that is empty
    for element in input_list:
        # using a for in statement, we iterate over each element in the inputted list
        if element in count_dict:
            count_dict[element] += 1
            # this statement adds one to the value associated with the element key in
            # the count_dict, if the element is already a key in the count_dict
        else:
            count_dict[element] = 1
            # in the case where the element is not yet a key in the count_dict
            # dictionary it adds it and assignes the value associated
            # with the key element = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    # defines a function alphabetizer, with one parameter, word_list, that is a
    # list of strings and returns a dict[str, list[str]] meaning the
    # value is a list of strings
    alphabet_word_dict: dict[str, list[str]] = {}
    # defines a local variable, alphaet_word_dict, that is a dict[str, list[str]]
    for word in word_list:
        letter = word[0].lower()
        # for in loop that iterates through every element in the inputted list
        # then assigns letter to be = to first letter of the word in lower case
        if letter not in alphabet_word_dict:
            alphabet_word_dict[letter] = []
            # checks to see if the letter is already a key in the alphabet_word_dict
            # if it is not in the dict, then we add the letter as a key and assign the value
            # as an empty list
        alphabet_word_dict[letter].append(word)
        # appends the word to the list that is the value matched with the letter key
    return alphabet_word_dict  # returns the dictionary created


def update_attendance(
    attendance_dict: dict[str, list[str]], day_of_week: str, name: str
) -> None:
    # defines a function called update_attendance, that has 3 parameters that are a
    # dict[str, list[str]], and two strings, that returns nothing
    if day_of_week not in attendance_dict:
        attendance_dict[day_of_week] = []
        # if statement, checks to see if the inputted string, day_of_week is
        # in the dictionary, attendance_dict, and if not, we add the day of the week as
        # a key with the value as an empty string
    if name not in attendance_dict[day_of_week]:
        attendance_dict[day_of_week].append(name)
        # if statement, that checks to see if the inputted name variable is a key
        # with the inputted dictionary and if not, it appends and adds the name
        # to the key list associated with the day_of_week
