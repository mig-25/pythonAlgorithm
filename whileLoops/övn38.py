''' En bilägare har för ett antal tankningar skrivit upp antal tankade liter
bensin och antal körda mil.
Läs in hur många liter som har tankats, samt antal körda mil för varje
tankningstillfälle.
Inmatningen ska avslutas med siffran 0.
Beräkna bensinförbrukningen per mil för varje tankning.
När data för samtliga tankningstillfällen är inlästa, ska genomslitlig
bensinförbrukning per mil skrivas ut.
OBS! Svaret för bensinförbrukningen och slutsvaret måste visas med enbart två decimaler

Exempel på utskrift:

Mata in antal tankade liter bensin: 78
Mata in antal körda mil: 56

 Tankningstillfället: 1.
 Du fyllde 78.0 liter, och du körde 56.0 mil.
 Bensinförbrukningen är 1.39 l/m 

Mata in antal liter: 56
Mata in antal körda mil: 45

 Tankningstillfället: 2.
 Du fyllde 56.0 liter, och du körde 45.0 mil.
 Bensinförbrukningen är 1.24 l/m 

Mata in antal liter: 89
Mata in antal körda mil: 67

 Tankningstillfället: 3.
 Du fyllde 89.0 liter, och du körde 67.0 mil.
 Bensinförbrukningen är 1.33 l/m 

Mata in antal liter: 0

 Medelförbrukningen var 1.33 liter per mil
 '''


def fuelConsumtion():

    sumLiter = sumMiles = numLiter = numMiles = consumtion = literPerMiles = 0.00
    #counter = int(0)
    counter = 0

    numLiter = float(input("Mata in antal tankade liter bensin: "))

    while numLiter != 0:
        sumLiter += numLiter
        numMiles = float(input("Mata in antal körda mil: "))

        sumMiles += numMiles
        consumtion = numLiter / numMiles
        counter += 1
        print(
            f"\n Tankningstillfället: {counter}.\n Du fyllde {numLiter} liter, och du körde {numMiles} mil.\n Bensinförbrukningen är {consumtion:.2f} l/m \n")

        numLiter = float(input("Mata in antal liter: "))

        if sumMiles != 0:
            literPerMiles = sumLiter / sumMiles

    print(f"\n Medelförbrukningen var {literPerMiles:.2f} liter per mil")


fuelConsumtion()
