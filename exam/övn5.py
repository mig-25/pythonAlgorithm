''' Skapa ett program för att beräkna summan och medel av tal du matar in
Antal tal i beräkningen läser du in från användaren i en variabel kallad avg

skapa en funktion kallad calcAvg,

sätt variabeln sum till 0

skapa en räknare, en variabel som heter counter och sätt dess värde till
detsamma som avg

använd while, med vilkoret, så länge variabeln counter är större än 0, 

låt användaren mata in heltal och spara det i variabeln num.

sum är då lika med sum + num

OBS! du måste nu subtrahera värdet i din räknar variabel counter med 1 för varje varv i while loopen,
annars kommer aldrig vilkoret i while loopen uppfyllas

printa ut summan och medel, inget av värden ska hårdkodas i printen utan,
hämtas från rätt variabel.

Kalla på funktionen calcAvg() 

Exempel:

Ange hur många tal som du ska beräkan summan och medel för: 5


Ange tal: 4
Ange tal: 5
Ange tal: 6
Ange tal: 7
Ange tal: 8


Summan är: 30 och medel är: 6.0

'''


avg = int(input("Ange hur många tal som du ska beräkan summan och medel för: "))


def calcAvg():
    print("\n")
    sum = 0
    counter = avg
    while counter > 0:
        num = int(input("Ange tal: "))
        sum = sum + num
        counter = counter-1

    print("\n")
    print(f"Summan är: {sum} och medel är: {sum/avg}")


calcAvg()
