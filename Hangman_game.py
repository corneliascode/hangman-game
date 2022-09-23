
# imports 

from random_word import RandomWords

import sys

import colorama
from colorama import Fore

# setting this to True will reset color and style settings after each line.
colorama.init(autoreset=True)

# also import this to work not only on your computer 
import os
os.system('color')

import time 


# --------------  Choose the word and the number of allowed mistakes  --------------------

play = True
name = None

while play == True:

    r = RandomWords()
    selected_word = r.get_random_word()
    selected_word = selected_word.lower()

    length_selected_word = len(selected_word)
    mistake = 0
    number_mistake_allowed = length_selected_word
    wrong_letters = list()

# ----------------------------------------------------------------------------------------

# -------------------------  Create the placeholder for guesses  -------------------------

    if name ==  None:
        name = input(Fore.MAGENTA + "Enter your name: ")
        sys.stdout.write("\033[A"*1) # Cursor up 1 line
        sys.stdout.write("\033[J") # Clear the screen
    print(Fore.MAGENTA + "Hello", Fore.MAGENTA+  name + Fore.MAGENTA+ "!")
    print(Fore.MAGENTA +'Welcome to the game and good luck!')
    input(Fore.YELLOW + "Press Enter to start the game")
    sys.stdout.write("\033[A"*3) # Cursor up 3 line
    sys.stdout.write("\033[J") # Clear the screen
    letter_placeholder = list('_')
    word_placeholder = length_selected_word*letter_placeholder
    joined_strings = '  '.join(word_placeholder)
    print(Fore.YELLOW + joined_strings)
    print('') # an empty space between prints
    print('') # an empty space between prints
    print('') # an empty space between prints

# -----------------------------------------------------------------------------------------

# ---------------------------  Main game engine  -----------------------------------------

    while True:
        # ask the user for a letter
        asked_for_letter = input(Fore.BLUE + 'Please choose a letter: ')
        sys.stdout.write("\033[A"*5) # Cursor up 5 line
        sys.stdout.write("\033[J") # Clear the screen

        # force the letter to lowercase
        asked_for_letter = asked_for_letter.lower()

        # if the inserted element is not a letter - ask again
        if not asked_for_letter.isalpha():
            print(Fore.YELLOW +'Use just letters!')
            print('') # an empty space between prints
            print(Fore.YELLOW + joined_strings + '     Wrong letters: ' + joined_wrong_letters)
            print('') # an empty space between prints
            continue
        
        # if there are more than one element - ask again
        if len(asked_for_letter) > 1:
            print(Fore.YELLOW +'Enter just one letter')
            print('') # an empty space between prints
            print(Fore.YELLOW + joined_strings + '     Wrong letters: ' + joined_wrong_letters)
            print('') # an empty space between prints
            continue

        # if the letter was already used - ask again
        if (asked_for_letter in wrong_letters) or (asked_for_letter in word_placeholder):
            print(Fore.YELLOW +'You already use this letter!')
            print('') # an empty space between prints
            print(Fore.YELLOW + joined_strings + '     Wrong letters: ' + joined_wrong_letters)
            print('') # an empty space between prints
            continue

    
        # if the inserted letter is in the word check at which indices and place it in the word placeholder at those indices
        if asked_for_letter in selected_word:
            print(Fore.MAGENTA + 'Good job. The letter is correct!')
            print('') # an empty space between prints
            for i in range(length_selected_word):
                if selected_word[i] == asked_for_letter:
                    word_placeholder[i] = asked_for_letter
            joined_strings = '  '.join(word_placeholder)
            joined_wrong_letters = ', '.join(wrong_letters)
            print(Fore.YELLOW + joined_strings + '     Wrong letters: ' + joined_wrong_letters)
            print('') # an empty space between prints

        # else: if there are less mistakes then maximum allowed, then add the letter to the wrong list and print it, else end the game
        else: 
            if mistake < number_mistake_allowed:
                wrong_letters.append(asked_for_letter)
                mistake = mistake + 1
                joined_wrong_letters = ', '.join(wrong_letters)
                print(Fore.YELLOW + f'Try again! The letter is not correct! You have {mistake} mistakes from {number_mistake_allowed} possible')
                print('') # an empty space between prints
                print(Fore.YELLOW + joined_strings + '      Wrong letters: ' + joined_wrong_letters)
                print('') # an empty space between prints
            else:
                print(Fore.MAGENTA + 'The letter is not correct. You reached maximum amount of mistakes. Game over!')
                print('') # an empty space between prints
                print(Fore.MAGENTA + 'The word was: ' + selected_word)
                print('')
                time.sleep(3)
                break
                
        # if the word is completed - congratulate and end the game
        if '_' not in word_placeholder:
            sys.stdout.write("\033[A"*4) # Cursor up 4 line
            sys.stdout.write("\033[J") # Clear the screen
            print(Fore.MAGENTA+ f'Congratulation, {name}! You guessed the word!')
            print('')
            print('')
            print('')
            time.sleep(3)
            break

    while True:
        sys.stdout.write("\033[A"*4) # Cursor up 4 line
        sys.stdout.write("\033[J") # Clear the screen
        next_round = input(f'{name}, do you want to play another round? (yes or no) ')
        if next_round.lower() == 'yes':
            sys.stdout.write("\033[A"*1) # Cursor up 1 line
            sys.stdout.write("\033[J") # Clear the screen
            break
        elif next_round.lower() == 'no':
            play = False
            sys.stdout.write("\033[A"*1) # Cursor up 1 line
            sys.stdout.write("\033[J") # Clear the screen
            print('Goodbye!')
            time.sleep(3)
            break
        else:
            continue          

# ---------------------------------------------------------------------------------------------------




                







