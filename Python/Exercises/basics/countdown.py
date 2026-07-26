#Coutdown timer program
# 1 Ask user how much time to countdown
# 2 convert that time into hour min and sec
# 3 show them in proper format 
# 4 once time is finished show time's up

import time

user_time = int(input("Enter time in seconds:"))

while user_time <= 0:
    print("Time cannot be 0 or negative")
    user_time = int(input("Enter time in seconds:"))
    
#using for loop because we know how many times to run loop
if user_time >86400:
    print("beyound the limit of this timer!")
else:
    for x in range(user_time,0,-1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME'S UP")

