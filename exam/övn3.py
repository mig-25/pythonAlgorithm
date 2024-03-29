''' Skapa en lista för leta rätt på den största och minsta siffran i en lista
Låt användaren bestämma hur många siffor får finnas i listan
Använd metoden append för att lägga till tal i listan.
Anvävnd dig av metoden min och max i listor för att ta 
fram största och minsta talet i listan

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



def minMax(antal):
    
    # skapa en for loop, och sätt en övre gräns för loopen,
    # genom att använda dig av variablen för max antal som du skapat innan
    # lägg till varje siffra du läser in till listan
    for i in range(0, antal):
        nr = int(input("Mata in siffra: "))
        list.append(nr)

    # print största och minsta talet i listan
    print("Minsta siffran är:", min(list))
    print("Största siffran är:", max(list))
    
# fråga efter hur många siffror för plats i listan
antal = int(input("skriv antal siffror som listan får innehålla: "))

minMax(antal)
