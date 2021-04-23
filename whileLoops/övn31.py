""" Så länge användaren inte matar in siffran 0,
fortsätt att mata in nya siffror """


def checkZero(num):
    while num != 0:
        num = int(input("Mata in en siffra: "))

        if num == 0:
            break
        print(f"Siffran var {num}")


num = int(input("Mata in en siffra: "))
print(f"Siffran var {num}")
checkZero(num)
