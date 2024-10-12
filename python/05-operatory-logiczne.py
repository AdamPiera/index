isSkyBlue = True
isPythonDifficult = False

print(isSkyBlue and isPythonDifficult)
print(isSkyBlue or isPythonDifficult)

a = 5
b = 2

print(a > b and b > 0)
print(a > b and b > 3)
print(a > 10 or b > 0)
print(a > 10 or (b > 0 and a < b))


c = 4
print(c % 2 == 0) # zwaraca True dla parzystej, False dla nieparzystej

print(not c % 2 == 0) # zwaraca True dla nieparzystej, False dla parzystej


userLoggedIn = False

if userLoggedIn:
    print("Użytkownik zalogowany")
    
if not userLoggedIn:
    print("Użytkownik niezalogowany")