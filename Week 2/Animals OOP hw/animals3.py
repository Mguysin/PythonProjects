from animals1 import Animals

class Python(Animals):

    def _init_(self):
        super()._init_()
        self.cold_blooded=True
        self.snake=True
        self.long=True
        self.safe=True

    def hiss(self):
        print("hssssss")

    def crawl(self):
        print("zzzzzzzzzzz ")

    def byte(self):
        print("Byte")

    def twist(self):
        print("Twist")

lewy=Python()
lewy.hiss()
lewy.crawl()
lewy.eat()
lewy.communicate()
lewy.byte()
lewy.twist()

