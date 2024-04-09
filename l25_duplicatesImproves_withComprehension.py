#Find duplicates in this list
some_List=['a','b','c','d','m','n','n','b']
#use set as no duplicates, without would just be ['b', 'n', 'n', 'b']
duplicates=set([item for item in some_List if some_List.count(item)>1])
print(duplicates)
#can turn back to list by
duplicates=list(duplicates)
print(duplicates)

#in one line
duplicates2=list(set([item for item in some_List if some_List.count(item)>1]))
print(duplicates2)