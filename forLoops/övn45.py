""" Du har 1000kr på banken, om du läser in valfri ränta, vad får du på banken
efter 10 år.
Svaret ska avrundas uppåt till närmaste heltal.
Räntan ska visas dynamisk, dvs det du läser in, och inte 
vara hårdkodad.
Exempel med 5.1% Ränta
Importera och använd Math bibloteket i Python
Mata in räntan: 4.5
Räntan är 4.5%
_______________________________
Saldot för år 1 är 1045 kronor
Saldot för år 2 är 1093 kronor
Saldot för år 3 är 1142 kronor
Saldot för år 4 är 1193 kronor
Saldot för år 5 är 1247 kronor
Saldot för år 6 är 1303 kronor
Saldot för år 7 är 1361 kronor
Saldot för år 8 är 1423 kronor
Saldot för år 9 är 1487 kronor
Saldot för år 10 är 1553 kronor
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
