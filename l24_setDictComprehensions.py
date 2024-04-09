#Set Comprehensions
set1={char for char in 'hello'}
print(set1)
print()
set2={num for num in range(0,100,10)}
set3={num**2 for num in range(0,100,10)} #make a set of to power of 2 of the last
set4={num**2 for num in range(0,30) if num%2==0} #only even nums from 0-29
print(set2)
print(set3)
print(set4)
print()

#Dict comprehensions
simple_dict={
    'a':1,
    'b':2
}
dict1={key:value**2 for key,value in simple_dict.items()}#make a dict that squares values of simple dict
print(dict1)
dict2={key:value**2 for key,value in simple_dict.items() if value%2==0} #make dic with values that are even
print(dict2)
dict3={num:num*2 for num in [1,2,3]}
print(dict3)