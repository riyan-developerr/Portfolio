# making a weight convertor program to master conditional statements

#aksing for weight from user
weight = float(input("Enter your weight: "))
#we need only string
unit = input("Enter the unit (K or L): ")

if unit == "K":
    weight = weight * 2.210
    print(f"Your weight is: {round(weight,2)} Lbs.")
elif unit == "L":
    weight = weight / 2.210
    print(f"Your weight is: {round(weight,2)} Kgs.")
else:
    print("Invalid input")