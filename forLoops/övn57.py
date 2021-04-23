""" Läs in 10 tal, skriv ut hur många ggr talet 7 läses in,
antal sjuor ska visas för varje itteration i loopen.
Exempel:

Input: 1

Mata in ett tal: 7
Talet du matade in var: 7

Du matade in talet 7, 1 gånger

Input: 2

Mata in ett tal: 34
Talet du matade in var: 34

Du matade in talet 7, 1 gånger

Input: 3

Mata in ett tal: 56
Talet du matade in var: 56

Du matade in talet 7, 1 gånger

Input: 4

Mata in ett tal: 7
Talet du matade in var: 7

Du matade in talet 7, 2 gånger

Input: 5

Mata in ett tal: 89
Talet du matade in var: 89

Du matade in talet 7, 2 gånger

Input: 6

Mata in ett tal: 54
Talet du matade in var: 54

Du matade in talet 7, 2 gånger

Input: 7

Mata in ett tal: 7
Talet du matade in var: 7

Du matade in talet 7, 3 gånger

Input: 8

Mata in ett tal: 6
Talet du matade in var: 6

Du matade in talet 7, 3 gånger

Input: 9

Mata in ett tal: 7
Talet du matade in var: 7

Du matade in talet 7, 4 gånger

Input: 10

Mata in ett tal: 54
Talet du matade in var: 54

Du matade in talet 7, 4 gånger
 """


def occour7():
    sevens = 0
    for i in range(1, 11):

        num = 0
        print(f"Input: {i}\n")

        num = int(input("Mata in ett tal: "))
        print(f"Talet du matade in var: {num}\n")

        if num == 7:
            sevens = sevens + 1

        print(f"Du matade in talet 7, {sevens} gånger\n")


occour7()
