# name = input("Enter your name:")

# result = len(name)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.find("y")
# result = name.rfind("y")
# result = name.replace("y","brave")
# result = name.count("r")
# result = name.casefold()
# result = name.center(" ")
# result = help(str)
# result = name.__add__(" hardworking")
# print(result)

# combined = "Riyan" + "Ahmad"
# print(combined)

#exercise

#asking for user to enter their name
user_name = input("please enter your name: ")

if len(user_name)<= 12:
    if user_name.find(" ") < 0:
        if user_name.isalpha():
            print("you are valid user")
        else:
            print("your name contain digits")
    else:
        print("it contains spaces")
else:
    print("length is greater than 12")
    
#another way could be as follows
if len(user_name) > 12:
    print("invalid: your name exceeds the limit")
elif not user_name.find(" ") == -1:
    print("Invalid: your name contain spaces")
elif not user_name.isalpha():
    print("Invalid: your name contain numbers")
else:
    print(f"your are a valid user\nWelcome {user_name}")