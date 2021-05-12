""" Beräkna lön, en man tjänar första dagen på sitt nya jobb 1 öre, andra dagen
2 öre, den tredje dagen 4öre osv.
Lönen fördubblas alltså för varje dag. Beräkna hur många dagar mannen
måste jobba för att tjäna en miljon kronor
 """


def calcSalary():
    antDag = 0
    totalLon = 0
    daglon = 0.01

    while totalLon <= 1000000:
        totalLon = totalLon + daglon
        daglon = daglon * 2
        antDag = antDag + 1
    print(f"Det tar {antDag} dagar att tjäna en miljon")


calcSalary()
