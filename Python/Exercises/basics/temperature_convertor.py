# Python program to convert temperature

value = float(input("Enter the value of temperature:"))
unit = input("Enter the unit of temperature:(F or C):")

if unit == "C":
    temp = (value * 9)/5 + 32
    print(f"The temperatur in Fahrenheit is {round(temp,2)}")
elif unit == "F":
    temp = ((value - 32) * 5)/9
    print(f"The temperatur in Celsius is {round(temp,2)}")
else:
    print(f"Invalid {unit} cannot be a unit")