import random

class Rpc_game():
    def __init__(self):
        self.player_input='nothing'
        self.computer_input='nothing'

    #Get user input
    def get_user_input(self):
        #1 ask/prompt user for input
        #store user input
        user_input = input('Enter rock, paper or scissors?')
        #change player input to user input
    #Get computer random input
    #Compare results