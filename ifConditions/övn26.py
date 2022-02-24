""" Läs in två tal, printa om tal1 är större än tal2 eller om tal2 är större än tal1
Om talet är lika, skriv ut "Talen är lika"
 """


def checkBigNum(num1, num2):
    if num1 > num2:
        print(f"Nummer1: {num1} är större än nummer2: {num2}")
    elif num2 > num1:
        print(f"Nummer2: {num2} är större än nummer1: {num1}")
    else:
        print(f"Nummer1: {num1} och nummer2: {num2} är lika stora")


num1 = int(input("Mata in första talet: "))
num2 = int(input("Mata in andra talet: "))

checkBigNum(num1, num2)
