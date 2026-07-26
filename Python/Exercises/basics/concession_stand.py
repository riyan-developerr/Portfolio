# concession stand program
menu = {
    "popcorn":6.12,
    "soda":2.3,
    "pretzel":3.12,
    "lemonade":4
}

cart = []
total = 0

#display the menu
print("----------Menu----------")
for key , value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Enter food you want to buy(q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)

    
print("-----Your Cart-----")
for food in cart:
    print(food , end = " ")
    
print()
print(f"Total Amount: ${total:.2f}")
