from player import Player
from pokemon import Pokemon

pokemon = Pokemon(name='')


def user_pokemon_add():

    input_1 = input('Please enter the pokemon name')
    # input_2 = int(input(f'What is the weight in KG of {input_1}?'))
    # input_3 = (input(f'How much is the grade of the {input_1}?'))
    # input_4 = input(f'Is the {input_1} treated YES/NO?')
    # input_5 = input(f'What is expiration date of {input_1}')
    pokemon.save(f'{input_1}')

print('Welcome, please select a option below')


print(user_pokemon_add())

while True:

    print('Option - 1 (Add player to the player List) \nOption - 2 (Print Player list)\n')
    user_input = int(input('Your selection >>'))

    if user_input == 1:
        user_pokemon_add()
        user_input = input('Do you wish to add another item? y/n')

        if user_input == 'y':
            user_pokemon_add()
        elif user_input == 'n':
            continue

    elif user_input == 2:
        print('Please see below the list')
        pokemon.load()

    else:
        print('Invalid entry please select a option from the list')

