""" Läs in 6 positiva tal, och bestäm vilket som är störst,
och vilket som är näst störst.
Exempel:

Input: 1

Mata in tal: 1
Du matade in talet: 1


Input: 2

Mata in tal: 2
Du matade in talet: 2


Input: 3

Mata in tal: 3
Du matade in talet: 3


Input: 4

Mata in tal: 44
Du matade in talet: 44


Input: 5

Mata in tal: 55
Du matade in talet: 55


Input: 6

Mata in tal: 6
Du matade in talet: 6


Största talet var: 55
Näst största talet var: 44
 """


def bigNextBig():

    big = -1
    nextBig = -1

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

    print(f"Största talet var: {big}")
    print(f"Näst största talet var: {nextBig}")


bigNextBig()
