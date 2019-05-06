from connect_player import*

class Pokemon():

    def __init__(self, name):
        self.name = name

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

    def save(self, Name):
        try:
            sql_query_no_transaction(f"INSERT INTO pokemon(Name) VALUES('{Name}');")
            docker_Pokemon.commit()
            print('The table has been updated, 1 row affected')

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)
