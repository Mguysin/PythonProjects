class flight_details:
    def __init__(self, phone , terminal, destination):
        self.phone = phone
        self.terminal = terminal
        self.destination = destination


details_list=[]

details1 = flight_details('073736374634', 'terminal 1', 'France')
details2 = flight_details('07386483483', 'terminal 2', 'Spain')
details3 = flight_details('0778374834387', 'terminal 3', 'Italy')
details4 = flight_details('077364364333', 'terminal 1', 'Germany')

details_list.append(details1)
details_list.append(details2)
details_list.append(details3)
details_list.append(details4)