""" Läs in kropptempraturen, skriv "VARNING!!"" om temp är mindre än 35, och
om temp överstiger 42
 """


def checkTemp(temp):
    if temp < 35 or temp > 42:
        print("WARNING!!!")
    else:
        print("Normal")


temp = int(input("Mata in en tempratur: "))

checkTemp(temp)
