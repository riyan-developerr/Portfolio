# membership operator = used to check whether a value\variable is in a sequence 
                        # sequence ( set,list,tuple,dictionary , string)
                        # in and not in
                        
grade = {
    "spongebob": "A",
    "patrick": "B",
    "diamond": "C",
    "adler" : "D"
}

# name = input("Enter the name of student: ")

# if name in grade:
#     print(f"{name} is a student")
# else:
#     print(f"{name} is not a student")
    
    
email = "riyan@gmail.com"

if "@" in email and "." in email:
    if not email.count(" ") == 0:
        print("invalid email")
    else:
        print("Valid email")
else : 
    print("InValid email")
    