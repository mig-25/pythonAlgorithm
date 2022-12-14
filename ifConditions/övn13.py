# Ange ett tal, och skriv ut om det är jämnt tal

def isEven(int):
    if int % 2 == 0:
        print("Jämt tal")
    else:
        print("udda tal")


int = int(input("Mata in ett tal: "))


isEven(int)
