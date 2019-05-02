# counter=1
# movie_list=['Die Hard', 'Terminator', 'Batman', 'Superman']
# for values in movie_list:
#     print(counter, '>' + values)
#     counter +=1
#
#
# # Don't know how to number
# counter=1
# places_list=['Spain', 'Italy', 'France', 'Luxemburg']
# for values in places_list:
#     print(counter, '>' + values)
#     counter +=1




movies = {
    'Die Hard':'USA',
    'Lord of the rings':'New Zealand',
    'Terminator':'Australia',
    'Batman': 'New York',
    'Superman':'Washington'
}

print(movies['Die Hard'])
counter=1
for movie_key in movies:
    print('This is the movie:', counter, movie_key, movies[movie_key])
    counter +=1


#Don't know how to number




# Create a game that runs until a magic number is found(while+if+break)
# guess=int(input('Enter a number'))

# while (guess==7):
# print('You found the magic number')
# if guess>7:
#     print('Number is too big')
# if guess<7:
#     print('Number is too small')
# else:
#     ('Type in a number')
#
# #Check if number is prime
# # number = int(input("Enter any number: "))
#
# # prime number is always greater than 1
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
#
# # if the entered number is less than or equal to 1
# # then it is not prime number
# else:
#     print(number, "is not a prime number")


#Program to count the number of individual characters in a string
#
# count=input("Enter a string")
# print(len(count))
