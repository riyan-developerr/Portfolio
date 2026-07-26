# OOP (object oriented programming) 

# object = it is a bundle of attributes(variables) and methods(functions)
# attributes -> they describe the object(the things object has)
# methods    -> these are the functions inside object(what object can do or perform?)

# class = The blueprint to design the structure of our objects

from car import Car
        

Car1 = Car("Lamborghni", "Cyan" , "2029")
Car2 = Car("Mercedes", "black" , "2029")

print(Car2.model)
Car2.drive()
Car2.describe()



