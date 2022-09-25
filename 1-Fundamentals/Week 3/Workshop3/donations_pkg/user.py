def login(database, username, password):
    username = username.lower()
    password = password.lower()
    if username not in database.keys():
        print('User not found. Please register')
        return ''
    elif username in database.keys():

        if database[username] == password:
            print('Welcome', username + '!\n')
            return username
        else:
            print('Incorrect password for', username + '.')
            return ''

def register(database, username, password):
    username = username.lower()
    if len(username) > 10:
        print('Username must be less than 10 characters.')
        return ''
    if len(password) < 5:
        print('Password must be more than 5 characters.')
        return ''
    if username in database.keys():
        print('Username is taken.')
        return ''
    else:
        print('Username', username, 'has been registered.\n')
        return username





