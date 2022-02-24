""" Beräkna ankomsttiden för ett tåg.
Ange följande:
    klockslag i timme och minut för avgången, 
    resetid i timmar och minuter.
    Om ankomsttiden i minuter blir 60 eller mer, hantera det
    genom att lägga ett påslag på variabeln för timmar.
    Om ankomsttimmen blir mer än kl 24, och midnatt passeras ska det även stå
    "Nästa dag"
    Printa sedan klockslaget för ankomsten. "
 """
ArrHour = 0
ArrMin = 0


def trainTimeTabell(depHour, depMin, travelHour, travelMin):
    ArrHour = depHour + travelHour
    ArrMin = depMin + travelMin

    if ArrMin >= 60:
        ArrMin = ArrMin - 60
        ArrHour = ArrHour + 1

    if ArrHour >= 24:
        ArrHour = ArrHour - 24
        print("\nAnkomst nästa dag")

    print(
        f"Med avgångstiden {depHour}:{depMin}, och en resetid på {travelHour}:{travelMin} så är ankomsten kl:{ArrHour}:{ArrMin}")


depHour = int(input("Mata avgångstimmen: "))
depMin = int(input("Mata avgångsminuten: "))
travelHour = int(input("Mata resetid i timmar: "))
travelMin = int(input("Mata resetid i minuter: "))


trainTimeTabell(depHour, depMin, travelHour, travelMin)
