# check for rating for this movie
  ## universal -> everyone can watch
  ##pg, general viewing, some scenes may not be suitable for young children
  ## 12,
  ##15- no younger than 15
  ##18- no younger than 18 to watch



# rating='universal'
# rating='pg'
# rating=12
# rating=15
# rating=18




rating=int(input("What's the rating?"))
age=int(input('What is your age?'))

if age>=12 and rating==12:
    print('You can watch the 12+ fimls! ')

elif age<12 and rating==12 :
    print('You are too young to watch these films, try universal rating')

elif age<18 and rating==18:
    print('You are too young to watch these films, try 15+ and universal ratings')

elif age<15 and rating==15:
    print('You are too young for 15+, try universal')

elif age>=1 and rating=='0':
    print('You are old enough to watch the universal ratings')

elif age>18 and rating==18:

    print('You can watch the 18+ movies')

elif age >= 15 and rating == 15:
    print('You are too young for 15+, try universal')


else:
    print("Sorry, please try again")


