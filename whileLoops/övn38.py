''' En bilägare har för ett antal tankningar  skrivit upp antal tankade liter
bensin och antal körda mil.
Läs in hur många liter som har tankats, samt antal körda mil för varje
tankningstillfälle.
Inmatningen ska avslutas med siffran 0.
Beräkna bensinförbrukningen per mil för varje tankning.
När data för samtliga tankningstillfällen är inlästa, ska genomslitlig
bensinförbrukning per mil skrivas ut.
OBS! Svaret för bensinförbrukningen och slutsvaret måste visas med enbart två decimaler

Exempel på utskrift:
Refuel occasion: 1
You filled: 79.6l, You drove: 130.2 miles
Consumtion is: 0.61 liter per miles
Refuel occasion: 2
You filled: 68.6l, You drove: 90.3 miles
Consumtion is: 0.76 liter per miles
Refuel occasion: 3
You filled: 89.6l, You drove: 98 miles
Consumtion is: 0.91 liter per miles
Average fuel consumtion is: 0.75 liter per miles
 '''

sumLiter = sumMiles = numLiter = numMiles = consumtion = literPerMiles = 0.00
counter = int(0)

numLiter = float(input("Mata in antal tankade liter bensin: "))

while numLiter != 0:
    sumLiter += numLiter
    numMiles = float(input("Mata in antal körda mil: "))

    sumMiles += numMiles
    consumtion = numLiter / numMiles
    counter += 1
    print(
        f"Tankningstillfället: {counter}.\n Du fyllde {numLiter} liter, och du körde {numMiles} mil.\n Bensinförbrukningen är {consumtion:.2f} l/m")

    numLiter = float(input("Mata in antal liter: "))

    if sumMiles != 0:
        literPerMiles = sumLiter / sumMiles


print(f"Medelförbrukningen var {literPerMiles:.2f} liter per mil")
