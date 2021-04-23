""" Skriv ut Summan av talen mellan 1 till 50

Svaret Måste vara i följande format:
    Omgång1 är summan: 1,
    Omgång2 är summan: 3,
    Omgång3 är summan: 6....och så vidare
 """


def calcSum():
    sum = 0
    for i in range(1, 51):
        sum = sum + i
        print(f"Omgång: {i} är summan {sum}")


calcSum()
