""" Läs in ett tal, testa om talet är mellan 0 till 9, men inte 5.
Printa ut Rätt eller Fel
 """


def testNum(num):
    if num >= 0 and num <= 9 and num != 5:
        print("RÄTT!")
    else:
        print(
            "FEL!")


num = int(input("Mata in en siffra mellan noll till nio, men inte fem: "))

testNum(num)
