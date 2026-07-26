# python Calculator
# we will perform following operations ( + , - , * , / , % )


#calulator program starts
#taking numbers from user to perform opweration on
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
#asking for which operation to perform
operator = input("Enter the operator ( + , - , * , / , % ): ")

# conditional if logic to caluculate the result based on operation chosen by user
if operator == "+":
    total = num1 + num2
    print(f"Your total is : {total}")
elif operator == "-":
    total = num1 - num2
    print(f"Your total is : {round(total,2)}") # so answer is always postive
elif operator == "*":
    total = num1 * num2
    print(f"Your total is : {round(total,2)}")   
elif operator == "/":
    if num2 == 0:
        print("invalid cannot divide by zero")
    else:
        total = num1 / num2
        print(f"Your total is : {round(total,2)}")
elif operator == "%":
    total = num1 % num2
    print(f"Your total is : {total}")
#final condition to handle any wrong selection of operator
else:
    print("your operator is NOT valid")