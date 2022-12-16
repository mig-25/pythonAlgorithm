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
            f"Med en timlön på: {salaryPerHour} per timme\n och en arbetstid på {workHours} timmar\n och med en övertid på {OverTime} timmar\n så är slutlönen {WeekSalary} kr")
    else:
        WeekSalary = workHours * salaryPerHour
        print(
            f"Med en timlön på {salaryPerHour} per timme\n och en arbetstid på {workHours} timmar\n så är slutlönen {WeekSalary} kr")


salaryPerHour = int(input("Mata in lön per timme: "))
workHours = int(input("Mata in arbetstid i timmar: "))

calcWeekSalary(salaryPerHour, workHours)
