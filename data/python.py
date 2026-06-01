import csv
import json
# # with open("name.txt","w") as file:
#     file.write("Riyan Ahmed")
# #so write method overrides the previos data
# lines=["Hi\n","My name is Riyan Ahmed\n","I am learning python programming\n"]
# with open("name.txt","w") as file:
#     file.write("Dragon Ahmed\n")
#     file.writelines(lines)
    
# with open("name.txt","r") as file:
#     data1=file.read()
#     data=file.readlines()
#     for items in data:
#         print(items,end="")
# normally writing data in json file
kb={
    "name":"riyan Ahmed",
    "goal":"REaching level one before the end of summer"
}
with open("data.json","w",encoding="utf-8") as f:
    json.dump(kb,f,indent=4)
    
#writing data in json file from list
large_data=[
    {"name":"Riyan","marks":100},
    {"name":"Huma","marks":100},
    {"name":"Aliyan","marks":97}
]
# jsonl writes one json object per line and json.dumps give string output so we use f.write
with open("data.jsonl","w") as f:
    for lines in large_data:
        f.write(json.dumps(lines) + "\n")
        
with open("data.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerow(["dragon",100])
    writer.writerow(["human",10])
