#Format specifiers are new to me i did not learn them before

# format specifiers = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

#lets practice Riyan Ahmed khan the best data analyst in the world

price1 = 1234.352
price2 = 435.234
price3 = -246.2

print(f"The value of price 1 is: ${price1:+,.2f}")
print(f"The value of price 2 is: ${price2:+,.2f}")
print(f"The value of price 3 is: ${price3:+,.2f}")