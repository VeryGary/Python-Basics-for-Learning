#Find duplicates in this list
some_List=['a','b','c','d','m','n','n','b']
duplicates=[]
for value in some_List:
    if some_List.count(value) > 1 :
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
