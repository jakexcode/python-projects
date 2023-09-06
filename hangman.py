import random
from words import words
import string


def get_valid_words(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_words(words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('you have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        # for letter in word:
        #     if letter in used_letters:
        #         word_list.append(letter)
        #     else:
        #         word_list.append('-')
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if lette is not in word
                print('The letter you guessed is not in the word. Please try again.')

        elif user_letter in used_letters:
            print('you have already guessed that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Sorry, you died. The word was', word, 'Better luck next time!')
    else:
        print('You guessed the word', word, '!!')


hangman()
