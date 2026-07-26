"""
   Exception = Anything that interrupts the normal flow of program
   exception handling ( try , except , finally)
   some exceptions (ZeroDivisionError , ValueError ,TypeError etc)
   they are used to gracefully handle the exceptions and prevent program from crashing 
    
    Working:
    
    first try block executes
    if something went wrong (exception) it will leave try block and attempt to match the exception
    once exception is identified it will run that code and leave the entire block
    if first exception doesn't work it will keep on going until it matches
    if nothing matches it will execute the final exception block(given it is decleared)
    Finally block always executes whether exception occurs or not
    """
try:
    num = int(input("Enter a number for division: "))
    print(1 / num)
except ZeroDivisionError:
    print(f"Friend you cannot divide by zero!")
except TypeError:
    print("You cannot add with words/letters (string)!")
except Exception:
    print("Something went wrong!")
finally:
    print("Cleaning up!")
