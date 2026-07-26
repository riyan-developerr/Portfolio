# @property = they define methods of class as property(still accessed as attribute)
# they help to organize things internally so if i want to modify my code in the future the users do not have to change their interaction 

class Student:
    def __init__(self, age=20):
        self._age = 20
        
    @property
    def age(self):
        return f"Your age: {self._age}"
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Invalid age")
            return
        else:
            self._age = value
            return f"Your age: {self._age}"
        
    @age.deleter
    def age(self):
        print("Age has been deleted")
        del self._age
    
    
std = Student()
print(std.age)

del std.age
# print(std.age)



