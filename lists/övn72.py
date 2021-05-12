""" Läs in fem tal i en array, kontrollera hur många av talen är större än det
     första talet som lästes in .
    Om du i prompten fyller i 2 som första tal, och sedan 3, 4, 5, 6, 7
    så borde printen se ut på följande sätt:
    
    Inmatate talen större än 2 är [3, 4, 5, 6, 7]
 """


def largerThenFirst():
    numbers = []
    largestNr = []
    #number = []

    firstNr = int(input("Mata in första talet: "))
    numbers.append(firstNr)
    print("-----------------------------------\n")

    for i in range(0, 5):
        number = int(input("Mata in resten av talen: "))
        numbers.append(number)
        print(f"Du matade in {number}\n\n")

    for number in numbers:
        if number > firstNr:
            largestNr.append(number)

    print(f"Inmatate talen större än {firstNr} är {largestNr}")


largerThenFirst()
