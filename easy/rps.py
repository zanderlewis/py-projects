# Difficulty: II

import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Do you choose rock, paper or scissors? ")
print(f"Computer chose {computer_choice}")
print(f"You chose {user_choice}")

if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")