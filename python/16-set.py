names = {'Kamil', 'Mariusz', 'Dominik'} #lista jest uporządkowana, a set nie, set nie pozwala na duplikaty, a lista tak
print(names)

names.add('Rafał')
print(names)

names.update(*s:'Adam',)

names.remove('Kamil')
print(names)

for name in names:
    print(name)