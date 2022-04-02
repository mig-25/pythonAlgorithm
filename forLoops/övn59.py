""" Läs in 10 tal, antal av alla
positiva OCH negativa tal som läses in,
Resultatet ska visas utanför loopen.
Exempel:

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

Mata in ett tal: -1
Talet du matade in var: -1

Input: 7

Mata in ett tal: -2
Talet du matade in var: -2

Input: 8

Mata in ett tal: -3
Talet du matade in var: -3

Input: 9

Mata in ett tal: -4
Talet du matade in var: -4

Input: 10

Mata in ett tal: -5
Talet du matade in var: -5

Summan av alla positiva tal är: 5

Summan av alla negativa tal är: 5
 """


def posNumNeg():
    pos = 0
    neg = 0

    for i in range(1, 11):

        num = 0
        print(f"Input: {i}\n")

        num = int(input("Mata in ett tal: "))
        print(f"Talet du matade in var: {num}\n")

        if num > 0:
            pos += 1
        else:
            neg += 1

    print(f"Summan av alla positiva tal är: {pos}\n")
    print(f"Summan av alla negativa tal är: {neg}")


posNumNeg()
