print('What is your name?')
name=input()





















#strings
#strings are characters inside quotes


my_string='hello'
print(my_string)


type('hello')
print(type('hello'))

#numbers inside quotes are also strings
print(type('9839424234723'))

#concatenation - adding 2 strings together
object_travolta="car"
variable_a='bicycle'
print("john" + " " + f"Travolta's {object_travolta} {variable_a}")
# f enables us to do interpolation i.e. turning {object} into what it meaans

#We cannotadd a number to a string
#e.g. (1+"1")

#calculating the length
#len()
example_text="Here is some text with lots of text "
print(len(example_text))

#Integers- numbers without the strings

print(type(97329473274823))

# Strip of white space
# .strip()
strip_variable=example_text.strip()
print(len(strip_variable))

print(example_text.count('text'))

#.lower()
#.upper()
#.capitalize()

#find something that helps me split my text in all white spaces

str = "THIS IS STRING EXAMPLE....WOW!!!";
print (str.lower())
print (str.upper())
print (str.capitalize())


txt = "hello, my name is Peter, I am 26 years old"
print(txt.split(" "))








