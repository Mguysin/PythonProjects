story_1= {
    'Beginning': 'Beginning: Once upon a time, Ben went to the windmill',
    'Middle': 'Middle: Following this Ben found some grain and started to look for recipes',
    'End': 'End: Ben gathered resources and baked some bread',
}


gender=(input('Please tell us your gender'))
if gender=='male' or 'Male':
    print('Welcome sir')
else: print('Welcome madame')



input('Type your name to start the story')
print(story_1['Beginning'])
input('Press any key to see the middle of the story')
print((story_1['Middle']))
input('Press any key to see the end of story')
print(story_1['End'])


