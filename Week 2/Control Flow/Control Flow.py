# Control Flow- Controlling where code runs or does not depending on our code making evaluations that return true or false
# Using if statements

#Agenda
#if
#else if -elif
## else
## switch or case


#Most specific information goes on top i.e. age AND licence above just age

age=int(input("What's your age?"))
driver_l=True

if age>=18 and driver_l==True:
    print('You can drive! ')
    print('and possibly drink depending on other things')

elif age>18:
    print('you can drive, once you take your driving licence')

elif age<18:
    print('sorry, you cannot drive You are too young')

else:
    print('sorry, you cannot drive')
