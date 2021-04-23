# Ange tre tal, skriv ut det minsta talet


def checkBigNum(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print(f"Första talet {num1} är minst av {num2} och {num3}")
    elif num2 < num1 and num2 < num3:
        print(f"Andra talet {num2} är minst av {num1} och {num3}")
    else:
        print(f"Tredje talet {num3} är minst av {num1} och {num2}")


num1 = int(input("Mata in första talet: "))
num2 = int(input("Mata in andra talet: "))
num3 = int(input("Mata in tredje talet: "))

checkBigNum(num1, num2, num3)
