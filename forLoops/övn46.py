""" Läs in antal ggr som du kan skriva ut siffor på skärmen
Läs in siffran och skriv sedan ut de
Formatet ska vara följande om jag skrev in 4 för antal siffrar som ska
ska skrivas ut.
Antal siffran som ska printas ut måste vara dynamisk och inte vara hårdkodad
You choose to print out: 4 numbers
Your number was: 56
Your number was: 78
Your number was: 98
Your number was: 23
 """


def printLoop():
    count = int(input("Mata in antal itterationer för loopen: "))
    print(f"Du valde att utföra loopen {count} gånger")
    print("-------------------------------------------- \n")

    for x in range(count):
        x = int(input("Skriv in ett tal: "))
        print(f"Talet du skrev in var: {x}\n")


printLoop()
