from animals1 import Animals

class Bull(Animals):

    def _init_(self):
        super()._init_()
        self.warm_blooded=True
        self.horns=True
        self.big=True
        self.four_legs=True

    def show_horns(self):
         print("shows horns")

    def charges(self):
        print("charges ")

    def eat_grass(self):
        print("eats grass")

    def sit(self):
        print("Sits.")

bobby=Bull()
bobby.show_horns()
bobby.charges()
bobby.eat_grass()
bobby.sit()
bobby.run()
bobby.jump()
bobby.eat()

