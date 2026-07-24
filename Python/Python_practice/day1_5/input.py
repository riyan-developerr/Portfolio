# input() = this functions helps us to get input from user
# note: it returns a string data type

# name = input("What is your name? ")
# age = input("What is your age? ")
# age = int(age) + 1

# print(f"hello {name}!")
# print("HAVE A HAPPY BIRTHDAY")
# print(f"You are {age} years old")

#Exercises 

#Exercise 1
# len = float(input("Enter length of Rectangle: "))
# wid = float(input("Enter width of Rectangle: "))

# print(f"The area of Reactangle is: {len * wid}")

#Exercise 2
# Shopping cart game

item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many items you want? "))

total = price * quantity

print(f"You have bought {quantity}x {item}/s ")
print(f"Your total amount is: ${total}")