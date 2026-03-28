login = False
'''Login 1 = admin | Login 2 = user | Password 1 = adminpassword123 | Password 2 | userpassword123'''
#Ngl, I spent some really good time getting the logic behind this to work and when I changed something it stopped working lol, but it was a challenge for my level rn
#I will try to explain it bc I actually need to understand better this
#First i made the variable login bc i wanted to make a loop without while True, then i defined that login was False, and to make the loop, when login was false, i ran the code
#My logic was simply: right login -> login == True, then it would stop the loop, obviously it was not that simple for me to code that
while login == False:
  l = input('Enter the login credentials:')
  if l == 'admin':
    password = input('Enter the password')
    if password == 'adminpassword123':
      print ('Welcome, Admin!')
      login = True
    else:
      print ('Wrong password, try again!')
  elif l == 'user':
    password = input('Enter the password')
    if password == 'userpassword123':
      print ('Welcome, User!')
      login = True
    else:
      print ('Wrong password, try again!') 
  else:
    print ('No valid user, try again!')


  


   
 

