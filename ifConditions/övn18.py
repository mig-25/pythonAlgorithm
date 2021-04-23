''' Läs in värden av två tal, X och Y. 
Tilldela sedan variablen A värdet
2 om X är större än 5 + Y.
I annat fall så tilldelas variablen A värdet 5
 '''


def calcA(x, y):
    if x > 5 + y:
        print("a=2")
    else:
        print("a=5")


x = int(input("Mata in x: "))
y = int(input("Mata in y: "))

calcA(x, y)
