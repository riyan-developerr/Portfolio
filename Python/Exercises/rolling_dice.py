# rolling dice program

# print("\u25CF , \u250C , \u2500 , \u2510 , \u2502 , \u2514, \u2518")
# ● , ┌ , ─ , ┐ , │ , └, ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

import random

dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),

    4 : ("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘"),   
}

dice = []
total = 0
number_of_dice = int(input("Enter number of dice: "))

for die in range(number_of_dice):
    dice.append(random.randint(1,6))
    
# printing our dice art
for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)
    
for die in dice:
    total += die   
print(total)

#waaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh i have only revised yesterday's work till now
#cryiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaiiinnnnnnnnnnnnnnnnnn