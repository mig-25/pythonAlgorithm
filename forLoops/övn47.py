""" En kommun gör följande prognos för befolkningsutvecklingen de närmaste åren:
         Vid början av 2020 hade kommunen 26000 invånare.
         Antal födda och avlidna uppskattas till 0.7 % respektive 0.6 % av
         befolkningen vid årets början
         Antal inflyttade och utflyttade uppskattas till 300 respektive 325 varje år
         Beräkna kommunens uppskattade invånarantal i början av ett visst år.
         Vilket år som ska vara slutår ska läsas in som indata
         Exempel utdata om startåret är 2020:
        At: 2021 the population is: 26305
        At: 2022 the population is: 26612
        At: 2023 the population is: 26920
        At: 2024 the population is: 27230
        At: 2025 the population is: 27541
 """

import math


def population(endYear):
    pop = 26000
    influx = 500
    emigrated = 325
    startYear = 2021

    for startYear in range(startYear, endYear+1):
        born = 0.01 * pop
        dead = 0.005 * pop
        pop = pop + (influx - emigrated) + (born - dead)
        print(f"Året: {startYear} var befolkningen {math.ceil(pop)}\n")


endYear = int(input("Mata in slutåret: "))
print("--------------------------------- \n")

population(endYear)
