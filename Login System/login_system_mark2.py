'''
Chat Gpt made me learn some things like while not, but is the same as while login == False that I used before, but using 'and' and 'or' made the code more understandable
In mark1 I tried using both and just made shit, a lot of logic errors bc they didnt work like i thought
'''
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
