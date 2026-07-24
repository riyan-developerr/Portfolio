import random
from wordslibrary import words

hangman_art = {
    0 : ("   ",
         "   ",
         "   "),
    1 : (" o ",
         "   ",
         "   "),
    2 : (" o ",
         " | ",
         "   "),
    3 : (" o ",
         "/| ",
         "   "),
    4 : (" o ",
         "/|\\",
         "   "),
    5 : (" o ",
         "/|\\",
         "/  "),
    6 : (" o ",
         "/|\\",
         "/ \\"),

}

def display_hangman(wrong_guesses):
    print("****************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    
def main():
    answer = random.choice(words)
    wrong_guesses = 0
    hint = ["_"] * len(answer)
    guessed_answer = set()
    is_running = True
    
    while is_running:   
        display_hangman(wrong_guesses)
        
        display_hint(hint)
        guess = input("Enter a letter: ")
        
        # handling user input
        if len(guess) > 1:
            print("Invalid input")
            continue
        
        if not guess.isalpha():
            print("You entered a number")
            continue
        
        #updating the hint
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    
        if guess in guessed_answer:
            print(f"{guess} is already guessed")
            continue
        guessed_answer.add(guess)
        
        if guess not in answer:
            wrong_guesses += 1
            
           
        print(wrong_guesses) 
        if "_" not in hint:
            display_hangman(wrong_guesses)
            print("YOU WIN")
            display_answer(answer)   
            is_running = False
            
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running = False
            
    print("Thankyou for Playing")
            
if __name__ == "__main__":
    main()