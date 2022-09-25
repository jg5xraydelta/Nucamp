def show_homepage():
    print('        === DonateMe Homepage ===')
    print('---------------------------------------------')
    print('| 1.    Login       | 2.     Register        |')
    print('---------------------------------------------')
    print('| 3.    Dontate     | 4.     Show Donations  |')
    print('---------------------------------------------')
    print('|                5.   Exit                   |')
    print('---------------------------------------------')

def donate(username, tot_don):
    username = username.lower()
    while True:
         try:
             donation_amt = int(input("Please enter a number: "))
             while donation_amt <= 0:
                donation_amt = int(input("Please enter a number greater than zero: "))
             break
         except ValueError:
             print("Oops!  That was no valid number.  Try again...")
    
    while donation_amt <= 0:
        print('Please enter an amount greater than zero.')
        
    tot_don += int(donation_amt)
    donation_string = username + ' donated $' + str(donation_amt)
    print('Thank you for your donation', username + '!\n')
    return donation_string, tot_don

