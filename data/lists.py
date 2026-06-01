names=["riyan","huma","riyan"]
names.append("hamza")
names.extend(["doremon","nobita"])
print(names.count("riyan"))
names.pop(1)
print(names)
names.remove("nobita")
print(names)
names.insert(2,"dragon")

print(names[0])
print(names[0:4])
print(names[::-1])
print(names.sort())