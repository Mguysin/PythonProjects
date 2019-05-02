class Monster_base():

    __monster_type='Base monster'


    def __init__(self, name_input='May', fur_amount='lots', eyes=67, limbs=1): #Abstraction of what it looks like
        self.fur=fur_amount
        self.eyes=eyes
        self.limbs=limbs
        self.name=name_input
        self.height='normal'

    def show_type(self):
        return self.__monster_type
    def walk(self):
        return("walking")
    def talk(self, string):
        return("i'm a monster, but I know english" + ' ' + string)




# define 3 methods for the animal class objects
# they should take in arguments
# one of the methods should take in optional arguments
