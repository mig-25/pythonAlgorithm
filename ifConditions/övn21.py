''' Läs in ett tal, testa om talet är mindre än - 10 eller större än 10, 
i så fall skriv ut "Talet är minst tvåsiffrigt,
annars skriv ut "Talet är inte tvåsiffrigt"
 '''


def testNum(num):
    if num <= -10 or num >= 10:
        print(f"Talet {num} är tvåsiffrigt")
    else:
        print(f"Talet {num} är inte tvåsiffrigt")


num = int(input("Mata in ett tvåsiffrigt tal: "))

testNum(num)
