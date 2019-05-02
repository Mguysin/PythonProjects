import random



class Rpc_game():
    def __init__(self):
        self.player_input = 'nothing'
        self.computer_input = 'nothing'

    # Get user input (done)
    def get_user_input(self):
        # 1 ask/prompt user for input
        # store user input
        user_input = input('Enter rock, paper or scissors?')
        # change player input to user input
        self.player_input = user_input

    # Get computer random input
    def generate_computer_input(self):
        options=['rock', 'paper', 'scissors']
        # generate/select randomly from our 3 options
        rand_int=random.randint(0,2)
        print(options[rand_int])
        # changeself.computer_input to equate to the random choice
        self.computer_input=options[rand_int]


    # Compare results
    def game_result(self):
        # if player input= rock and computer=rock
            #draw
          if self.player_input==self.computer_input:
              return 'Draw'
          elif self.player_input=='rock' and self.computer_input=='paper':
              return'You lose'
          elif self.player_input=='rock' and self.computer_input=='scissors':
              return 'You win!'

          elif self.player_input == 'paper' and self.computer_input == 'rock':
              return 'You win!'

          elif self.player_input == 'paper' and self.computer_input == 'scissors':
              return 'You lose!'

          elif self.player_input == 'scissors' and self.computer_input == 'rock':
              return 'You lose!'

          elif self.player_input == 'scissors' and self.computer_input == 'paper':
              return 'You win!!'
          else:
              return 'Please type rock, paper or scissors'

    def run_game(self):

          while True:
              self.get_user_input()
              self.generate_computer_input()
              print(self.game_result())
              player_option_input=input('Play again?y/n')
              if player_option_input=='n':
                  break

game=Rpc_game()
game.run_game()



while True:
    game = Rpc_game()
    # game.get_user_input()
    game.generate_computer_input()
    print(game.game_result())