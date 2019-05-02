from zoo1 import Animals

class python(Animals):

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

Lewy=python()
Lewy.hiss()
Lewy.crawl()
Lewy.eat()
Lewy.communicate()
Lewy.byte()
Lewy.twist()
