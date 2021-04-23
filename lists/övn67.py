""" En array innehåller personnr, med formatet YYMMDD-NNNN.
Kontrollera att födelsedatumet följ av en
streck innan de fyra sista siffrorna,
skriv ut ett fel meddelande annars.
Exempel:

Mata in ditt personr: 660125-0000
Ditt personnr 660125-0000 var i rätt format
 """


def socialSec():
    ssn = []

    ssn = input("Mata in ditt personr: ")
    #print(f"Personnumret du matade in var {ssn}")

    if ssn[6] != "-":
        print(f"ERROR, FEL FORMAT")
    else:
        print(f"Ditt personnr {ssn} var i rätt format")


socialSec()
