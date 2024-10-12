# Draw Tree!!

#      *
#     ***
#    *****
#   *******
#  *********
# *********** 11
#      *

# height = 6
# height * 2 = 12 - 1 = 11

# def tree(height):
#     lenght = height * 2 - 1
#     stars = 1 
#     for i in range(1, height + 1):
#         print(("*" * stars).center(lenght))
#         stars += 2
#     print("*".center(lenght))
    
# tree(3)





# import random

# def game():
#     user_choice = input("Wybierz: kamień, papier, nożyce? ")
#     computer_choice = random.choice(["kamień", "papier", "nożyce"])
#     print(f"Komputer wybrał: {computer_choice}")
    
#     if user_choice == computer_choice:
#         print("Remis!")
#     elif (user_choice == "kamień" and computer_choice == "nożyce") or\
#          (user_choice == "papier" and computer_choice == "kamień") or\
#          (user_choice == "nożyce" and computer_choice == "papier"):
        
#         print("Wygrałeś!")
#     else:
#         print("Komputer wygrał!")
        
# game()





import math

def calculator():
    result = 0
    
    if operator == "+":
        result = num1 + num2
        
    elif operator == "-":
        result = num1 + num2
        
    elif operator == "*":
        num1 * num2
        
    elif result == "/":
        if num2 == 0:
            print("Nie można dzielić przez zero!")
        else:
            result = num1 / num2
            
    elif operator == "^":
        result = num1 ** num2
        
    elif operator == "sqrt":
        result = math.sqrt(num1)
    else:
        print("Nieprawidłowy operator")
        
    print("Wynik: ", result)
    
    
    
num1 = float(input("Podaj peirwszą liczbę: "))
operator = input("Podaj operator (+, -, *, /, ^, sqrt)")

if operator == "sqrt":
    calculator()
else:
    num2 = float(input("Podaj drugą liczbę: "))
    calculator()