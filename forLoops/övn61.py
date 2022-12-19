""" 
Läs in 10 decimaltal, skriv ut den största av de inlästa talen, svaret ska
anges med 2 decimaler. Talordningen ska utryckas dynamisk, förutom för det
första talet som läses in.
Resultatet ska visas utanför loopen.

Input 1 är: 45.78
-----------------------------------------------------

Input: 2

Mata in ett tal: -34.12
Du matade in: -34.12

Input: 3

Mata in ett tal: -4.67
Du matade in: -4.67

Input: 4

Mata in ett tal: 34567.89
Du matade in: 34567.89

Input: 5

Mata in ett tal: 23.7
Du matade in: 23.7

Input: 6

Mata in ett tal: 1.2
Du matade in: 1.2

Input: 7

Mata in ett tal: 89.3
Du matade in: 89.3

Input: 8

Mata in ett tal: 78.3
Du matade in: 78.3

Input: 9

Mata in ett tal: 123.5
Du matade in: 123.5

Input: 10

Mata in ett tal: 88.3
Du matade in: 88.3

Största talet var: 34567.89
 """


def compareToFirst():
    largestNr = float(0.0)
    num = float(0.0)

    num = float(input("Mata in första numret att jämföra med: "))
    largestNr = num
    print(f"Input 1 är: {num}")
    print("-----------------------------------------------------\n")

    for i in range(2, 11):

        num = float(0.0)
        print(f"Input: {i}\n")

        num = float(input("Mata in ett tal: "))
        #print(f"Input: {i}\n")
        print(f"Du matade in: {num}\n")

        if num > largestNr:
            largestNr = num

    print(f"Största talet var: {largestNr}")


compareToFirst()
