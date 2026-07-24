# class variables = these are variables shared by all instances of a class
# these are used to share data between all the objects of a class

# Note : We can access class variables with class name as well instance 

class Student:
    num_students = 0
    grad_year = 2029
    
    def __init__(self, name , age):
        self.name = name
        self.age = age
        Student.num_students += 1

std1 = Student("Riyan",18)
std2 = Student("Huma",19)

print(f"My class of {Student.grad_year} has {Student.num_students} students")
print(std1.name )
print(std2.name )
        
    