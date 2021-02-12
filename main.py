import random
from WordList import words
import string
import time

def start_msg():
    name = input('Enter your name: ')

    print(f'Welcome to Hangman {name}! I hope you enjoy the game! Goodluck!')

def get_word(words):
    guess_word = random.choice(words)
    while '-' in guess_word or ' ' in guess_word:
        guess_word = random.choice(words)

    return guess_word.upper()

def number_lives(len_word):
    if len_word <= 5:
        lives = 5
    elif len_word >= 6 and len_word <= 10:
        lives = 8
    else:
        lives = 12
    return lives

def game(words):
    guess_word = get_word(words)
    letters_in_word = set(guess_word)
    lives = number_lives(len(guess_word))
    letters_guessed = set()
    alphabet = set(string.ascii_uppercase)
    word_list = ''
    while lives > 0 and guess_word != word_list:
        count = 0
        word_list = ''
        if lives > 1:
            print('You have ', lives, 'lives remaining.')
        else:
            print('You have ', lives, 'life remaining.')
        print('You have used: ', ' '.join(letters_guessed))
        for letters in guess_word:
            if letters in letters_guessed:
                word_list = word_list + letters
                count +=1
            else:
                if count < len(guess_word)-1:
                    word_list = word_list + '-'
                    count +=1
        print(word_list)
        user_guess = input('Guess a letter: ').upper()
        print()
        if user_guess in alphabet - letters_guessed:
            letters_guessed.add(user_guess)
            if user_guess in letters_in_word:
                letters_in_word.remove(user_guess)
            else:
                lives -=1
        elif user_guess in letters_guessed:
            print('You have tried this character already!')
        else:
            print("Invalid character.Please try again.")
    if len(letters_in_word) == 0:
        print("Congrats! You have guessed the correct word: ", guess_word)
    elif lives == 0:
        print('You have no lives left. You lost')
        print('The correct word is: ', guess_word)

start_msg()
time.sleep(5)
print()
game(words)