# Läs in ett tal och skriv ut om det är positivt eller negativt


def checkPosNeg(num):
    if num > 0:
        print("Positivt tal")
    else:
        print("Negativt tal")


num = int(input("Mata in en siffra: "))

checkPosNeg(num)
