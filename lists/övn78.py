""" Läs in två tal till en bråk, dvs täljare och nämnare, spara de i en array med två
platser.
Kontrollera om nämaren är 0, skriv i så fall ut ett felmeddelande
Exempel:

Mata in täljaren: 4
Mata in nämnaren: 0
 FEL!!! Nämnare får inte vara 0
Täljaren är 4 och nämnare är 0
 """


def div():
    numbers = []

    number = int(input("Mata in täljaren: "))
    numbers.append(number)

    for i in range(0, 1):
        number = int(input("Mata in nämnaren: "))
        numbers.append(number)
        if numbers[1] == 0:
            print(f" FEL!!! Nämnare får inte vara 0")

    print(f"Täljaren är {numbers[0]} och nämnare är {numbers[1]}")


div()
