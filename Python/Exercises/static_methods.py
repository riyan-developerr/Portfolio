# static methods = they belong to class and exist when no object is created
# they can be accessed by both instance and class names
# they are used as utility functions and do not access the data of objects

class Employee:
    alive = True
    def __init__(self, name , position):
        self.name = name
        self.position = position
        # Employee.alive = False
        
    @staticmethod
    def is_valid_position(position):
        positions = ["manager","cook","janitor","ceo","accountant"]
        return position in positions
    
# print(Employee.is_valid_position("manager"))
employee1 = Employee("doremon","manager")
print(employee1.name)
print(employee1.is_valid_position(employee1.position))
# print(employee1.alive)
# print(Employee.alive)