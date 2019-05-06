from connect_player import*
import random

class Player():

    def __init__(self, name):
        self.name = name
        self.city = ''
        self.pokemon_caught = []

    # def search_for_pokemon(self):
    #     pass
    #
    # def try_to_catch_pokemon(self):
    #     pass


    def __try_catch_pokemon(self):
        user_input = input('Would you like to try and catch this pokemon?')
        if user_input == 'y':
            print('Thowing Pokeball!')
            catch = random.randint(0, 10)
            if catch >= 5:
                poke = Pokemon(self.name)
                poke.get_name()
                new_pokemon = print('You caught a..', poke.name)
                self.pokemon_caught.append(new_pokemon)
                self.save_player_and_pokemon('' , '' , f'{poke.name}')

            elif catch <= 5:
                print('The pokemon got away, better luck next time')

    def search_for_pokemon(self):
        print('Searching for a pokemon!')
        self.__try_catch_pokemon()




    def save(self, name='', city='', pokemon_caught=''):
        try:
            sql_query_no_transaction(f"INSERT INTO player(Name, City, Pokemon_caught) VALUES('{name}', '{city}', '{pokemon_caught}');")
            docker_Pokemon.commit()
            print('The table has been updated, 1 row affected')

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)



    def load(self):
        try:
            players = sql_query_no_transaction("SELECT * FROM player")
            for player in players:
                print(f"Name: {player.Name}\nCity: {player.City}\nPokemon caught: {player.Pokemon_caught}")
                Player(player.Name, player.City)
            print('Operation complete, read successful')

        except Exception as errmsg:
                print('There has been a error the record(s) have not been read, please see below exception message')
                print(errmsg)



