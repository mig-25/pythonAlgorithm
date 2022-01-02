""" Du har 1000kr på banken, om du läser in valfri ränta, vad får du på banken
efter 10 år.
Svaret ska avrundas uppåt till närmaste heltal.
Räntan ska visas dynamisk, dvs det du läser in, och inte 
vara hårdkodad.
Exempel med 5.1% Ränta
Importera och använd Math bibloteket i Python
You choose 5.1 % interest
_______________________________
Annual Account Balance for Year 1 = 1051
Annual Account Balance for Year 2 = 1105
Annual Account Balance for Year 3 = 1161
Annual Account Balance for Year 4 = 1221
Annual Account Balance for Year 5 = 1283
Annual Account Balance for Year 6 = 1348
Annual Account Balance for Year 7 = 1417
Annual Account Balance for Year 8 = 1489
Annual Account Balance for Year 9 = 1565
Annual Account Balance for Year 10 = 1645
 """

import math


def balance(intrest):
    invest = 1000
    print(f"Räntan är {intrest}%")
    print(f"_______________________________")

    amount = 0
    amount = invest

    for x in range(1, 11):
        amount *= (1 + intrest / 100)
        print(f"Saldot för år {x} är {math.ceil(amount)} kronor")


intrest = float(input("Mata in räntan: "))

balance(intrest)
