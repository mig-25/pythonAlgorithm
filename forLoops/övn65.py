""" Läs in 6 positiva tal, och bestäm skillnaden mellan
den största och minsta talet
Exempel:

Input: 1

Mata in tal: 21
Du matade in talet: 21


Input: 2

Mata in tal: 4
Du matade in talet: 4


Input: 3

Mata in tal: 8
Du matade in talet: 8


Input: 4

Mata in tal: 45
Du matade in talet: 45


Input: 5

Mata in tal: 12
Du matade in talet: 12


Input: 6

Mata in tal: 2345
Du matade in talet: 2345


Skillnaden mellan den största talet 2345 och det näst största talet 45 är 2300
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
        f"Skillnaden mellan den största talet {big} och det näst största talet {nextBig} är {diff}")


bigDiff()
