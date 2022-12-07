""" Läs in ett tal, testa om talet är större än eller med 0
eller om talet är mindre eller lika med 9, men inte 5.
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
