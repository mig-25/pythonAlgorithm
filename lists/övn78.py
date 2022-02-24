""" Läs in två tal till en bråk, dvs täljare och nämnare, spara de i en array med två
platser.
Kontrollera om nämnaren är 0, skriv i så fall ut ett felmeddelande
Exempel:

Mata in täljaren: 4
Mata in nämnaren: 0
 FEL!!! Nämnare får inte vara 0
Täljaren är 4 och nämnare är 0

annars skriv ut svaret med två decimaler,
Exempel:
Mata in täljaren: 2
Mata in nämnaren: 3
Svaret är: 0.67
 """


def div():
    numbers = []

    for i in range(0, 1):
        number = int(input("Mata in täljaren: "))
        numbers.append(number)
        number = int(input("Mata in nämnaren: "))
        numbers.append(number)
        if numbers[1] == 0:
            print(f" FEL!!! Nämnare får inte vara 0")
        else:
            print(f"Svaret är: {numbers[0] / numbers[1]:.2f}")


div()
