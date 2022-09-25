from donations_pkg.homepage import show_homepage, donate
from donations_pkg.user import login, register

database = {'admin': '123'}
donations = []
tot_don = 0
authorized_user = ''
show_homepage()

while True:
    if authorized_user == '':
        print('You must be logged in to donate.\n')
    else:
        print('Logged in as:', authorized_user)

    choice = input('Choose an option 1-5:')

    if choice == '1':
        username = input('Enter your username:')
        password = input('Enter your password:')
        authorized_user = login(database, username, password)
        show_homepage()

    elif choice == '2':
        username = input('Enter your username:')
        password = input('Enter your password:')
        authorized_user = register(database, username, password)
        if authorized_user != '':
            database[username] = password
        show_homepage()

    elif choice == '3':
        if authorized_user == '':
            print('You are not logged in.')
        else:
            donation_string, tot_don = donate(authorized_user, tot_don)
            donations.append(donation_string)
        show_homepage()

    elif choice == '4':
        if len(donations) == 0:
            print('Currently, there are no donations.')
        else:
            for i in donations:
                print(i)
            print('Total donations: $' + str(tot_don), '\n')
        show_homepage()

    elif choice == '5':
        print('Goodbye!')
        quit()
