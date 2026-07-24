# polymorphism = come from greek work 
#                   Poly = Many
#                   morph = shapes
# we can acheive polymorphism with 2 techniques
# inheritance = where the child is also considered as parent
# Duck Typing = ...

from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        

class Square(Shape):
    def __init__(self , length):
        self.lenght = length
        
    def area(self):
        return self.lenght ** 2

class Triangle(Shape):
    def __init__(self , length , height):
        self.lenght = length
        self.height = height  
    def area(self):
        return (self.lenght * self.height) * (1/2)
    
class Pizza(Circle):
    def __init__(self , toppings , radius):
        super().__init__(radius)
        self.toppings = toppings
        
    
shapes = [Circle(3), Square(3) , Triangle(3,4), Pizza("cheese",4)]

for shape in shapes:
    print(f"{shape.area()} cm^2")