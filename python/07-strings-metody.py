channel_name = '   jak nauCZyć się progRamowania'

print(channel_name.upper()) #JAK NAUCZYĆ SIĘ PROGRAMOWANIA
print(channel_name.capitalize()) #Jak nauczyć się programowania
print(channel_name.lower()) #jak nauczyć się programowania
print(channel_name.strip()) #usuwa białe znaki na początku stringa(spacje, tabulatory)

print(channel_name.startswith("j")) #sprawdza czy string zaczyna się na "j"
print(channel_name.endswith("a")) #sprawdza czy string kończy się na "a"

# metody stingów możemy ze sobą łączyć

print(channel_name.lower().strip().startswith("j")) #najpierw kompilator zmienia wszystkie znaki na małe, potem usuwa białe znaki, a potem sprawsza czy string zaczyna się ma "a"

print(channel_name.replace("progRamowania","jazdy na nartach")) #wyrażenie "progRamowania" zostanie zamienione na "jazdy na nartach"

print(channel_name.split(" ")) #dzieli stringa na podstawie podanego znaku(w tym przypadku spacji)