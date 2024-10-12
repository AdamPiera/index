names = ['Kamil', 'Mariusz', 'Dominik'] 
print(names)


del names[1]
print(names)


names.append('Mariusz')
names.append('Dominik')
print(names)


names[2] = 'Adam'


names.extend(['Paulina', 'Rafał'])
print(names)


print(names.count('Dominik'))
print(len(names))


print(names[0])


names.remove('Dominik')
print(names)


for name in names:
    print(name)


names.sort() #Sortuje według kolejności alfabetycznej
print(names)


names.sort(reverse=True) #Sortuje według kolejności alfabetycznej odwróconej
print(names)