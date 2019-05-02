crazy=['Snow', 'The north', 'Cerci', 'Kings Landig']

# Lists not efficient as data not connected
#Would be useful tp provide aadditional information e.g. where lives/previous work experiece/previous education/previous test results
#Saves time as don't have to spend time looping through information

#Dictionaries
# Dictionaries keep information with keys and value pairs
# In dictionaries you do not look up an index- insted a key.
# Much like looking up a word in the dictionary

# key= reference to object
# values/s - whatever data is stored- could be a string, number or even other dictionaries.

#Defiining/creating a dictionary (also known as hash in ruby or object in JS)
student_1= {
    'name': 'Arya',
    'stream': 'DevOps',
    'grades': 5,
    'completed modules':['git', 'github', 'business week', 'variables', 'data types']

}

print(student_1)
print(type(student_1))

#Access values of keys
print(student_1['stream'])
print(student_1['completed modules'])
print(student_1['completed modules'][2])

# array_modules=student_1['completed modules']
# print(array_modules[2])


#Defiining/creating a dictionary (also known as hash in ruby or object in JS)

student_1['name']='A Girl has no name'
print(student_1)


# Adding 2 modules to 'completed modules' within student_1 dictionary

student_1['completed modules'] += ['Armour', 'Guns']
print(student_1)

#Accessing just 1 of modules
print(student_1['completed modules'][2])
print(student_1['completed modules'].count('Armour'))




student_1['completed modules'].append('Bullets')
print(student_1['completed modules'])

weapons='Missiles'
student_1['completed modules'].append(weapons)
print(student_1['completed modules'])
print(student_1['completed modules'][-1])











