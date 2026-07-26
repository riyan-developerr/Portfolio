# i know the basic arithematic operators and math functions but lets practice math

import math
x=3
y=-2
z=4

#important arithematic functions
print(abs(y))
print(round(3.14159,2))
print(pow(3,4))
print(min(x,y,z))
print(max(x,y,z))

pi = math.pi
print(pi)

e = math.e
print(e)

fac = math.pow(2,3)
print(fac)

# Exercise
#finding the circumference of a circle

import math

radius = float(input("Enter the radius of circle:"))
circumference = 2 * math.pi * radius
print(f"The circumference of circle is: {round(circumference,2)}cm")

#finding the area of a circle

area = math.pi * pow(radius,2)
print(f"The area of circle is: {round(area,2)}cm^2")

# finding the third side using pythagoras theoram
a = float(input("Enter first side:"))
b = float(input("Enter second side:"))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(f"The third side is: {round(c,2)}cm")
