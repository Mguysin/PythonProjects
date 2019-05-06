from pokemonNames.pokemonNames import PokemonNames

from connect_pokemon import*


class Pokemon():

    def __init__(self, name=''):
        self.name = name


    def get_name(self):

        generator = PokemonNames()
        pokemon = generator.get_random_name()
        self.name = pokemon


    def tackle(self):
        print('The pokemon runs towards you')

    def make_noise(self):
        print('The pokemon makes a sound')

    def rest_to_refill_health(self):
        print('The pokemon rests to refill health')

    def load(self):
        try:
            pokemons = sql_query_no_transaction("SELECT * FROM pokemon")
            for pokemon in pokemons:
                print(f"Name: {pokemon.Name}\n")
                Pokemon(pokemon.Name)
            print('Operation complete, read successful')

        except Exception as errmsg:
            print('There has been a error the record(s) have not been read, please see below exception message')
            print(errmsg)

    def save(self, name=''):
        try:
            sql_query_no_transaction(f"INSERT INTO pokemon(Name) VALUES('{name}');")
            docker_Pokemon.commit()
            print('The table has been updated, 1 row affected')

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)
