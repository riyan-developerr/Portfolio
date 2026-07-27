""" 
Multi-threading = it is used to perform multiple tasks simultaneously (multi-tasking)
why it is useful? => Good for I/O tasks e.g: reading files or fetching data from api

syntax: threading.Thread(target = function , arg = (tuple))

lesson: Do not write () after the functions in target 
""" 

import threading
import time

def reading(book):
    time.sleep(8)
    print(f"You have read the {book} book")
    
def eating():
    time.sleep(4)
    print("you have eaten a pizza")
    
def watching():
    time.sleep(2)
    print("you have watched dragon ball z movie")
    
    
# reading()
# eating()
# watching()

# if i want to perform these tasks simultaneously i will use multi threading

thread1 = threading.Thread(target = reading, args=("The 7 habits of highly effective people",))
thread1.start()

thread2 = threading.Thread(target = eating)
thread2.start()

thread3 = threading.Thread(target = watching)
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f"Well done you have completed your tasks!")
    