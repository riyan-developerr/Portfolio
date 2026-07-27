""" 
Datetime module to access date and time
"""

import datetime

# date1 = datetime.date(2029,4,21)
# print(date1)

today = datetime.datetime.now()
# print(today)

current_date = datetime.datetime.now()
target_date = datetime.datetime(2029 , 4,1 ,6,0,0)

if current_date == target_date:
    print(f"Congratulations! You have reached Financial freedom")
else:
    print("""
          Keep on striving.
          You are getting closer to your target.
          Inshallah you will get there soon✌️""")

print(today.second)