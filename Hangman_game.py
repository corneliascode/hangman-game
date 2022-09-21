
# imports 

from random_word import RandomWords


# --------------  Choose the word and the number of allowed mistakes  --------------------

r = RandomWords()
selected_word = r.get_random_word()
selected_word = selected_word.lower()

length_selected_word = len(selected_word)
mistake = 0
number_mistake_allowed = length_selected_word + 3
wrong_letters = list()

# ----------------------------------------------------------------------------------------

# -------------------------  Create the placeholder for guesses  -------------------------

print('Welcome to the game!')
letter_placeholder = list('_')
word_placeholder = length_selected_word*letter_placeholder
joined_strings = '  '.join(word_placeholder)
print(joined_strings)

# -----------------------------------------------------------------------------------------

# ---------------------------  Main game engine  -----------------------------------------

while True:
    # ask the user for a letter
    asked_for_letter = input('Hello. Please choose a letter: ')
    # force the letter to lowercase
    asked_for_letter = asked_for_letter.lower()

    # if the inserted element is not a letter - ask again
    if not asked_for_letter.isalpha():
        print('Use just letters!')
        continue
    
    # if there are more than one element - ask again
    if len(asked_for_letter) > 1:
        print('Enter just one letter')
        continue

    # if the letter was already used - ask again
    if (asked_for_letter in wrong_letters) or (asked_for_letter in word_placeholder):
        print('You already use this letter!')
        continue

    
    # if the inserted letter is in the word check at which indices and place it in the word placeholder at those indices
    if asked_for_letter in selected_word:
        print('Good job. The letter is correct!')
        for i in range(length_selected_word):
            if selected_word[i] == asked_for_letter:
                word_placeholder[i] = asked_for_letter
        joined_strings = '  '.join(word_placeholder)
        joined_wrong_letters = ', '.join(wrong_letters)
        print(joined_strings + '     Wrong letters: ' + joined_wrong_letters)
    
    # else: if there are less mistakes then maximum allowed, then add the letter to the wrong list and print it, else end the game
    else: 
        if mistake < number_mistake_allowed:
            wrong_letters.append(asked_for_letter)
            mistake = mistake + 1
            joined_wrong_letters = ', '.join(wrong_letters)
            print(f'Try again! The letter is not correct! You have {mistake} mistakes from {number_mistake_allowed} possible')
            print(joined_strings + '     Wrong letters: ' + joined_wrong_letters)
        else:
            print('The letter is not correct. You reached maximum amount of mistakes. Game over!')
            print('The word was: ' + selected_word)
            break
        
    # if the word is completed - congratulate and end the game
    if '_' not in word_placeholder:
        print('Congratulation! You guessed the word!')
        break

# ---------------------------------------------------------------------------------------------------




                







