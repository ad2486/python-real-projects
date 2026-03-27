print('Welcome to the calculator!')
print('Enter the operation you want to perform, for example: 2 + 2, and use spaces between the numbers and the operator.')
print('The available operators are: +, -, *, /')

o1 = input('Enter the operation: ')
o2 = o1.strip().split()

if len(o2) != 3:
    print("Invalid input! Please enter in the format: number operator number (e.g. 2 + 2)")
else:
    try:
        num1 = float(o2[0])
        num2 = float(o2[2])
    except ValueError:
        print("Invalid numbers! Please enter valid numbers.")
    else:
        if o2[1] == '+':
            print('The result is:', num1 + num2)
        elif o2[1] == '-':
            print('The result is:', num1 - num2)
        elif o2[1] == '*':
            print('The result is:', num1 * num2)
        elif o2[1] == '/':
            print('The result is:', num1 / num2)
        else:
            print('Invalid operator. Please use one of the following: +, -, *, /')
