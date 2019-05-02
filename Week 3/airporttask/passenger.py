from person import Person

class Passenger(Person):
    def __init__(self, name, passport_number):
        super()._init_()
        self.name=name
        self.passport_number=passport_number

# name=input('What is your name?')
# passport_number=input('What is your passport number?')

# john=Passenger(name, passport_number)
# print(john.name)
# print(john.passport_number)

# Need to create passengers

passenger_list=[]

passenger_1=Passenger('John', 1457)
passenger_2=Passenger('Lewis', 1757)
passenger_3=Passenger('Tony', 1957)
passenger_4=Passenger('James', 1457)
passenger_5=Passenger('Piers', 1957)

passenger_list.append(passenger_1)
passenger_list.append(passenger_2)
passenger_list.append(passenger_3)
passenger_list.append(passenger_4)
passenger_list.append(passenger_5)


passenger_list2=[]

passenger_list2.append(passenger_1)
passenger_list2.append(passenger_2)


passenger_list3=[]

passenger_list3.append(passenger_3)
passenger_list3.append(passenger_4)


passenger_list4=[]

passenger_list4.append(passenger_5)



passenger_list5=[]
passenger_list5.append(passenger_1)
passenger_list5.append(passenger_3)
