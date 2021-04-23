""" Undersök hur många termer som behövs för att summan ska bli större än
100000. Termen ska läsas in
Om den inlästa termen är 7 ska beräkningen vara 7+7+7+....7 = 100000
Utdata är 14286
 """


def Operator(term):
    sum = 0
    count = 0
    while sum <= 100000:
        sum = sum + term
        count = count + 1
    print(f"Utdata är {count}")


term = int(input("Läs in termen: "))

Operator(term)
