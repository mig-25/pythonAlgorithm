''' Skapa en siffer gisningsspel där du får gissa talen mellan siffrorna
1 till 10, du får max 5 försök.
Importera random för att slumpa tal mellan 1 till 10, spara sedan 
det i en variabel.
Du måste använda dig av en for loop.
Läs in spelarens namn, och printa ut enligt nedan.
Läs sedan in en siffra, det nr du vill gissa på

OBS! att du måste visa för varje rad, hur många gissningar dittills,
samt det gissade talet, sedan om det är för lågt, för högt, enligt exemplet nedan

eller om rätt gissat, printa:
Din gissning nr: (visa vilken försök nr) på siffran )(siffran för den rätta gissning)
är rätt efter (visa vilken försök nr) försök
Se nedan som exempel

Exempel på övning och utfallet i terminalen:
    
Tjenis, vad heter du? kalle
Okay kalle, gissa ett tal mellan 1 till 10
Gissa siffran: 5
Din gissning nr: 1 på siffran 5 är för lågt
Gissa siffran: 7
Din gissning nr: 2 på siffran 7 är för högt
Gissa siffran: 6
Din gissning nr: 3 på siffran 6 är rätt efter 3 försök '''

import random

number = random.randint(1, 10)

player_name = input("Tjenis, vad heter du? ")


print(f"Okay {player_name}, gissa ett tal mellan 1 till 10")


def guessNr():

    for i in range(1, 6):
        counter = 0
        guess = int(input("Gissa siffran: "))
        counter = counter + i
        if guess < number:
            print(f"Din gissning nr:{counter} på siffran {guess} är för lågt")
        if guess > number:
            print(f"Din gissning nr:{counter} på siffran {guess} är för högt")
        if guess == number:
            break
    if guess == number:
        print(
            f"Din gissning nr:{counter} på siffran {guess} är rätt efter {counter} försök")
    else:
        # print('Dinna gissningar var fel, den rätta numret är:  ' + str(number))
        print(f"Dinna gissningar var fel, den rätta numret är: {str(number)}")


#guess = int(input("Gissa siffran: "))
guessNr()
