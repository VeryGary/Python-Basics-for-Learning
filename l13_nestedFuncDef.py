def sum(num1,num2):
    def another_func(num1,num2):
        return num1+num2
    return another_func

total=sum(1,2)
print(total(3,7))

def sum2(num1,num2):
    def another_func2(num1,num2):
        return num1+num2
    return another_func2(num1,num2)

total2=sum2(1,2)
print(total2)