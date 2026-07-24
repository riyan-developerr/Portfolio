# collections = These are "variables" that store other values
# there are 4 basic types of collections

# list [] = ordered and mutable.duplicates are ok
# sets {} = unordered and immutable.add/remove ok.No duplicates allowed
# tuple ()= ordered and unchangeable.duplicates ok.

fruits = {"apple","banana"}

# print(fruits)
# print(fruits[0])
# print(dir(fruits))
# print(help(fruits))

# print(fruits.count("mango"))

# required_fruit = input("Enter the fruit you want:")

# if fruits.count(required_fruit) == 0:
#     print("This fruit is not available")
# else:
#     print("This fruit is available")

fruits = {"mango"}
sports = {"haki"}
fruits.update(sports)
print(fruits)