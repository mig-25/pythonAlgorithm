""" Beräkna och skriv ut kvadraten för talen 1 till 9
Resultet ska skrivas i formen som "Kvadraten för 1 är: 1"
 """


def kvadrat():
    result = 0
    for x in range(1, 10):
        result = x*x
        print(f"Kvadraten av talet: {x} är {result}")


kvadrat()
