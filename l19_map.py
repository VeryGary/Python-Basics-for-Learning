#map,filtzer,zip,reduce

#Map
def mult_by2(li):
    new_list=[]
    for item in li:
        new_list.append(item*2)
    return new_list

#Need this for map, above one reutnrs a list obj, need jsut a function
#pure function that doesnt modify list
def mult_by2_2(item):
    return item*2

my_list=[1,2,3]

print(mult_by2([1,2,3]))
print()
print(map(mult_by2_2,[1,2,3]))#print where map obj is in memory
print(list(map(mult_by2_2,my_list)))
print(my_list)

