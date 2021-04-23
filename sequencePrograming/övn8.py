# Beräkna arean och omkretsen av en rektangel
# Skapa en en enda funktion för både omkrets och area

def rectangel(bas, höjd):
    area = bas*höjd
    omkrets = (2*bas)+(2*höjd)
    return area, omkrets


b = int(input("Mata in basen: "))
h = int(input("Mata in höjden: "))

area, omkrets = rectangel(b, h)

print(f"Arean är: {area} och omkrets är: {omkrets}")
