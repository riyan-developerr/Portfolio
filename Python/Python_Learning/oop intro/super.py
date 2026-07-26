# super() = it is used to access the methods of parent class inside child class (constructor etc.)
# it is used to extend the functionality of methods in child class

class Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def Describe(self):
        print(f"this shape has a {self.color} color and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self , color , is_filled , radius):
        super().__init__(color , is_filled)
        self.radius = radius   
        
    def Describe(self):
        super().Describe()
        print(f"The area of circle is : {3.14 * pow(self.radius,2):.0f}")   

class Square(Shape):
    def __init__(self , color , is_filled , lenght):
        super().__init__(color , is_filled)
        self.lenght = lenght      

    
class Triangle(Shape):
    def __init__(self, color , is_filled , base , height):
        super().__init__(color , is_filled)
        self.base = base
        self.height = height
        
        
circle = Circle(color="blue",is_filled=True ,radius = 4)

print(circle.color)   
circle.Describe()