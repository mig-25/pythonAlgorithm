""" Läs in en array av 5 tal, skriv ut indexet för alla negativa tal i arrayn. 
     Använd metoden index() vilket returnerar positionen vid den första förekomsten av det angivna värdet.
     Om du matar in följande siffror i prompten:
     67, -2, 89, -234, 7
    så SKA printen vara i följande format:
    
Mata in tal: 67


Mata in tal: -2


Mata in tal: 89


Mata in tal: -234


Mata in tal: 7


Det sista negativa talet var -2, på indexplatsen: 1
Det sista negativa talet var -234, på indexplatsen: 3
 """


def lastNegNr():
    numbers = []

    for i in range(0, 5):
        number = int(input("Mata in tal: "))
        print("\n")
        numbers.append(number)

    for number in numbers:
        if number < 0:
            # Använd metoden index() vilket returnerar positionen vid den första förekomsten av det angivna värdet.
            index = numbers.index(number)
            print(
                f"Det sista negativa talet var {number}, på indexplatsen: {index}")


lastNegNr()
