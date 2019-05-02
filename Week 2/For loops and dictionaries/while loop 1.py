cars=['Ferrari', 'Fiat Panda', 'Fiat Panda 4*4', 'Skoda Felicia Fun']



max_size_list=len(cars)
counter=-1
number=-1


while counter<max_size_list -1:
    counter=-1
    number=1
    while counter < max_size_list -1:
        counter +=1
        print(str(number) + ' ~ ' + cars[counter])
        number+=1




while True:
    user_input = input("Please input a value")
    if user_input == 'exit':
        break
    elif user_input=='cute':
        print('jigglypuff...<3')
    else:
        print('JIGGLYPUUUFFF')

#keep asking for user input
   #break if user types in exit






#Pseudo Code
# We have a list of cars
# Its in a variable called cars
# I can access using the index
# Let's start by printing each car using the index
