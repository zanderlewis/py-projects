# Difficulty: IV

import random

words = ['python', 'java', 'ruby', 'javascript']
chosen_word = random.choice(words)
guessed_letters = []
tries = 7

while tries > 0:
    print(f"Word: {''.join([letter if letter in guessed_letters else '_' for letter in chosen_word])}")
    print(f"Tries left: {tries}")
    guess = input("Guess a letter: ")
    guessed_letters.append(guess)
    if guess not in chosen_word:
        tries -= 1
    if all(letter in guessed_letters for letter in chosen_word):
        print(f"You win! The word was {chosen_word}")
        break
else:
    print(f"You lose! The word was {chosen_word}")