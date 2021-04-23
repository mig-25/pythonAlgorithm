# Ange ett tal, och skriv ut om det är jämnt tal

def isEven(int):
    if int % 2 == 0:
        print("Jämt tal")
    else:
        print("Udda tal")


int = int(input("Mata in första talet: "))

isEven(int)
