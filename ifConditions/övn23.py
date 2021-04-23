""" Läs in ett tal, testa om talet är jämt delbart med 3, men inte med 30,
I så fall divideras talet med 3
 """


def testNum(num):
    if num % 3 == 0 and num % 30 != 0:
        kvot = num / 3
        print(f"{num} / 3 = {kvot}")
    else:
        print("ERROR!")


num = int(input("Mata in en siffra: "))

testNum(num)
