class User:

    def __init__(self, name, pin, password) -> None:
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        while len(new_name) < 2 or len(new_name) > 10 or (' ' in new_name):
            new_name = input("New name must be at least 2 up to 10 characters without space.")

        while len(self.name) == len(new_name):
            new_name = input("New name cannot be the same as your current name.")
        self.name = new_name

    def change_pin(self, old_pin, new_pin):
        while len(new_pin) == 4:
            new_pin = input("New PIN must be exactly 4 digits.")

        self.pin = new_pin

    def change_password(self, old_password, new_password):
        while len(new_password) < 5 or ' ' in new_password:
            new_pin = input("New password must be 5 or more characters without space.")

        self.password = new_password 

class BankUser(User):

    def __init__(self, name, pin, password, balance=0, hold=False) -> None:
        super().__init__(name, pin, password)
        self.balance = balance
        self.hold = hold

    def on_hold(self):
        self.hold = not(self.hold)

    def show_balance(self):
        print(self.name, "has an account balance of: $" + "{:.2f}".format(self.balance))

    def withdraw(self, wd):
        if self.hold is True:
            return print("Account is on hold.  Transaction rejected.\n")

        if wd < 0:
            print("You must enter a positive amount.  Transaction canceled.\n")
            return False
        self.balance -= wd

    def deposit(self, dep):
        if self.hold is True:
            return print("Account is on hold.  Transaction rejected.\n")

        if dep < 0:
            print("You must enter a positive amount.  Transaction canceled.\n")
            return False
        self.balance += dep

    def transfer_money(self, reciever, trans):
        if self.hold is True:
            return print(self.name + "'s account is on hold.  Transaction rejected.\n")
        if reciever.hold is True:
            return print(reciever.name + "'s account is on hold.  Transaction rejected.\n")

        if trans > reciever.balance:
            print("You must enter a lesser amount.  Transaction canceled.\n")
            return False

        if trans < 0:
            print("You must enter a positive amount.  Transaction canceled.\n")
            return False

        print("\nYou are transferring $" + "{:.2f}".format(trans) + " to", reciever.name)
        print("Authentication required")
        pin = input("Enter your PIN:")

        if int(pin) != self.pin:
            print("Invalid PIN. Transaction canceled.\n")
            return False

        else:
            print("Transfer authorized")
            print(self.name, "will transfer $" + "{:.2f}".format(trans), "to", reciever.name, ".")
            self.balance -= trans
            reciever.balance += trans
            return True

    def request_money(self, sender, rec_amt):
        if self.hold is True:
            return print(self.name + "'s account is on hold.  Transaction rejected.\n")
        if sender.hold is True:
            return print(sender.name + "'s account is on hold.  Transaction rejected.\n")

        if rec_amt > sender.balance:
            print("You must enter a lesser amount.  Transaction canceled.\n")
            return False

        if rec_amt < 0:
            print("You must enter a positive amount.  Transaction canceled.\n")
            return False

        print("\nYou are requesting $" + "{:.2f}".format(rec_amt), "from", sender.name)
        print("User authentication is required...")
        string = "Enter " + sender.name + "'s PIN:"
        sender_pin = input(string)

        if int(sender_pin) != sender.pin:
            print("Invalid PIN. Transaction canceled.")
            return False

        req_password = input("Enter your password:")

        if req_password != self.password:
            print("Invalid password.  Transaction canceled.\n")
            return False
        else:
            print("Request authorized")
            sender.balance -= rec_amt
            self.balance += rec_amt
            print(sender.name, "sent $" + "{:.2f}".format(rec_amt))
            return True





""" Driver Code for Task 1 """###########################################

""" user1 = User("Bob", 1234, "pass")
print(user1.name, user1.pin, user1.password) """


""" Driver Code for Task 2 """###########################################

""" user1 = User("Bob", 1234, "pass")
user1.change_name("Bobby")
user1.change_pin(1234, 4321)
user1.change_password("pass", "newpassword")
print(user1.name, user1.pin, user1.password) """

""" Driver Code for Task 3"""############################################

""" b_user1 = BankUser("Bob", 1234, "pass")
print(b_user1.name, b_user1.pin, b_user1.password, b_user1.balance) """

""" Driver Code for Task 4"""############################################

""" b_user1 = BankUser("Bob", 1234, "pass")
b_user1.show_balance()
b_user1.deposit(10)
b_user1.show_balance()
b_user1.withdraw(5)
b_user1.show_balance() """

""" Driver Code for Task 5"""

Bob = BankUser("Bob", 1234, "pass")
Alice = BankUser("Alice", 4321, "pass2")

print(Bob.hold)
Bob.on_hold()
print(Bob.hold)

Alice.deposit(5000)
Alice.show_balance()
Bob.deposit(3000)
Bob.show_balance()
trans_success = Alice.transfer_money(Bob, 500)
if trans_success == True:
    Alice.request_money(Bob, 400)

Bob.show_balance()
Alice.show_balance()

