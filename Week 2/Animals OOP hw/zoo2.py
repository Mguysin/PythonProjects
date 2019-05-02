from zoo1 import Animals

class monkey(Animals):

    def _init_(self):
        super()._init_()
        self.warm_blooded=True
        self.baboon=True
        self.furry=True
        self.friendly=True

    def scratch_body(self):
         print("Scratch, scratch, scratch")

    def __play(self):
        print("Play,play play ")

    def scream(self):
        print("eee eee eeee eee ou ou ou")

    def sit_on_branch(self):
        print("Sitting...")

Johny=monkey()
Johny.scratch_body()
Johny.run()
Johny.eat()
Johny.communicate()
Johny.scream()
Johny.sit_on_branch()
Johny.__play()