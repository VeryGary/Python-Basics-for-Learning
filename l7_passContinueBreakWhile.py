#continue resets to start of loop and reiterates
for i in range(4):
    print(i)
    pass #just passes to next line, good for placeholding but not useful
    continue

for j in range(4):
    continue
    print(j) #this will be skipped

for k in range(4):
    pass #usefullness of pass just for testing and stuff not empty
