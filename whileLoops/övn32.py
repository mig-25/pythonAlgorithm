""" Läs in ett antal tecken, skriva ut dessa tecken. Programmet ska avslutas när tecknet * matas in. """


def checkChar(char):
    while char != "*":
        char = input("Mata in ett tecken: ")

        if char == "*":
            print(f"Tecknet var {char}")
            break
        


char = input("Mata in en tecken: ")
print(f"Tecknet var {char}")
checkChar(char)
