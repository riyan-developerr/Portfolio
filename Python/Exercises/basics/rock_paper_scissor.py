# rock papar and scissors game

import random

options = ("rock","paper", "scissors")
is_running = True
print("----------------------------------")
print("-----Oldest Game in The World-----")
print("----------------------------------")
while is_running:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter your choice (rock,paper,scissors): ")

    print(f"Your choice: {player:>10}")
    print(f"computer's choice: {computer}")

    if player == computer:
        print("----------------------------------")
        print("it's a draw")
        print("----------------------------------")
    elif player == "rock" and computer == "scissors":
        print("----------------------------------")
        print("You win!")
        print("----------------------------------")
    elif player == "paper" and computer == "rock":
        print("----------------------------------")
        print("You win!")
        print("----------------------------------")
    elif player == "scissors" and computer == "paper":
        print("----------------------------------")
        print("You win!")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("You lose!")
        print("----------------------------------")
        
    if not input("Play again? (y/n): ").lower() == "y":
        is_running = False
        
print("Thanks for playing")
