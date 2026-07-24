# nested loops = A loop inside another loop

#for  example i want to print numbers from 1 to 10

# for x in range(1,10):
#     print(x,end = "")

#but if i want to repeat this looping structure three times then i will use nested looop

for x in range(3):
    for num in range(1,10):
        print(num,end = "")
    print()
    
# now ask for user input and print a rectangle

rows = int(input("Enter the # of rows: "))
col = int(input("Enter the # of col: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(col):
        print(symbol,end = "")
    print("")
