""" Skapa en array av både positiva och negativa tal, skriv ut alla positiva och negativa tal.
Med följande värden i arrayn:
    -1, -2, -3, 5, 6, 1
    så borde printen se ut på följande sätt:

    Antal positiva tal är: [5, 6, 1]
    Antal negativa tal är: [-1, -2, -3]
 """


def posNeg():
    numbers = [-1, -2, -3, 5, 6, 1]
    pos = []
    neg = []

    for number in numbers:
        if number < 0:
            neg.append(number)
        else:
            pos.append(number)
    print(f"Antal positiva tal är: {pos}")
    print(f"Antal negativa tal är: {neg}")


posNeg()
