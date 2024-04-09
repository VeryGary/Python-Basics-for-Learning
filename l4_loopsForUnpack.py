#For loop that parses through each item in string
for item in 'Garrett':
    for x in ['a','b','c']:
        print(item,x)

#items in a list
for item in [1,2,3]:
    print(item)
    print(item)
print('hi')
print(item)#by the time loop end item stores 3

#dictionary
user = {
    'name': 'Golem',
    'age': 5000,
    'can_swim': False
}
for item in user:
    print(item,user.get(item))
for key,value in user.items():
    print(key,value)
#output values foe each key
for item in user.values():
    print(item)
#Output keys
for item in user.keys():
    print(item)
for x in range(10,0,-1):
    print(x)