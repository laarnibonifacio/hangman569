import random
from typing import Self

from hangman.hangman_Template import play_game
from milestone_3 import ask_for_input

word_list = ['apple', 'orange', 'banana', 'grapes', 'melon']


class Hangman:
    def __init__ (self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed =  ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
            guess = input('Guess a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 1 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

game = Hangman(word_list)
play_game(word_list)
