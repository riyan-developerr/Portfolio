# Python Banking Program

def Show(balance):
    print("===========~============")
    print(f"Your Balance is: ${balance:.2f}")
    print("===========~============")

def Deposit():
    amount = float(input("Enter the deposit Amount: "))
    
    if amount < 0:
        print("===========~============")
        print("Amount cannot be less than zero")
        print("===========~============")
        # if i do empty return it will give error
        return 0
    else:
        return amount

def Withdraw(balance):
    amount = float(input("Enter the deposit Amount: "))
    
    if amount < 0:
        print("===========~============")
        print("Amount cannot be less than zero")
        print("===========~============")
        return 0
    elif amount > balance:
        print("===========~============")
        print("Insufficient Balance")
        print("===========~============")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    print("=======================")
    print("Banking Program")
    print("=======================")
    while is_running: 
        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit program")
        print("=======================")
        choice = input("Enter your choice: ")
        print("=======================")
        
        if choice == "1":
            Show(balance)
        elif choice == "2":
            balance += Deposit()
        elif choice == "3":
            balance -= Withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("=======================")
            print("Your choice is not valid")
            print("=======================")
            
    print("===========~============")
    print("Thank you for Working with us.Have a nice day")
    print("===========~============")
    
if __name__ == '__main__':
    main()