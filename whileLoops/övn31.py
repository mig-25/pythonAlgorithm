""" Läs in ett antal tal och skriv ut de, SÅ LÄNGE inte 0 matas in, mata in nya taL,
OM 0 matas in avslutas programmet. """


def checkZero(num):
    while num != 0:
        num = int(input("Mata in en siffra: "))

        if num == 0:
            print(f"Siffran var {num}")
            break
        

#Börja med ett startvärde innan ni anropar funktionen och går in i loppen
num = int(input("Mata in en siffra: "))
print(f"Siffran var {num}")
checkZero(num)
