# skapa en tom lista
list = []



def sumNrs(antal):
    
    # skapa en for loop, och sätt en övre gräns för loopen,
    # genom att använda dig av variablen för max antal som du skapat innan
    # lägg till varje siffra du läser in till listan
    for i in range(0, antal):
        nr = int(input("Mata in siffra: "))
        list.append(nr)

    # print summan av talet i listan
    print("svaret är:", sum(list))
    
# fråga efter hur många siffror för plats i listan
antal = int(input("skriv antal siffror som listan får innehålla: "))

sumNrs(antal)
