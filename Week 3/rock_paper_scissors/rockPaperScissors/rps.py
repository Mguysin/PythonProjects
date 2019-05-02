import random
list  = ['rock', 'paper', 'scissors']
print("random.choice() to select random item from list - ", random.choice(list))




input_value=input('Select rock, paper or scissors')

if input_value=='rock' and random.choice(list)=='rock':
    print('draw')


elif input_value=='scissors' and random.choice(list)=='scissors':
    print('draw')


elif input_value=='paper' and random.choice(list)=='paper':
    print('draw')

