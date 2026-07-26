#Compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the value of principle:"))
    #in order to notify the customer we will use if condition
    if principle <= 0:
        print("principle cannot be less than or equal to zero")
        
while rate <= 0:
    rate = float(input("Enter the value of interest rate:"))
    #in order to notify the customer we will use if condition
    if rate <= 0:
        print("interest rate cannot be less than or equal to zero")
        
while time <= 0:
    time = int(input("Enter the value of time in years:"))
    #in order to notify the customer we will use if condition
    if time <= 0:
        print("time cannot be less than or equal to zero")
    
#now calculating total compunded amount using formula

total = principle * pow((1 + rate / 100),time)

print(f"Your total amout is: ${total:,.2f}")