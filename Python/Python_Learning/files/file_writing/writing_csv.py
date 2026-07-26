import csv
""" 
Writing in csv files

=============================
Explanation
=============================

import csv module 
to write to a csv first create a writer object 
then iterate over the 2d list and enter rows in csv file

when creating writer object only pass the file name
writer = csv.writer(file)

to write from 2d dataset without using loop use writerows(2d dataset)
writer.writerows(file , row)

"""
data = [["name","age","job","salary"],
        ["doremon",100,'caretaker',0],
        ["nobita",20,'accountant',100],
        ["Gian",21,'singer',100000]]

#  we can also use absolute file path 
file_path = "file_writing/output_js.csv"

try:
    with open(file_path , "w" , newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"{file_path} file is created")
except FileExistsError:
    print("This file already exists")
except TypeError:
    print("Please check whether you are using string or list to write to file!")
    
finally:
    print("Cleaning up")