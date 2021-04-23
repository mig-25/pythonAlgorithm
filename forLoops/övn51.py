""" Skriv ut Summan av de jämna heltalen mellan 2 till 30
    
Svaret Måste vara i följande format:
     
Omgång: 1 är summan 2
Omgång: 3 är summan 6
Omgång: 5 är summan 12
Omgång: 7 är summan 20
Omgång: 9 är summan 30
    ...och så vidare
 """


def calcSum():
    sum = 0
    for i in range(2, 31, 2):
        sum = sum + i
        i = i-1
        print(f"Omgång: {i} är summan {sum}")


calcSum()
