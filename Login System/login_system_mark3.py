"""
In this project, I learned that using a dictionary to store user data makes the code much more compact and easier to understand, instead of writing multiple conditions like "if user == 'admin'" every time.

Here, I compare the login credentials with the dictionary, rather than checking against fixed strings repeatedly.
"""
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
