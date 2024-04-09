i=0
while i<3:
    print(i)
    i+=1
else:
    print('Finished while loop')

j=1
while j<10:
    print(j)
    break
else:
    print('This is the special case to show that else wont go if a break happens')

my_list = [1,2,3]
print(my_list)
i=0
while i<len(my_list):
    print(i)
    i+=1

while True:
    response=input('say something: ')
    if(response=='bye'):
        break
