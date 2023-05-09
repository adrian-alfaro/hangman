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


