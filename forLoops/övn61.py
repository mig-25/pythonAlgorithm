""" 
Läs in 10 decimaltal, skriv ut den största av de inlästa talen, svaret ska
anges med 2 decimaler. Talordningen ska utryckas dynamisk, förutom för det
första talet som läses in.
Resultatet ska visas utanför loopen.

Exempel på utskrift:

Mata in första numret att jämföra med: 1.1
Input 1 är: 1.1
-----------------------------------------------------

Input: 2

Mata in ett tal: 1.2
Input: 2

Du matade in: 1.2

Input: 3

Mata in ett tal: 33.4
Input: 3

Du matade in: 33.4

Input: 4

Mata in ett tal: 4
Input: 4

Du matade in: 4.0

Input: 5

Mata in ett tal: 5678.23
Input: 5

Du matade in: 5678.23

Input: 6

Mata in ett tal: 11.2
Input: 6

Du matade in: 11.2

Input: 7

Mata in ett tal: 56.7
Input: 7

Du matade in: 56.7

Input: 8

Mata in ett tal: 2.4
Input: 8

Du matade in: 2.4

Input: 9

Mata in ett tal: 6.8
Input: 9

Du matade in: 6.8

Input: 10

Mata in ett tal: 4.6
Input: 10

Du matade in: 4.6

Största talet var: 5678.23
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
