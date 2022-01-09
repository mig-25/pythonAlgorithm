''' Skapa ett program för leta rätt på den största och minsta siffran i en lista
Låt användaren bestämma hur många siffor får finnas i listan
Anvävnd dig av metoden min och max för detta

Exempel:
skriv antal siffrar som listan får innehålla: 4
Mata in siffra: -4567
Mata in siffra: 4
Mata in siffra: 67
Mata in siffra: 456678
Minsta siffran är: -4567
Största siffran är: 456678 '''

# skapa en tom lista
list = []

# fråga efter hur många siffror för plats i listan
maxNrInList = int(input("skriv antal siffrar som listan får innehålla: "))

# skapa en for loop, och sätt en övre gräns för loopen,
# genom att använda dig av variablen för max antal som du skapat innan
# lägg till varje siffra du läser in till listan
for i in range(0, maxNrInList):
    nr = int(input("Mata in siffra: "))
    list.append(nr)

# print största och minsta talet i listan
print("Minsta siffran är:", min(list))
print("Största siffran är:", max(list))
