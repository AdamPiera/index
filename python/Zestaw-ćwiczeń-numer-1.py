# 1. Napisz program, który sprawdza, czy podana przez użytkownika liczba jest parzysta czy nieparzysta

# number = float(input("Podja liczbę: "))

# if number % 2 == 1:
#     print("Podana liczba jest nieparzysta.")
# else:
#     print("Podana liczba jest parzysta.")





# 2. Napisz program, który spawdza, czy podana przez użytkownika liczba jest większa od 0, mniejsza od 0, równa 0

# number1 = float(input("Podaj liczbę: "))

# if number1 == 0:
#     print("Podana liczba jest równa 0.")
# elif number1 > 0:
#     print("Podana liczba jest większa niż 0.")
# else:
#     print("Podana liczba jest mniejsza niż 0")





# 3. Napisz porgram, który zapyta użytkownika o wynik na egzamienie (od 0 do 100) i wyświetli odpowiednią ocenę:
# 90 - 100 -> 5
# 80 - 89 -> 4
# 70 - 79 -> 3
# 60 - 69 -> 2
# poniżej 60 -> 1

# number2 = int(input("Podaj ocenę z egzaminu: "))

# if number2 >= 90:
#     print(5)
# elif number2 >= 80 and number2 <= 89:
#     print(4)
# elif number2 >= 70 and number2 <= 79:
#     print(3)
# elif number2 >= 60 and number2 <= 69:
#     print(2)
# elif number2 < 60:
#     print(1)





# 4. Napisz program, który wyświetli liczby od 0 do 100

# for i in range(1, 101):
#     print(i)
#     i += 1





# 5. Napisz program, który wyświetli wszystkie liczby pierwsze od 0 do 100
# i = 1
# while i < 101:
#     if (i / 1 == i and i / i == 1):
#         print(i)
#     i += 1
#     # j = i + 2
#     # if j - i == 2:
#     #     print(i)
#     # i += 2
#     # print(i)



# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych z przediału 1 - 100

# sumaParzystych = 0
# i = 0
# while i < 101:
#     if i % 2 == 0:
#         sumaParzystych = sumaParzystych + i
#     i += 1
    
# print(sumaParzystych)





# 7. Napisz program, który policzy pole prostokąta (użytkownik musi podać długości boków)

# a = float(input("Podaj dłógość boku a: "))
# b = float(input("Podaj dłógość boku b: "))

# area = a * b
# print("Pole prostokąta to:",area)





# 8. Napisz program, który spawdzi, czy podane przez użytkownika imię jest imieniem męskim
# czy żeńskim (załóż, że imiona żeńskie kończą się na literę a)

# name = input("Podaj imię: ").lower().strip()

# if name.endswith("a"):
#     print("Podanie mnię jest imieniem żeńskim.")
# else:
#     print("Podanie mnię jest imieniem męskim.")





# 9. Pobierz od użytkownika trzy liczby całkowite i uporządkuj je w kolejności od najmniejszej do największej

# a = float(input("Podaj pierwszą liczbę całkowitą: "))
# b = float(input("Podaj drugą liczbę całkowitą: "))
# c = float(input("Podaj trzecią liczbę całkowitą: "))

# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
    
# print(f"{a}, {b}, {c}")





# 10. Stwórz grę, w której wylosujesz liczbę z przediału od 1 do 100, zapiszesz tą liczbę do zmiennej,
# a następnie poprosisz użytkownika o odgadnięcie tej liczby. Po każdej próbie wyświetlaj informacje, czy
# liczba podana przez użytkownika jest mniejsza czy większa od wylosowanej. Gdy użytkownik odgadnie liczbę, zakończ gre
# Dodatkowe zadanie (w ramach tego ćwiczenia):
# Znajdż informacje, w jaki sposób losować liczby całkowite w Pythonie.



import random

number = random.randint(1, 100)
userNumber = 0
proba = 1

while number != userNumber:
    if userNumber > number:
        print("Komputer wylosował mniejszą liczbę.")
        userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
    elif userNumber < number:
        print("Komputer wylosował większą liczbę.")
        userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
    print(f"""""")
    proba += 1
        
print(f"Odgadłeś liczbę w próbie {proba - 1}.")





# import random

# def easy():
    
#     number = random.randint(1, 50)
#     userNumber = 0
#     proba = 1

#     while number != userNumber:
#         if userNumber > number:
#             print("Komputer wylosował mniejszą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         elif userNumber < number:
#             print("Komputer wylosował większą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         print(f"""""")
#         proba += 1
            
#     print(f"Odgadłeś liczbę w próbie {proba - 1}.")
#     cho()
    
    
    
    
    
# def normal():
    
#     number = random.randint(1, 100)
#     userNumber = 0
#     proba = 1

#     while number != userNumber:
#         if userNumber > number:
#             print("Komputer wylosował mniejszą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         elif userNumber < number:
#             print("Komputer wylosował większą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         print(f"""""")
#         proba += 1
            
#     print(f"Odgadłeś liczbę w próbie {proba - 1}.")
#     cho()    
    
    
    
    
# def hard():
    
#     number = random.randint(1, 1000)
#     userNumber = 0
#     proba = 1

#     while number != userNumber:
#         if userNumber > number:
#             print("Komputer wylosował mniejszą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         elif userNumber < number:
#             print("Komputer wylosował większą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         print(f"""""")
#         proba += 1
            
#     print(f"Odgadłeś liczbę w próbie {proba - 1}.")
#     cho()
    
    
    
    
    
# def extreme():
    
#     number = random.randint(1, 10000)
#     userNumber = 0
#     proba = 1

#     while number != userNumber:
#         if userNumber > number:
#             print("Komputer wylosował mniejszą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         elif userNumber < number:
#             print("Komputer wylosował większą liczbę.")
#             userNumber = int(input(f"Odgadnij liczbę jaką wylosował komputer. Twój wybór to ({proba}): "))
#         print(f"""""")
#         proba += 1
            
#     print(f"Odgadłeś liczbę w próbie {proba - 1}.")
#     cho()
    
    
# def cho():
#     print(f"""""")
#     choice = int(input("Wybierz tryb gry (łatwy - 1, normaly - 2, trudny - 3, ekstremalny - 4): "))
#     match choice:
#         case 1:
#             easy()
#         case 2:
#             normal()
#         case 3:
#             hard()
#         case 4:
#             extreme()
# cho()
