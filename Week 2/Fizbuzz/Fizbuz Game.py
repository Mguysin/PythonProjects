string_nums_fiz_buzz_fizzbuzz = ''
# string_nums_fiz_buzz_fizzbuzz = '1 2 ...... 14 fizzbuzz '
first_value = int(input("Start Value:"))
last_value = int(input("End Value:"))
example_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for i in example_range:
    if i%3 == 0:
        string_nums_fiz_buzz_fizzbuzz += "fizz" # if i is divisible by 3 , print fizz
    if i%5 == 0:
        string_nums_fiz_buzz_fizzbuzz += "buzz" # if i is divisible by 5 , print buzz
    if i%3 != 0 and i%5 != 0:
        string_nums_fiz_buzz_fizzbuzz += str(i)

    string_nums_fiz_buzz_fizzbuzz += ' '

print(string_nums_fiz_buzz_fizzbuzz)