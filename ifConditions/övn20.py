""" Läs in ett tal, testa om talet är mellan 0 till 9, (OBS! båda vilkoren måste vara sanna) 
i så fall skriv ut kvadraten.
Annars generera en felmeddalnde """
 


def calcKvadrat(num):
    if 0 <= num & num <= 9:
        num *= num
        print(num)
    else:
        print(f"{num} är inte mellan 0 till 9")


num = int(input("Mata in ett tal mellan 0 till 9: "))

calcKvadrat(num)
