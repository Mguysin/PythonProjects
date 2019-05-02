from animals1 import Animals

class Bear(Animals):

    def _init_(self):
        super()._init_()
        self.warm_blooded=True
        self.paws=True
        self.big=True
        self.four_legs=True

    def eat_hunny(self):
         print("eats hunny")

    def roars(self):
        print("roar!")

    def lie_down(self):
        print("lies")

    def yawns(self):
        print("yawn")


teddy=Bear()
teddy.eat_hunny()
teddy.roars()
teddy.lie_down()
teddy.yawns()

teddy.run()
teddy.communicate()
teddy.eat()