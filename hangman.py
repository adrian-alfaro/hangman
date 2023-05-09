# This is a hangman game

# Author: Adrian Alfaro
# StartDate: 08/05/2023

words = ['cookie', 'pizza', 'hamburger', 'chicken']

import random as rd

current_word = words[rd.randint(0,len(words))]

print(current_word)