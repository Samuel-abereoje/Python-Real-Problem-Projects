balance = 50000        # starting account balance
transactions = []          # stores all deposits/withdrawal

def check_balance():        # A function to shows current balance
    print(f"Your Balance is: #{balance}") 
transactions = [] 

def withdraw():           # A function that subtracts money if enough balance exists
    global balance
    try:
        amount = int(input("Enter amount: "))  
        if amount <= 0:
            print("Invalid amount")
        elif balance < amount:
            print("Insufficient funds")
        else:
            balance -= amount
            transactions.append(f"Withdrew #{amount}")
            print(f"Withdrawn #{amount}")
            
    except ValueError:
        print("Enter a valid number")

def deposit():             # A fuction that adds money to balance
    global balance
    try:
        amount = int(input("Enter amount: "))
        
        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            transactions.append(f"Deposited #{amount}")
            print(f"You Deposited #{amount}")
            
    except ValueError:
        print("Enter a valid number")

def show_transactions():       # A function that displays history of actions
    if not transactions:
        print("No transactions yet")
    else:
        print("\nTransaction History:")
        for t in transactions:
            print("-", t)

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Select option: ")
    
    if choice == "1":
        check_balance()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        deposit()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid option")