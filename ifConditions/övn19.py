''' En anställd som har timlön får, när arbetstiden överstiger 40 timmar per
vecka, övertidsbetalning för tiden utöver 40 timmar med en och halv timme
Läs in timlön och en veckas arbetstid.
Den totala veckolönen beräknas och skrivs ut

Exempel:
Mata in lön per timme: 1500
Mata in arbetstid i timmar: 45
Vecklönen är 71250.0kr med 1500 kr/timme och 45 timmars arbetstid och 5 övertidstimmar
 '''


def calcWeekSalary(salaryPerHour, workHours):

    if workHours > 40:
        OverTime = workHours - 40
        WeekSalary = 40 * salaryPerHour + 1.5 * salaryPerHour * OverTime
        print(
            f"Vecklönen är {WeekSalary}kr med {salaryPerHour} kr/timme och {workHours} timmars arbetstid och {OverTime} övertidstimmar")
    else:
        WeekSalary = workHours * salaryPerHour
        print(
            f"Vecklönen är {WeekSalary}kr med {salaryPerHour} kr/timme och {workHours} timmars arbetstid ")


salaryPerHour = int(input("Mata in lön per timme: "))
workHours = int(input("Mata in arbetstid i timmar: "))

calcWeekSalary(salaryPerHour, workHours)
