""" Beräkna och skriv ut produkten för de ojämna talen från 1 till 15
Dvs, 1*3*5....*15

Exempel:
Produkten för omgång: 1 är 2
Produkten för omgång: 3 är 3
Produkten för omgång: 5 är 4
Produkten för omgång: 7 är 5
Produkten för omgång: 9 är 6
Produkten för omgång: 11 är 7
Produkten för omgång: 13 är 8
Produkten för omgång: 15 är 9
 """


def odd15():
    prod = 1
    for räknare in range(1, 16, 2):
        prod = prod + 1
        print(f"Produkten för omgång: {räknare} är {prod}")


odd15()
