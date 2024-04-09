#list comprehensions
#Quick way to create lists in python without looping or appending

#old slow way
li1=[]
for char in 'hello':
    li1.append(char)
print(li1)
print()

#with comprehensions
#li2=[param for param in iterable]
li2=[char for char in 'hello']
print(li2)
print()
li3=[num for num in range(0,100,10)]
li4=[num**2 for num in range(0,100,10)] #make a list of to power of 2 of the last
li5=[num**2 for num in range(0,30) if num%2==0] #only even nums from 0-29

print(li3)
print(li4)
print(li5)
