"""
file detection Python

===================
Explanation
===================

os is the module used for the interaction of python code with operation system
os.path.exists(file_path) is used to detect a path it returns boolean

we can use two types of paths 

relative path e.g("test.txt")
Absolute path e.g("C:/Users/Riyan Ahmed/Desktop/test.txt")

we can also check whether the thing is a file or directory(folder)
    """
    
import os

file_path = "C:/Users/Riyan Ahmed/Desktop/test"

if os.path.exists(file_path):
    print(f"this path '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print(f"This is a file")
    elif os.path.isdir(file_path):
        print(f"This is a directory")
    else:
        print(f"this is neither a file nor a directory")
else:
    print(f"this path '{file_path}' does not exist")
    
