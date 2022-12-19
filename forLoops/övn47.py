""" En kommun gör följande prognos för befolkningsutvecklingen de närmaste åren:
         Vid början av 2022 hade kommunen 26000 invånare.
         Antal födda och avlidna uppskattas till 7% respektive 6% av
         befolkningen vid årets början
         Antal inflyttade och utflyttade uppskattas till 300 respektive 325 varje år
         Beräkna kommunens uppskattade invånarantal i början av ett visst år.
         Vilket år som ska vara slutår ska läsas in som indata
         Exempel utdata om startåret är 2022 och slutåret 2025:
        
Mata in slutåret: 2025
--------------------------------- 

Året: 2023 var befolkningen 26235

Året: 2024 var befolkningen 26473

Året: 2025 var befolkningen 26713
 """

import math


def population(endYear):
    pop = 26000
    influx = 300
    emigrated = 325
    startYear = 2022

    for startYear in range(startYear, endYear):
        born = 0.07 * pop
        dead = 0.06 * pop
        pop = pop + (influx - emigrated) + (born - dead)
        print(f"Året: {startYear+1} var befolkningen {math.ceil(pop)}\n")


endYear = int(input("Mata in slutåret: "))
print("--------------------------------- \n")

population(endYear)
