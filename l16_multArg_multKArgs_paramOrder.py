#rule of param order: def sum_function(params, *args, default parameters,**kwargs)

#*args
#Use any num of arguemnts
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

print()

# **kwargs
#Use anme num of keyword arguemtns
def super_func2(*args,**kwargs):
    print(kwargs)
    return sum(args)

print(super_func2(1,2,3,4,5, num1=5,num2=10))#print a dictionary

print()

def super_func3(*args,**kwargs):
    total=0
    print(kwargs)
    for items in kwargs.values():
        total+=items
    return sum(args) +total

print(super_func3(1,2,3,4,5, num1=5,num2=10))#print a dictionary
