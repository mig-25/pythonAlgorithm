""" Läs in två tal, och skriv ut det största talet, följt av orden "är störst"
Om talet är lika, skriv ut "Talen är lika"
 """


def checkBigNum(num1, num2):
    if num1 > num2:
        print(f"{num1} är större än {num2}")
    elif num2 > num1:
        print(f"{num2} är större än {num1}")
    else:
        print(f"{num1} och {num2} är lika stora")


num1 = int(input("Mata in första talet: "))
num2 = int(input("Mata in andra talet: "))

checkBigNum(num1, num2)
