# Quiz game in Python

# tuples because we do not need to change them and tuples are faster
questions = (("Which animal lays the largest egg?")
             ,("how many bones does human body has?")
             ,("Which planet is the hottest in the solar system")
             ,("Answer this calculation\n'7 * 8 = ?'")
             ,("How many Surah are in Quran?"))

options = (("A. Elephant\nB. Whale\nC. Ostrich\nD. Flamingo")
           ,("A. 204\nB. 206\nC. 208\nD. 210")
           ,("A. mercury\nB. venus\nC. earth\nD. mars")
           ,("A. 45\nB. 52\nC. 56\nD. 54")
           ,("A. 110\nB. 112\nC. 114\nD. 116"))

answers = (("C"),("B"),("B"),("C"),("C"))
# because we need to append the guesses
guesses = []

score = 0
# counter to alterate over the questions
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option,end = "")
        
    guess = input("\nEnter your answer(a ,b ,c ,d):").upper()
    if guess == answers[question_num]:
        score += 1
        print("CORRECT ANSWER")
    else:
        print(f"INCORRECT ANSWER {answers[question_num]} is the correct option")
        
    guesses.append(guess)   
    question_num += 1
    print("----------------")
   
print("----------") 
print("  result  ") 
print("----------") 

for answer in answers:
    print(answer, end = " ")
    
print()
for guess in guesses:
    print(guess, end = " ")
   
result = int(score /len(questions) * 100)
print()

print(f"your performance: {result}%")