# age = input("Ile masz lat? ")
# age = int(age)

# if age >= 18:
#     print("Jesteś pełnoletni(-a)")
# else:
#     print("Jesteś niepełnoletia(-a)")

light = input("Jakie jest światło? (zielone, żółte, czerwone) ")

if light == "zielone":
    print("Możesz jechać!")
    
elif light == "żółte":
    print("Jeszcze chwila")
    
elif light == "czerwone":
    print("Nie możesz jechać")
    
else:
    print("Niewłaściwy kolor")
