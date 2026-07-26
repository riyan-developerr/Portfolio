# decorators = These are functions that extend the functionality of a base function 
#  without modifying the original function
# we can add more than one decorators 
# and can also add parameters

"""
This is the basic syntax of a decorator 
Note: we use wrapper because if we don't use it when we write
@decorator before base function it will automatically call the decorator 
so to prevent that we use wrapper function

def add_sprinkles(func):
    def wrapper():
        func()
    return wrapper()

Another point when we use decorator essentially this is happening
get_icecream() = add_sprinkles(get_icecream())
so if i write return wrapper() with '()' it is gonna call the wrapper and return none so 

get_icecream() = None 
which is not callable so thats why i got that error

"""
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print(f"you have added sprinkles 🧁")
        func(*args,**kwargs)
    return wrapper

# Creating another decorator
def add_fundge(func):
    def wrapper(*args,**kwargs):
        print(f"Added fudge to the ice-cream 🍫")
        func(*args,**kwargs)
    return wrapper

# this is base function
@add_sprinkles
@add_fundge
def get_icecream(flavour):
    print(f"you have ordered {flavour} ice-cream 🍨")
  
# suppose i want to add functionality to it without changing it what to do?
# one way is to use decorators  
get_icecream("Mango")