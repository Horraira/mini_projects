import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    # print(word)
    hint = [letter for letter in word[:1]] + ['-' for letter in word[2:]] + [letter for letter in word[-1:]]
    print('Hint: ', ''.join(hint))
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)      # get all letters in uppercase
    used_letters = set()    # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ''.join(['a', 'b', 'cd']) --> 'a b c cd'
        print('\nYou have', lives, 'lives left and You have used these letters: ', ''.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  # one letter cen be used only onced
            used_letters.add(user_letter)   # add a letter in used_letter list
            if user_letter in word_letters: # check if the user_letter match with any word_letter
                word_letters.remove(user_letter)    # remove the matching letter from word_letter
            else:
                lives = lives - 1   # takes away a life if the user letter doesn't match
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 or when live == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


flag = 'Y'
while flag == 'Y':
    hangman()
    flag = input('Wanna Play again Y/N: ').upper()


#hangman()