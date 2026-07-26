# match-case (switch) = they are alternative to if else elif statement
# they make the code clean and much easier to read

def is_weekend(day):
    day = day.lower()
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case "saturday" | "sunday":
            return True
        
print(is_weekend("saturday"))
            