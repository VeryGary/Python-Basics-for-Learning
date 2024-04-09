
total = 0

def count():
    global total #get asccess total var
    total+=1
    return total

print(total)
print(count())
print(total)