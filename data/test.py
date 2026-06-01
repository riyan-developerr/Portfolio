
pdf=[]
docs=[]
images=[]
data=[]
code=[]
others=[]

files = [
    "notes.txt", "photo.jpg", "assignment.pdf", "data.csv",
    "script.py", "image.png", "report.pdf", "main.cpp",
    "readme.txt", "table.xlsx", "index.html", "logo.jpg",
    "unknownfile", "archive.zip"
]

for items in files:
    if items[-3:]=="pdf":
        pdf.append(items)
        
    elif items[-3:]=="docx" or items[-3:]=="txt" or items[-3:]=="ppt" or items[-3:]=="pptx":
        docs.append(items)
    elif items[-3:]=="jpg" or items[-3:]=="png":
        images.append(items)
        
    elif items[-3:]=="xls" or items[-3:]=="xlsx" or items[-3:]=="csv":
        data.append(items)
        
    elif items[-3:]=="cpp" or items[-3:]=="py" or items[-3:]=="html":
        code.append(items)
        
    else:
        others.append(items)
        
total=0
lis=[pdf,docs,images,data,code,others]
for items in lis:
    count=0
    for files in items:
        total+=1
        count+=1
    print(f"{items} count:{count}")
print(f"total count:{total}")