""" Beräkna och skriv ut produkten för de ojämna talen från 1 till 15
Dvs, 1*3*5....*15
 """


def odd15():
    prod = 1
    for i in range(1, 16, 2):
        prod = prod + 1
        print(f"Produkten för omgång: {i} är {prod}")


odd15()
