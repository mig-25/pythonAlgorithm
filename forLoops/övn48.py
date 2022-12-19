""" Beräkna och skriv ut svaret för följande algoritm:
     f(x) = 3x ^ 3 - 5x ^ 2 + 2x - 20
     Använd Math.pow() metoden för att göra upphöjt till beräkningar
     Värdet på x är mellan heltalen - 10 till 10
    Svaret Måste ha följande format:

Värdet på f är -29540.0 om x är -10
Värdet på f är -21746.0 om x är -9
Värdet på f är -15460.0 om x är -8
Värdet på f är -10520.0 om x är -7
Värdet på f är -6764.0 om x är -6
Värdet på f är -4030.0 om x är -5
Värdet på f är -2156.0 om x är -4
Värdet på f är -980.0 om x är -3
Värdet på f är -340.0 om x är -2
Värdet på f är -74.0 om x är -1
Värdet på f är -20.0 om x är 0
Värdet på f är -16.0 om x är 1
Värdet på f är 100.0 om x är 2
Värdet på f är 490.0 om x är 3
Värdet på f är 1316.0 om x är 4
Värdet på f är 2740.0 om x är 5
Värdet på f är 4924.0 om x är 6
Värdet på f är 8030.0 om x är 7
Värdet på f är 12220.0 om x är 8
Värdet på f är 17656.0 om x är 9
Värdet på f är 24500.0 om x är 10

 """

import math


def calcF():
    for x in range(-10, 11):
        f = math.pow(3*x, 3) - math.pow(5*x, 2) + 2 * x - 20
        print(f"Värdet på f är {f} om x är {x}")


calcF()
