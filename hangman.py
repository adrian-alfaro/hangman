# This is a hangman game

# Author: Adrian Alfaro
# StartDate: 08/05/2023

words = ['cookie', 'pizza', 'hamburger', 'chicken']

import random as rd

# Selects a random word and assigns it to a variable
current_word = words[rd.randint(0,len(words)-1)]
# Creates a string of underscores, one per letter
spaces_word = '_ '*len(current_word)

print(current_word)
print(spaces_word)

current_guess = input("Please enter one letter: ")

while current_guess in current_word:
    print("nice!")
    index = (current_word.find(current_guess))
    if index != -1:
        spaces_word[index+index] = current_guess
        current_word[index] = "_"


def replacer():
    while index:
        pass
