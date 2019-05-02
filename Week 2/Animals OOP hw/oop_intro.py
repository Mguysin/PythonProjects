#OOP- object orientated programming

# 4 pillars: abstraction, polymorphism, encapsulation, inheritance

# Abstraction

class Animal:

    #1)define how it looks, by initializing
    #2) create methods for this class object

    def _init_(self):
        self.alive=True
        self.spine=True
        self.eyes=True
        self.lungs=True
    def _breathe_(self):
        print("INNNNN...andddddd.....OUTTTTT")

    def eat(self):
        print('Nom nom nomnomnomnonmnom')

    def poty(self):
        print('... 0.0 .....Splosh...0.0')

# cat= Animal()
# cat._breathe_()
# cat.eat()
# cat.poty()




