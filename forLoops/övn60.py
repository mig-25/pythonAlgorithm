""" 
Läs in 10 heltal, skriv ut summan av de tal som är större än det allra
första talet som läses in, samt summan av alla som är mindre än det
allra första talet som läses in
Utskriften bör se ut på följande sätt om 50 var första talet:
Resultatet ska visas utanför loopen.

Mata in första numret att jämföra med: 50
-----------------------------------------------------

Input: 1

Mata in ett tal: 1
Talet du matade in var: 1

Input: 2

Mata in ett tal: 2
Talet du matade in var: 2

Input: 3

Mata in ett tal: 3
Talet du matade in var: 3

Input: 4

Mata in ett tal: 4
Talet du matade in var: 4

Input: 5

Mata in ett tal: 5
Talet du matade in var: 5

Input: 6

Mata in ett tal: 55
Talet du matade in var: 55

Input: 7

Mata in ett tal: 55
Talet du matade in var: 55

Input: 8

Mata in ett tal: 55
Talet du matade in var: 55

Input: 9

Mata in ett tal: 55
Talet du matade in var: 55

Input: 10

Mata in ett tal: 55
Talet du matade in var: 55

Summan av alla tal är större än: 50 är 275

Summan av alla tal är större än: 50 är 15
 """


def compareToFirst():
    firstNr = 0
    biggestNr = 0
    smallestNr = 0
    num = 0

    firstNr = int(input("Mata in första numret att jämföra med: "))
    print("-----------------------------------------------------\n")

    for i in range(1, 11):

        num = 0
        print(f"Input: {i}\n")

        num = int(input("Mata in ett tal: "))
        print(f"Talet du matade in var: {num}\n")

        if num > firstNr:
            biggestNr += num
        elif num < firstNr:
            smallestNr += num

    print(f"Summan av alla tal är större än: {firstNr} är {biggestNr}\n")
    print(f"Summan av alla tal är mindre än: {firstNr} är {smallestNr}")


compareToFirst()
