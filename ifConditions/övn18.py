''' Läs in värden av två tal, X och Y.  
om X är större än 5 + Y.
Så printa att a = 2
I annat fall Så printa att a = 5
 '''


def calcA(x, y):
    if x > (5 + y):
        print("a=2")
    else:
        print("a=5")


x = int(input("Mata in x: "))
y = int(input("Mata in y: "))

calcA(x, y)
