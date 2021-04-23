""" Läs in prix exkl moms
Beräkna pris inkl moms om momsen är 25%
Om pris exkl moms är noll, gå ur programmet
 """


def priceVat(priceExvat):
    vat = 1.25
    while priceExvat != 0:
        priceIncVat = vat * priceExvat
        if priceExvat == 0:
            break
        print(f"Priset inkl moms är {priceIncVat}kr")
        priceExvat = float(input("Läs in pris ex moms: "))


priceExvat = float(input("Skrivet priset ex moms: "))

priceVat(priceExvat)
