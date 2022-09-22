def show_balance(balance):
    print("Current balance: $ ", round(float(balance), 2)) 
    pass

def deposit(balance):
    amount = input("Enter amount to deposit: $ ")
    return round(balance + float(amount), 2)

def withdraw(balance):
    withdraw = input("Enter amount to withdraw: $ ")
    while float(withdraw) > balance:
        print("Where are you going to get that kind of money?")
        print("Please request an amount less than $", str(balance), ".")
        withdraw = input("Enter amount to withdraw: $ ")
    return round(balance - float(withdraw),2)
    
def logout(name):
    print("Goodbye", name + "!")
