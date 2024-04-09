is_old = True
is_licensed = False
if is_old and is_licensed:
    print('Both are true')
elif (not is_old) or (not is_licensed):
    print('One is false')
else:
    print('Both are false')

#Truthy and Falsy test
user1='Garrett' #truthy
pw1='password'  #truthy
user2='Steve'  #truthy
pw2=''  #Falsy bc empty
if user1 and pw1:
    print('You entered a username and password')
else:
    print('One of the fields is empty')
if user2 and pw2:
    print('You entered a username and password')
else:
    print('One of the fields is empty')

#Ternanry