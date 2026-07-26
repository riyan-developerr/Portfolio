class Car:
    # it is a constructor(A constructor creates the object)
    # self keyword refers to the (calling) object
    def __init__(self, model , color , year):
        self.model = model
        self.color = color
        self.year = year
        
    # we can also have methods in an object
    
    def drive(self):
        print(f"You are driving {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")