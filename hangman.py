# This is a hangman game

# Author: Adrian Alfaro
# StartDate: 08/05/2023

words = ['cookie', 'pizza', 'hamburger', 'chicken']
lifes = 3

import random as rd

# Creates variables to store the word that has to be guessed and the representation of that word with underscores

current_word = words[rd.randint(0,len(words)-1)]
blanks = '_ '*len(current_word)
original_word = current_word

#----------------------------------------------
def show_status():
    print(original_word)
    print(current_word)
    print(blanks)
    print(lifes)

show_status()
#------------------------------------------------

# Basicaly this moves the letters from the "current_word" to "blanks" and viceversa
def letter_mover():
    global current_word, blanks
    while guess in current_word:
        index = (current_word.find(guess))
        current_word = current_word[:index] + '_' + current_word[index+1:]
        blanks = blanks[:(index+index)] + guess + blanks[(index+index+1):]

# User enters a letter
def user_input():
    global guess
    try:
        guess = input("Please enter one letter: ")
    except:
        print("please try again")

# Checks if the guessed letter is part of the word
user_input()

if guess in current_word:
    letter_mover()
else:
    lifes -= lifes
    print("the letter was not part of the word")


#----------------------------------------------------------------
show_status()
