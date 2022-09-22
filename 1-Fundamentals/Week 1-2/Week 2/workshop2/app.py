from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Register
while True:
    print("          === Automated Teller Machine ===          ")
    name =  input("Enter name to register (at most 10 char): ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    else:
        break

while True:
    pin = input("Enter PIN (exactly 4 char): ")
    if len(pin) != 4:
        print("PIN must contain exactly 4 characters.")
    else:
        break

balance = 0


# Registration statement
print(name, "has registerd with a starting balance of $", str(balance))

# Login 
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    u_val = input("Enter name:")
    p_val = input("Enter PIN:")
    if u_val == name and p_val == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(u_val)
    option = input("Choose and option:")
    if option not in ['1','2','3','4']:
        print("Please enter a number from 1-4.")
        continue
    if int(option) == 1:
        account.show_balance(balance)
    elif int(option) ==2:
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif int(option) == 3:
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif int(option) == 4:
        account.logout(u_val)
        break



