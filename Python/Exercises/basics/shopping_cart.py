#shopping cart program 

#first we will create collective variables 
# then we will use loop to run the program 
# then conditions for user to enter or quit the program
# finally display the items and the total amount

foods = []
prices = []
total = 0

# we do not know how many things user will buy so use while
while True:
    #asking for user input
    food = input("Enter the food you want to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of food: $"))
        foods.append(food)
        prices.append(price)
    
# decorative text    
print("-----Cart Final-----")
for food in foods:
    print(food,end = " ")
  
# calculating total price  
for price in prices:
    total += price

# printing the total amuont
print()
print(f"Your total price is: ${total}")