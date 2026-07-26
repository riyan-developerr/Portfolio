import json
""" 
Writing in json files

=============================
Explanation
=============================

import json module 
to write to a json first write correct extension in file path (ends .json)

json.dump("data to enter" , "file name" , indent, etc )

"""
dic = {
    "name": "Riyan",
    "title": "searching Allah's forgiveness and success in both worlds",
    "age" : 18,
    "is_student": True
}

#  we can also use absolute file path 
file_path = "file_writing/output_js.json"

try:
    with open(file_path , "w") as file:
        json.dump(dic , file , indent = 4)
        print("json file is created and data is written")
except FileExistsError:
    print("This file already exists")
except TypeError:
    print("Please check whether you are using string or list to write to file!")
    
finally:
    print("Cleaning up")