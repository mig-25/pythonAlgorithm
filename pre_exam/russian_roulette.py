""" skapa ett spel för en revolver med sex platser i magasinet,

du får sex försök att skjuta dig själv i huvudet.

Du måste hålla koll på varje försök att skjuta

om talet du gissar är för lågt än det som ligger dolt i revolvern, så skriv ut detta,

eller om talet du gissar är för högt än det som ligger dolt i revolvern, så skriv ut detta, 

annars gissningen är rätt eller att du matar in ett ogiltig gissning, alltså högre än 6,
så lämmnar du loopen med texten du är död efter x försök
eller om din gissning var högre än sex så skriv ut ogiltig värde,
annars om du har gissat fel alla gånger, så skriv du lever, och kulan låg på platsnr, du kan omvandla det till en str """

import random

number = random.randint(1, 6)
print("Låt oss spela rysk roulette, hur länge kommer du leva")
player_name = input("Tjenis, vad heter du? ")


print(f"Okay {player_name}, gissa var kulan finns i revlovern, gissa ett tal mellan 1 till 6")


def guessNr():

    for i in range(1, 6):
        counter = 0
        guess = int(input("Gissa vart kulan finns, du lever om du gissar fel: "))
        counter = counter + i
        if guess < number:
            print(f"Din gissning nr:{counter} på siffran {guess} är för lågt")
        if guess > number:
            print(f"Din gissning nr:{counter} på siffran {guess} är för högt")
        if guess == number or guess > 6:
            break
    if guess == number:
        print(
            f"DU ÄR DÖD!! Din gissning nr:{counter} på siffran {guess} är rätt efter {counter} försök")
    elif guess > 6:
        print(f"Din gissning nr:{counter} på siffran {guess} är ogiltig")
    else:
        # print('Dinna gissningar var fel, den rätta numret är:  ' + str(number))
        print(f"Dinna gissningar var fel, den rätta numret är: {str(number)} och du lever")


#guess = int(input("Gissa siffran: "))
guessNr()