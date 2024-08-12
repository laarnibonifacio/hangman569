import random

word_list = ['apple', 'orange', 'banana', 'grapes', 'melon']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Enter a single letter: ')

#Check if the input is valid
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
