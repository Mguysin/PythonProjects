from animals1 import Animals

class Monkey(Animals):

    def _init_(self):
        super()._init_()
        self.warm_blooded=True
        self.baboon=True
        self.furry=True
        self.friendly=True

    def scratch_body(self):
         print("scratch")

    def __grooming(self):
        print("scracth & search YUMM! Eat flee.")

    def play(self):
        print("playing hide and seek")

    def scream(self, sound = ''):
        print("eee eee eeee eee ou ou ou" + ' ' + sound)

    def sit_on_branch(self):
        print("Sitting...")
        self.play()
        self.__grooming()


#Running somewhere else creating mokeys and calling it's methods
johny=Monkey()
johny.scratch_body()
johny.eat()
johny.communicate()
johny.scream( 'Uhgaaa Uhgaa')
johny.sit_on_branch()