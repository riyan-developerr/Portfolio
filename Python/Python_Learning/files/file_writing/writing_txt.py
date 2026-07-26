""" 
Writing files in python (.txt , csv , pdf)

===============================
Explanation
===============================
with => opens and closes the file automatically
open => returns the object (the actual file) at the given path
"w"  => is the mode w for writing also have a (append) , x(create new file) , r(reading)
as   => assings the name to the file

now simple file.write(..) writes on the same line so to add new line
file.write(... + "\n")

to write from a list use loop to iterate over and then write
"""

# file_text = "I am learning to become financially free!"
employees = ["Doremon", "Nobita", "fishman","Naruto"]

# we can also use absolute file path 
file_path = "output.txt"

try:
    with open(file_path , "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print("file is created and data is written")
except FileExistsError:
    print("This file already exists")
except TypeError:
    print("Please check whether you are using string or list to write to file!")
    
finally:
    print("Cleaning up")
    