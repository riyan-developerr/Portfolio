#conditional expression = it is a shortcut for if else statements
# it is called ternary operator in other programming languages
#it returns one of two results based on condition
# Formula = X if condition else Y

age = 18 
role = "admin"
appearance = "ugly"

status = "adult" if age >= 18 else "child"
print(status)

access_level = "full access" if status == "admin" else "limited access"
print(access_level)

acceptance = "you are accepted" if appearance == "beautiful" else "you are rejected"
print(acceptance)