""" Så länge användaren inte matar in tecknet *,
fortsätt att mata in nya tecken """


def checkChar(char):
    while char != "*":
        char = input("Mata in ett tecken: ")

        if char == "*":
            break
        print(f"Tecknet var {char}")


char = input("Mata in en tecken: ")
print(f"Tecknet var {char}")
checkChar(char)
