""" Läs in ett antal tal och skriv ut de, om 0 matas in avslutas programmet. """


def checkZero(num):
    while num != 0:
        num = int(input("Mata in en siffra: "))

        if num == 0:
            break
        print(f"Siffran var {num}")


num = int(input("Mata in en siffra: "))
print(f"Siffran var {num}")
checkZero(num)
