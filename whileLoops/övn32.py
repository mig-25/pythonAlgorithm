""" Läs in ett antal tecken, skriva ut dessa tecken. Programmet ska avslutas när tecknet * matas in. """


def checkChar(char):
    while char != "*":
        char = input("Mata in ett tecken: ")

        if char == "*":
            break
        print(f"Tecknet var {char}")


char = input("Mata in en tecken: ")
print(f"Tecknet var {char}")
checkChar(char)
