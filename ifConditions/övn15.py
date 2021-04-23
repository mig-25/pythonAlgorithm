# Ange ett tal, och skriv ut om det är jämnt tal

def isEven(int1, int2):
    if int1 % int2 == 0:
        print("Jämt tal")
    else:
        print("Udda tal")


int1 = int(input("Mata in första talet: "))
int2 = int(input("Mata in andra talet: "))

isEven(int1, int2)
