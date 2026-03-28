users = {
    'admin': 'adminpassword123',
    'user': 'userpassword123'
}

login = False

while not login:
    username = input('Enter username: ')
    
    if username in users:
        password = input('Enter password: ')
        
        if password == users[username]:
            print(f'Welcome, {username}!')
            login = True
        else:
            print('Wrong password, try again!')
    else:
        print('No valid user, try again!')