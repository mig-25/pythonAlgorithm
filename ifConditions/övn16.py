''' En firma erbjuder 10 procents rabatt om
man vid ett köptillfälle handlar för mer än
1000kr.
Ange antal enheter och pris per enhet
 '''


def totalPrice(units, unitsPrice):
    totalSum = units * unitsPrice

    if totalSum > 1000:
        totalSum = (totalSum * 0.9)
        print(f"{totalSum} kr inkl 10% rabatt")
    else:
        print(f"{totalSum} kr, ingen rabatt")


units = int(input("Mata in enheter: "))
unitsPrice = int(input("Mata in per enhet: "))

totalPrice(units, unitsPrice)
