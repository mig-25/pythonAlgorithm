""" Ange radie för en cirkel,
beräkna diameter, omkrets och area
Enbart en funktion för användas,
Svaret ska vara med decimaler """

import constant

radie = 6


def cirkel():
    diameter = 2*radie
    omkrets = diameter*constant.PI
    area = radie*radie*constant.PI
    return diameter, omkrets, area


d = float(input("Mata in diametern: "))
o = float(input("Mata in omkretsen: "))
a = float(input("Mata in arean: "))

diameter, omkrets, area = cirkel()

print(
    f"Diametern är: {diameter:.2f}, omkretsen är: {omkrets:.2f} och arean är: {area:.2f}")
