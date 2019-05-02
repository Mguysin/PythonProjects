import random
class Game:
    def _init_(self):

      self.game=True


    # def rock(self):
    #     print("rock")
    # def paper(self):
    #     print("paper")
    # def scissors(self):
    #     print("scissors")



list  = ['rock', 'paper', 'scissors']
print("random.choice() to select random item from list - ", random.choice(list))


input_value=input('Select rock, paper or scissors')

if input_value=='rock' and random.choice(list)=='rock':
    print('draw')


if input_value=='scissors' and random.choice(list)=='scissors':
    print('draw')


if input_value=='paper' and random.choice(list)=='paper':
    print('draw')




elif input_value=='scissors' and random.choice(list)=='paper':
    print('you win')
elif input_value=='stone' and random.choice(list)=='scissors':
    print('you win')
elif input_value=='paper' and random.choice(list)=='stone':
    print('you win')



elif input_value=='scissors' and random.choice(list)=='stone':
    print('you lose')
elif input_value=='stone' and random.choice(list)=='paper':
    print('you lose')
elif input_value=='paper' and random.choice(list)=='scissors':
    print('draw')









# elif input('Select rock, paper or scissors')=='paper' and random.choice(list)=='paper':
#     print('draw')
# elif input('Select rock, paper or scissors')=='scissors' and random.choice(list)=='scissors':
#     print('draw')
#
# elif input('Select rock, paper or scissors')=='paper' and random.choice(list)=='stone':
#     print('you win')
# elif input('Select rock, paper or scissors')=='scissors' and random.choice(list)=='paper':
#     print('you win')
# elif input('Select rock, paper or scissors') == 'stone' and random.choice(list) == 'scissors':
#     print('you win')


# elif input('Select rock, paper or scissors') == 'scissors' and random.choice(list) == 'stone':
#     print('you lose')
# elif input('Select rock, paper or scissors') == 'paper' and random.choice(list) == 'scissors':
#     print('you lose')
# elif input('Select rock, paper or scissors') == 'stone' and random.choice(list) == 'paper':
#     print('you lose')

