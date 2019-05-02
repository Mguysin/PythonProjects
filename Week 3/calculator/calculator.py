import self as self


class Calculator():
    def __init__(self):
        self.num1=0
        self.num2=0

    def generate_input_1(self):
        num1=int(input('Please enter the first number'))


    def generate_input_2(self):
        num2=int(input('Please enter the second number'))

    def user_input(self):
        user_selection=input('Select add, subtract, multiply or divide')


    def operation(self):
        user_operation=input('Select between add, subtract, multiply, divide')
        self.operation=user_operation

    def addition(self):
        addition=2+2
        print(addition)

    def subtraction(self):
        subtraction=2-2
        print(subtraction)

    def multiplication(self):
        multiplication=2*2
        print(multiplication)

    def division(self):
        division=2/2
        print(division)




    def calculator(self):

        user_input=(input('Enter operation (add, subtract, multiply, divide'))
        if user_input=='add':
            self.addition()
            print('addition')
        elif user_input=='subtract':
            self.subtraction()
            print('subtraction')
        elif user_input=='multiplication':
            self.multiplication()
            print('multiplication')
        elif user_input=='division':
            self.division()
            print('division')
            # else:
        # print('Please enter a valid value(addition, subtractio, multiplication, division')

