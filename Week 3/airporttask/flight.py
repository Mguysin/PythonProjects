from passenger import *
from flight_details import *

class Flight(Passenger):
    def __init__(self, origin, destination, date):
        super()._init_()
        self.origin=''
        self.destination=destination
        self.date=date
        self.list_of_passengers = []
        self.plane = ''



    def add_plane(self, plane):
        self.plane=plane

    def add_passenger_to_list(self, passenger):
        # append to list the passanger
        self.list_of_passengers.append(passenger)






# destination_las_vegas=Flight('', 'Las Vegas')

flight_list=[]

flight_1=Flight('London', 'Paris', '26.04.2019')
flight_2=Flight('London', 'Berlin', '26.04.2019')
flight_3=Flight('London', 'Milan', '26.04.2019')
flight_4=Flight('London', 'Barcelona', '26.04.2019')
flight_5=Flight('London', 'Nice', '26.04.2019')

flight_list.append(flight_1)
flight_list.append(flight_2)
flight_list.append(flight_3)
flight_list.append(flight_4)
flight_list.append(flight_5)







while True:
    print('Welcome to the airport')
    selection=int(input('Select 1 for for list of flights, 2 to add passenger, 3 to select flight and passenger, 4 to add a chosen passenger to a chosen flight, 5 to add passsengers and see flight details'))
    # print(selection ==1)
    if selection == 1:
        print('list of flights is the following:')
        for data in flight_list:
            print(data.origin, data.destination)
        break
    elif selection == 2:
        print('Please fill in the following details to add passenger')
        name=input('Enter passenger name ')
        passport_number=input('Enter passport number')
        gender=input('Enter gender')
        nationality=input('Enter nationality')
        passenger = Passenger(name, passport_number, gender, nationality)
        print('Passenger details are the following:', name, passport_number, gender, nationality)
        # Need to create passenger objects
        break
    elif selection == 3:
        choice=int(input('Select a flight, between 1-4'))
        # Add existing passengers
        # Creating a passenger object
        # Hard coding, need dynamic
        # Print out the flights as in option 1 with formating to show the options/numbers that people can choose

        if choice == 1:
            print('You chose London-Paris')
            print('Please fill in the following details to add passenger')
            name = input('Enter passenger name ')
            passport_number = input('Enter passport number')
            gender = input('Enter gender')
            nationality = input('Enter nationality')
            print('Passenger confirmed, details are the following:', name, passport_number, gender, nationality)
            print('Destination is London-Paris')
        if choice == 2:
            print('You chose London-Madrid')
            print('Please fill in the following details to add passenger')
            name = input('Enter passenger name ')
            passport_number = input('Enter passport number')
            gender = input('Enter gender')
            nationality = input('Enter nationality')
            print('Passenger confirmed, details are the following:', name, passport_number, gender, nationality)
            print('Destination is London-Madrid')
        if choice == 3:
            print('You chose London-Milan')
            print('Please fill in the following details to add passenger')
            name = input('Enter passenger name ')
            passport_number = input('Enter passport number')
            gender = input('Enter gender')
            nationality = input('Enter nationality')
            print('Passenger confirmed, details are the following:', name, passport_number, gender, nationality)
            print('Destination is London-Milan')
        if choice ==4:
            print('You chose London-Zurich')
            print('Please fill in the following details to add passenger')
            name = input('Enter passenger name ')
            passport_number = input('Enter passport number')
            gender = input('Enter gender')
            nationality = input('Enter nationality')
            print('Passenger confirmed, details are the following:', name, passport_number, gender, nationality)
            print('Destination is London-Zurich')
    elif selection == 4:
        print('Adding existing passenger to a flight')
        for flights in flight_list:
            print(flights.origin, flights.destination, flights.date)
        flight_choice=int(input('Choose flight number, between 1-4'))
        if flight_choice == 1:
            print('You selected the flight', flight_list[0].origin, flight_list[0].destination, flight_list[0].date)
        elif flight_choice == 2:
            print('You selected the flight', flight_list[1].origin, flight_list[1].destination, flight_list[1].date)
        elif flight_choice == 3:
            print('You selected the flight', flight_list[2].origin, flight_list[2].destination, flight_list[2].date)
        elif flight_choice == 4:
            print('You selected the flight', flight_list[3].origin, flight_list[3].destination, flight_list[3].date)
        else:
            print('Please enter the correct value (1-4)')

        for passanger in passenger_list:
            print(passanger.name)
        passenger_choice = int(input('Select the passenger, 1-5'))
        if passenger_choice == 1:
            print('You selected the passenger', passenger_list[0].name, passenger_list[0].passport_number)
        elif passenger_choice == 2:
             print('You selected the passanger', passenger_list[1].name, passenger_list[1].passport_number)
        elif passenger_choice == 3:
            print('You selected the passenger', passenger_list[2].name, passenger_list[2].passport_number)
        elif passenger_choice == 4:
            print('You selected the passenger', passenger_list[3].name, passenger_list[3].passport_number)
        elif passenger_choice == 5:
            print('You selected the passenger', passenger_list[4].name, passenger_list[4].passport_number)
        else:
            print('Enter the correct value, 1-5')
    elif selection == 5:
        print('Please select to see the details of existing flight')
        for flights in flight_list:
            print(flights.origin, flights.destination, flights.date)
        flight_choice = int(input('Please select flight (1-4)'))
        if flight_choice == 1:
            print('You selected the flight', flight_list[0].origin, flight_list[0].destination, flight_list[0].date)
            print('The list of passengers are', passenger_list2[0].name, ',', passenger_list[1].name)
            print('Flight details are:', details_list[0].phone, details_list[0].terminal, details_list[0].destination)
        elif flight_choice == 2:
            print('You selected the flight', flight_list[1].origin, flight_list[1].destination, flight_list[1].date)
            print('The list of passengers is', passenger_list3[0].name, ',', passenger_list3[1].name)
            print('Flight details are:', details_list[1].phone, details_list[1].terminal, details_list[1].destination)
        elif flight_choice == 3:
            print('You selected the flight', flight_list[2].origin, flight_list[2].destination, flight_list[2].date)
            print ('The list of passengers is', passenger_list4[0].name)
            print('Flight details are:', details_list[2].phone, details_list[2].terminal, details_list[2].destination)
        elif flight_choice == 4:
            print('You selected the flight', flight_list[3].origin, flight_list[3].destination, flight_list[3].date)
            print('The list of passengers is', passenger_list5[0].name, ',', passenger_list[1].name)
            print('Flight details are:', details_list[3].phone, details_list[3].terminal, details_list[3].destination)
        else:
            print('Please enter the correct value (1-4)')








            # prompt user for input and store it in a variable(what flight would you like to go to)
            # use that number to get a flight object out of our flight list(flight_list[user_input)
            # call .add_passenger method on the flight object
                # send in a passenger object (create one or select from a list)







#
# test_flight=Flight()
#
# test_flight.add_plane()
#
# test_flight.add_origin()
#
# test_flight.add_destination()
#
# test_flight.add



