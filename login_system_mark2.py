login = False

while not login:
    user = input('Enter username: ')

    if user == 'admin' or user == 'user':
        password = input('Enter password: ')

        if user == 'admin' and password == 'adminpassword123':
            print('Welcome, Admin!')
            login = True

        elif user == 'user' and password == 'userpassword123':
            print('Welcome, User!')
            login = True

        else:
            print('Wrong password, try again!')

    else:
        print('No valid user, try again!')