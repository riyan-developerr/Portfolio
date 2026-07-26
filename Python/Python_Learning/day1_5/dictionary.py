# dictionary = it is another type of collection which consist of key value pairs

capitals = {
    "USA":"Washington D.C",
    "Pakistan":"Islamabad",
    "China":"Beijing"
}

print(capitals.get("Australia"))
# print(help(capitals))

capitals.update({"Emperors Domain":"abc","domain":"hello"})
print(capitals)

capitals.pop("domain")
capitals.popitem() #returns the popped item as a tuple

print(capitals.keys())
print(capitals.values())

for key , value in capitals.items():
    print(f"{key}: {value}")
