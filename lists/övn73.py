""" Läs in en array av 5 tal, skriv ut indexet för det sista negativa talet i
     arrayn. Ett litet tips, om ni löser det med en for loop, börja loopen
     omvänd.
     Om du matar in följande siffror i prompten:
     45, -3, 5, 6, 7
    så SKA printen vara i följande format:
    
Mata in tal: 45


Mata in tal: -3


Mata in tal: 4


Mata in tal: 5


Mata in tal: -7


Det sista negativa talet var -3, på indexplatsen: 1
Det sista negativa talet var -7, på indexplatsen: 4
 """


def lastNegNr():
    numbers = []

    for i in range(0, 5):
        number = int(input("Mata in tal: "))
        print("\n")
        numbers.append(number)

    for number in numbers:
        if number < 0:
            index = numbers.index(number)
            print(
                f"Det sista negativa talet var {number}, på indexplatsen: {index}")


lastNegNr()
