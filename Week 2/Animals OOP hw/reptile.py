from oop_intro import Animal

# To create inheritance, pass in the Animal to the reptile
class reptile(Animal):

    def __init__(self):
        super()._init_() #this line of code needs to be here to initialise as an animal
        self.cold_blooded=True
        self.heart_chambers=[3,4]

    def seek_heat(self):
        print("Hmmm, need to find me some SUN! get that vitamin D")

    def hunt(self):
        print("wait...wait...wait...pounce!")

ringo = reptile()
ringo.poty()
ringo.eat()
ringo.seek_heat()
ringo.hunt()
ringo.breathe()


# ringo.hunt()

