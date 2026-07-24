# logical operators: There are three main operators 
                     #AND (True when both conditions are true)
                     #OR (True when Either of the conditions are true)
                     #NOT (Inverts the condition , False if True vice versa)
                     
temp = 27
is_sunny = False

if temp < 25 and is_sunny:
    print("We will go outside")
elif temp < 25 and not is_sunny:
    print("It is cloudy we will not go outside")
elif temp > 25 and is_sunny:
    print("we will think about it")
else:
    print("it is warm outside will not go")
    
healty = True
valid_age = True
degree = "AI"

if healty and valid_age and degree=="AI":
    print("YOu are selected for the contest")
else:
    print("You are not qualified for the contest")