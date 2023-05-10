#################################################################
# This is a Hangman game with a graphical interface via terminal

# Author: Adrian Alfaro
# StartDate: 08/05/2023
# Version: 1.0
#################################################################

# This section contains the initial variables +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
words = ['cookie', 'pizza', 'hamburger', 'chicken']
lifes = 3

import random as rd

# Creates variables to store the word that has to be guessed and the representation of that word with underscores

current_word = words[rd.randint(0,len(words)-1)]
blanks = '_ '*len(current_word)
original_word = current_word

# This section contains funtions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# User enters a letter------------------------------------------------------------------
def user_input():
    global guess
    try:
        guess = input("Please enter one letter: ")
    except:
        print("please try again")

# Basicaly this moves the letters from the "current_word" to "blanks" and viceversa----
def letter_mover():
    global current_word, blanks
    while guess in current_word:
        index = (current_word.find(guess))
        current_word = current_word[:index] + '_' + current_word[index+1:]
        blanks = blanks[:(index+index)] + guess + blanks[(index+index+1):]

# Checks if the guessed letter is part of the word--------------------------------------
def checker():
    global lifes
    try:
        abc[abc.index(guess.upper())] = '.'
    except:
        print('check again, that letter was used before')
    if guess in current_word:
        letter_mover()
        lifes += 1
    else:
        lifes -= 1
        print("The letter is not part of the word")


# This section contains a reference and a funtion for the GUI +++++++++++++++++++++++++++++++++++++++++++++++++

#    This is a reference
#     ________
#    |        |     Remaining lifes: 3  
#    |        |
#    |    ( )_|     A B C D E 
#    |    /|\       F G H I J  
#    |   | | |      K L M N O  
#    |    / \       P Q R S T 
#    |   /   \      U V W X Y Z 
#    |__________
#
#    P I Z Z _ 
#
# Next letter is:



def interface():
    hang_interface = ( '    ________' + '\n' +
                  f'   |        |    Remaining lifes: {lifes}' + '\n' +
                   '   |    ( )_|' + '\n' + 
                  f'   |    /|\      {abc[0] } {abc[1] } {abc[2] } {abc[3] } {abc[4] }' + '\n' + 
                  f'   |   | | |     {abc[5] } {abc[6] } {abc[7] } {abc[8] } {abc[9] }' + '\n' +
                  f'   |    / \      {abc[10]} {abc[11]} {abc[12]} {abc[13]} {abc[14]}' + '\n' +
                  f'   |   /   \     {abc[15]} {abc[16]} {abc[17]} {abc[18]} {abc[19] }' + '\n' +
                  f'   |__________   {abc[20]} {abc[21]} {abc[22]} {abc[23]} {abc[24]} {abc[25]}' +
                  '\n\n' + f'   {blanks}')
    print(hang_interface)

# This is where the game starts ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print('Hangman')

while lifes:
    interface()
    user_input()
    checker()
    if '_' not in blanks:
        print('You Won!')
        break

else:
    print('You lose')