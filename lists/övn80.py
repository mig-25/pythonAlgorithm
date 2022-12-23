""" OBS! För att köra denna uppgift, installera numpy
med följande kommando: pip install numpy
Mata in blodsockret för sju dagar,
om blodsockret är lägre än 5 så skriv ut "För lågt",
om blodsockret är över 10, så skriv ut "För högt",
annars skriv ut "Normalt"
Dessutom ska printen visa vilken dag mätning skedde


Efter alla inmatningar, skriv ut det högsta och lägsta värdet,
plus vilka dagar mätningen skedde.
Medel sockernivån ska också vissas för den perionden mätningen skedde,
Detta ska ske dynamisk och inte hårdkodas. 

Exempel:

Mata in antal gånger du ska mäta ditt blodsocker : 4
------------------------------------------------------------

Mata in blodsockret: 3.4


Mata in blodsockret: 6.7


Mata in blodsockret: 5.7


Mata in blodsockret: 12.3


Ditt blodsocker: 3.4 är för lågt!!! under dag 1

Ditt blodsocker: 6.7 är normalt under dag 2

Ditt blodsocker: 5.7 är normalt under dag 3

Ditt blodsocker: 12.3 är för högt!!! under dag 4

Blodsocker under alla dagar [(0, 3.4), (1, 6.7), (2, 5.7), (3, 12.3)]
Högsta sockernivån var 12.3 under dag 4
Lägsta sockernivån var 3.4 under dag 1
Medel sockernivån var 7.02 under 4 dagar
"""
from numpy import mean


def bloodSugar():
    sugarLevel = []

    occour = int(input("Mata in antal gånger du ska mäta ditt blodsocker : "))
    print("------------------------------------------------------------\n")

    for i in range(occour):
        value = float(input("Mata in blodsockret: "))
        print("\n")
        sugarLevel.append(value)

        day = enumerate(sugarLevel)

    for value in sugarLevel:
        index = sugarLevel.index(value)
        #day = enumerate(sugarLevel)
        if value < 5:
            print(
                f"Ditt blodsocker: {value} är för lågt!!! under dag {index+1}\n")
        elif value > 10:
            print(
                f"Ditt blodsocker: {value} är för högt!!! under dag {index+1}\n")
        else:
            print(f"Ditt blodsocker: {value} är normalt under dag {index+1}\n")

    avg = mean(sugarLevel)

    print(f"Blodsocker under alla dagar {list(day)}")

    print(
        f"Högsta sockernivån var {max(sugarLevel)} under dag {sugarLevel.index(max(sugarLevel)) + 1}")
    print(
        f"Lägsta sockernivån var {min(sugarLevel)} under dag {sugarLevel.index(min(sugarLevel)) + 1}")
    print(f"Medel sockernivån var {round(avg,2)} under {occour} dagar")


bloodSugar()
