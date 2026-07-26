""" 
File reading is similar to writing so i will keep it short

=====================================
Explanation
=====================================

Text:
we will open the file and then 
content = file.read (simple)

Json
open the file and then 
content = json.load(file)

Csv
content = csv.reader(file)
remember this is a 2d object just like spreadsheet like in excel

lets practice text (it's easy 😁)

"""

file_path = "file_writing/output.txt"

with open(file_path , "r") as file:
    content = file.read()
    print(content)