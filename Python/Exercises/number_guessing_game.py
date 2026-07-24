#number guessing game  (PYTHON MINI PROJECT)

# generate a random number
# ask user for entering the number 
# use while loop for keep on asking user
# define a counter to keep track of guesses
# if user enters wrong input handle that
# if user guesses correctly end the program and print number of guesses

import random
#defining variables for the game
lowest_num = 1
highest_num = 100
is_running = True
guesses = 0
#generating random number between our range
answer = random.randint(lowest_num , highest_num)

while is_running:
    guess = input(f"Enter a number between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        #this is correct input
        # first typecast
        guess = int(guess)
        guesses +=1
        
        if guess <= 0 or guess > 100:
            print("Out of range!")
            # print(f"Please Enter a number between {lowest_num} and {highest_num}: ")
        elif guess > answer:
            print("Too high! try again")
            # print(f"Please Enter a number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print("Too low! try again")
            # print(f"Please Enter a number between {lowest_num} and {highest_num}: ")
        else:
            print(f"Correct Guess\nAnswer was {answer}")
            print(f"your number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Input!")
        guess = int(input(f"Please Enter a number between {lowest_num} and {highest_num}: "))
