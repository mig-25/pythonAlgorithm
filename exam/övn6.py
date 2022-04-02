""" Mata in blodsockret för sju dagar,
om blodsockret är lägre än 5 så skriv ut "För lågt",
om blodsockret är över 10, så skriv ut "För högt",
annars skriv ut "Normalt"
Dessutom ska printen visa vilken dag mätning skedde


Efter alla inmatningar, skriv ut det högsta och lägsta värdet,
plus vilka dagar mätningen skedde.
Medel sockernivån ska också vissas för den perionden mätningen skedde,
Detta ska ske dynamisk och inte hårdkodas. 

För att åstkomma allt detta så behöver du använda dig av följande inbygga
metoder för listor:
.append för att lägga till värden i en lista
.index för att återge indexvärdet i en lista, använd denna metod för att lista
dagarna i mätningen, men indexet i en lista börjar på 0, så lägg till värdet 1
för att visa dagen för mätningen.
.sum för att addera alla värden i en lista, detta ska användas för att räkna ut
medel blodsockret, så tex avg = sum(sugarLevel) / occour där sugarLevel är er
lista och occour är variabeln för hur många dagar ni valde att mäta blodsockret.
.min och .max för att visa den mista och högsta värdet i en lista, andvända detta
vilken dag blodsockret var lägst och vilken dag den var högst.

Mata in antal gånger du ska mäta ditt blodsocker : 4
------------------------------------------------------------

Mata in blodsockret: 2.2


Mata in blodsockret: 5.5


Mata in blodsockret: 5.5


Mata in blodsockret: 12.5


Ditt blodsocker: 2.2 är för lågt!!! under dag 1

Ditt blodsocker: 5.5 är normalt under dag 2

Ditt blodsocker: 5.5 är normalt under dag 2

Ditt blodsocker: 12.5 är för högt!!! under dag 4

Högsta sockernivån var 12.5 under dag 4
Lägsta sockernivån var 2.2 under dag 1
Medel sockernivån var 6.42 under 4 dagar
"""


def bloodSugar():
    sugarLevel = []

    occour = int(input("Mata in antal gånger du ska mäta ditt blodsocker : "))
    print("------------------------------------------------------------\n")

    for i in range(occour):
        value = float(input("Mata in blodsockret: "))
        print("\n")
        sugarLevel.append(value)

    for value in sugarLevel:
        index = sugarLevel.index(value)
        if value < 5:
            print(
                f"Ditt blodsocker: {value} är för lågt!!! under dag {index+1}\n")
        elif value > 10:
            print(
                f"Ditt blodsocker: {value} är för högt!!! under dag {index+1}\n")
        else:
            print(f"Ditt blodsocker: {value} är normalt under dag {index+1}\n")

    avg = sum(sugarLevel) / occour

    print(
        f"Högsta sockernivån var {max(sugarLevel)} under dag {sugarLevel.index(max(sugarLevel)) + 1}")

    print(
        f"Lägsta sockernivån var {min(sugarLevel)} under dag {sugarLevel.index(min(sugarLevel)) + 1}")
    print(f"Medel sockernivån var {avg:.2f} under {occour} dagar")


bloodSugar()
