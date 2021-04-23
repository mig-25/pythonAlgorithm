""" 
Beräkna netto besinkostnad
Indata:
anal l 
pris per l
rabatt 

Skapa en funktion med argument för ovanstående,
läs in dem från användaren. Rabatten från läsaren måste 
anges som ett procenttal, tex för 5% rabatt ska användaren
skriva in enbart 5 och inte 0.05
Svara med slutpris, visa rabatten som användes i inläsningen.
"""


def fuelPrice(ppl, l, disc):
    fuelCost = ppl*l
    netFuelCost = fuelCost * (1-(disc/100))
    return netFuelCost


ppl = int(input("Pris per liter: "))
l = float(input("Antal liter: "))
disc = float(input("Rabatt: "))

netFuelCost = fuelPrice(ppl, l, disc)

print(f"Slutpris med {disc}% rabatt är {netFuelCost} kr")
