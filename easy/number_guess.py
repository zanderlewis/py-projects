# Difficulty: II

import random

n = random.randint(1, 100)
tries = 1

while True:
    print('Guess a number between 1 and 100: ')
    guess = int(input())
    i = int(guess)
    if i == n:
        print(f'Congratulations! You guessed the number {n} in {tries} tries!')
        break
    elif i < n:
        print('Try higher')
        tries += 1
    elif i > n:
        print('Try lower')
        tries += 1
