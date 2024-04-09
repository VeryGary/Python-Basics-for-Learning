#default paramseters
def say_name(name='default name', gender='default gender'):
    print(f'Hello {name} your gender is {gender}!')

#arguements
say_name('Garrett','Male')
#Keyword arguements work regardless of position in arguemnts statement
say_name(gender='Dog',name='Rufus')
#Test Default arguements
say_name()