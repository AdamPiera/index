def add(a, b):
    print(a + b)
    
a = 3 
b = "2"

add(str(a), b) # wywołuje funkcje

print(a + int(b)) #zmienia wartość zmiennej b na intiger tylko na potrzeby wyświetlenia
b = int(b) #zmienia całkowicie wartość zmiennej b na intiger

#str() zmienia liczbe na string
#int() zmiena string na liczbe


print(type(a)) #wyświetla typ zmiennej
print(type(b))


c = 2
print(type(c))
#  |
# \|/

c = "kamil"
print(type(c))
#  |
# \|/

c = True
print(type(c))