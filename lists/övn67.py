""" En array innehåller personnr, med formatet YYMMDD-NNNN.
Kontrollera att födelsedatumet följs av en
streck innan de fyra sista siffrorna,
skriv ut ett fel meddelande annars. 
Med andra ord, strecket ska beffina sig på indexplats 6, indexstart är alltid 0
Exempel:

Mata in ditt personr: 660125-0000
Ditt personnr 660125-0000 var i rätt format
 """


def socialSec():
    ssn = []

    ssn = input("Mata in ditt personr i följande format YYMMDD-NNNN: ")
    #print(f"Personnumret du matade in var {ssn}")

    if ssn[6] != "-":
        print(f"ERROR, FEL FORMAT")
    else:
        print(f"Ditt personnr {ssn} var i rätt format")


socialSec()
