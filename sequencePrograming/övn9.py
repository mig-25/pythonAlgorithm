""" Ange radie för en cirkel,
beräkna diameter, omkrets och area
Enbart en funktion för användas, använd en konstant för Pi
Svaret ska vara med två decimaler """

import constant

def cirkel(radie):
    diameter = 2*radie
    omkrets = diameter*constant.PI
    area = radie*radie*constant.PI
    return diameter, omkrets, area


r = float(input("Mata in radien: "))
diameter, omkrets, area = cirkel(r)

print(
    f"Diametern är: {diameter:.2f}, omkretsen är: {omkrets:.2f} och arean är: {area:.2f}")
