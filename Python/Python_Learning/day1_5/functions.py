# function = Block of code used again and again
# it is defined as 
# def fun_name(parameters):

# return = word used to end function and return some value

# default arguments
def greet(name="ahmed"):
    print(f"hello {name}")

greet("riyan")

# positional arguments
def full_name(title,first_name,last_name):
    print(f"{title} {first_name} {last_name}")
    
full_name(title="kakkar",last_name="shami",first_name="fahad")

# keyword arguments
# * unpacking operator(packs as tuple)
def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
add(1,2,3,12)

# ** takes arguments as dictionary key-value pairs
def address(**kwargs):
    for value in kwargs.values():
        print(value , end = " ")

address(house_no=123,
        street=23,
        city="Lahore",
        country="Pakistan",
        contenent="Asia")

# return is very important part of a function
print()
def full_name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full = full_name("Riyan","Ahmed")
print(full)