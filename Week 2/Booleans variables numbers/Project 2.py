name=input('What is you name')
age=input('How old are you')

character_1= {
    'name':name,
    'age':age,
    'animal':[mouse, cat, dog],
    'event': ['party', 'games', 'holiday']
    'place':'town'
}

print(character_1[name])
print(f"Hi (name), because you are (age) years old you are going to read (name)'s adventure")
print(f"(character_1['name']) is a mouse who...")