""" Beräkna ankomsttiden för ett tåg.
Ange följande:
    tidpunkt i timma och minut för avgången, tex 12: 41
    körtid i timma och minuter.
    Om minuter anges i 60 min eller mer, hantera det
    genom att lägga ett påslag på variabeln för timmar.
    Printa klockslaget för ankomsten. Om midnatt passeras ska det även stå
    "Nästa dag"
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
        print("Ankomst nästa dag")

    print(
        f"Med avgångstiden {depHour}:{depMin}, och en resetid på {travelHour}:{travelMin} så är ankomsten kl:{ArrHour}:{ArrMin}")


depHour = int(input("Mata avgångstimmen: "))
depMin = int(input("Mata avgångsminuten: "))
travelHour = int(input("Mata ankomsttimmen: "))
travelMin = int(input("Mata ankomstminuten: "))


trainTimeTabell(depHour, depMin, travelHour, travelMin)
