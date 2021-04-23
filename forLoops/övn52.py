""" Läs in och bestämma hur många tal du vill summera.
Tex om du skriver in 5, så Måste printen se ut på följande vis:

    Omgång 1 är summan 5
    Omgång 2 är summan 10
    Omgång 3 är summan 15
    Omgång 4 är summan 20
    Omgång 5 är summan 25
 """


def calcSum(count):
    sum = 0

    for i in range(0, count):
        sum = sum + count
        print(f"Omgång: {i+1} är summan {sum}")


count = int(input("Mata in antal gånger du vill summera: "))

calcSum(count)
