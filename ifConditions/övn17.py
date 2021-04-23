''' Ange två tal, dividera det första talet med det andra talet,
Om det andra talet(nämnaren) är 0, printa fel meddelande,
annars ska kvoten skrivas ut
 '''


def zeroDiv(numerator, denominator):
    if denominator == 0:
        print("Får ej divideras med 0")
    else:
        result = numerator / denominator
        print(f"{numerator} / med {denominator} = {result}")


numerator = int(input("Mata in täljare: "))
denominator = int(input("Mata in nämnare: "))

zeroDiv(numerator, denominator)
