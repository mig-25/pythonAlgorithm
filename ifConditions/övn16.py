''' En firma erbjuder 10 procents rabatt om
man vid ett köptillfälle handlar för mer än
1000kr.
Ange antal enheter och pris per enhet
 '''

disc = 0.9
def totalPrice(units, unitsPrice):
    totalSum = units * unitsPrice

    if totalSum > 1000:
        totalSum = (totalSum * disc)
        print(f"{totalSum:.2f} kr inkl 10% rabatt")
    else:
        print(f"{totalSum:.2f} kr, ingen rabatt")


units = int(input("Mata in enheter: "))
unitsPrice = int(input("Mata in per enhet: "))

totalPrice(units, unitsPrice)
