# Inheritance = Child class can use the methods and attributes of parent class
#               aka a class can use attributes and methods of other classes by inheriting them
# It helps in code reuseability and easy modification
# class child(parent)

class Animal:
    def __init__(self , name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Wafadar")
print(dog.name)
dog.eat()
dog.sleep()
dog.speak()