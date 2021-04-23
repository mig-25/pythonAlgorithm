""" Läs in 6 positiva tal, och bestäm skillnaden mellan
den största och minsta talet
Exempel:
 """


def bigDiff():
    big = -1
    nextBig = -1
    diff = 0

    for i in range(1, 7):
        num = 0

        print(f"Input: {i}\n")

        num = int(input("Mata in tal: "))
        print(f"Du matade in talet: {num}\n\n")

        if num > big:
            nextBig = big
            big = num
        elif num > nextBig:
            nextBig = num

        diff = big - nextBig

    print(
        f"Skillnaden mellan den största talet {big} och det näststörsta talet {nextBig} är {diff}")


bigDiff()
