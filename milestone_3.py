import random

word_list = ['apple', 'orange', 'banana', 'grapes', 'melon']
word = random.choice(word_list)    

def check_guess(guess) :
    if guess in word:
        print (f"Good guess! {guess} is in the word.")
    else:
        print (f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input ('Guess letter: ')
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print ("Invalid letter. Please, enter a single alphabetical character.")
            

ask_for_input()