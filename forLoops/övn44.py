""" Beräkna och skriv ut kvadraten för talen 1 till 9
Resultatet ska skrivas i formen som "Kvadraten för 1 är: 1"
 """


def kvadrat():
    result = 0
    for x in range(1, 11):
        result = x*x
        print(f"Kvadraten av talet: {x} är {result}")
    # print(f"Kvadraten av talet: {x} är {result}")


kvadrat()
