def dough(water, wheat):
    # print(f'Mixing {water} with {wheat}')
    if water=="water" and wheat=="wheat":
        return 'dough'
    else:
        return'blob of mixture'

def bake(substance):
    if substance=='dough':
        return 'bread'
    else:
        return 'not bread :('

def bread_factory(substance_1, substance_2):
    output_dough=dough(substance_1, substance_2)
    return bake(output_dough)


bread_factory('water', 'flour')

# output=dough('water', 'wheat')
# print(output)
# print(output == 'dough')
#
#
# print(output=='dough')

# Test and TDD
print(dough('water', 'wheat')== 'dough')

print(bake('dough')=='bread')
print(bake('dough'))
print(bake('brick')=='not bread.. :( ')


# for our bread factory
# we should put water and dough and get out bread
     # if we put something else we should get 'not bread.. :( '
print('testing factory with water and wheat- expect output to be bread')
print(bread_factory('water', 'wheat')=='bread')
print(bread_factory('water', 'wheat'))

print('testing factory with water and cement- expext output to be not bread .. :( ')
print(bread_factory('water', 'cement')== 'not bread.. :( ')
print(bread_factory('water', 'cement'))

