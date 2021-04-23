""" Skriv ut n(fakulteten), läs in n
Fakultet betecknas med ett utropstecken(!), fakultetstecken
Ex: 3 != 1*2*3
Ex: 5 != 1*2*3*4*5
 """


def nFakultet(num):
    f = 1
    for i in range(1, num):
        f *= i
        print(f"Fakulteten för {i} är {f}")


num = int(input("Mata in tal: "))
num = num+1
nFakultet(num)
