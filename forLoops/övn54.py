""" Skriv ut n(fakulteten), läs in n
Fakultet betecknas med ett utropstecken(!), fakultetstecken
Ex: 3 != 1*2*3
Ex: 5 != 1*2*3*4*5

Exempel om 5 matas in:

Mata in tal: 5
Fakulteten för 1 är 1
Fakulteten för 2 är 2
Fakulteten för 3 är 6
Fakulteten för 4 är 24
Fakulteten för 5 är 120
 """


def nFakultet(num):
    f = 1
    for i in range(1, num):
        f *= i
        print(f"Fakulteten för {i} är {f}")


num = int(input("Mata in tal: "))
num = num+1
nFakultet(num)
