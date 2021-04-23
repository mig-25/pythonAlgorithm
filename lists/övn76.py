""" Läs in en array av 5 tal, skriv ut summan av alla positiva och negativa tal för sig
Om du matar in 4, -56, 67, -32, 89 så SKA printen vara i följande format:

Mata in tal: 4
Mata in tal: -56
Mata in tal: 67
Mata in tal: -32
Mata in tal: 89
Summan av alla positiva tal är 160
Summan av alla negativa tal är -88
 """


def sumPosNeg():
    numbers = []
    pos = 0
    neg = 0

    for i in range(0, 5):
        number = int(input("Mata in tal: "))
        numbers.append(number)

    for number in numbers:
        if number > 0:
            pos += number
        elif number < 0:
            neg += number

    print(f"Summan av alla positiva tal är {pos}")
    print(f"Summan av alla negativa tal är {neg}")


sumPosNeg()
