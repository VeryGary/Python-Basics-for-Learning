#Need to import reduce from functools toolbelt
from functools import reduce

my_list=[1,2,3]
def accumulator(accum,item):
    print(accum,item)
    return accum+item
print(reduce(accumulator,my_list,0))
print(my_list)