from player import Player
from pokemon import Pokemon
player = Player(name='')
pokemon = Pokemon(name='')

def new_player():
    input_1 = input('What is your name?')
    input_2 = input(f'What city are you from?')
    player.save(f'{input_1}', f'{input_2}', '')
    Player(player.name)

print('Welcome to the Pokemon game')
print('Please enter your details')
new_player()
print('Thank you for submitting details, please proceed to the game')
player.search_for_pokemon()
while True:
    user_input = input('Would you like to search again?')
    if user_input == 'y':
        player.search_for_pokemon()
    else:
        break

