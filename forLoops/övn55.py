""" Beräkna f(x) ^ n
x och n ska läsas in
Exempel om x läses in som 5, och n läses in som 7:

    Svaret på f(x) ^ n, om x är: 5 och n är 7, så är svaret 78125
 """


def calcXN(x, n):
    f = 1

    for i in range(n):#om loopen börjar med 0, alltså default värdet så behöver inte n vara n+1
        f *= x

    print(
        f"Svaret på f(x)^n, så är svaret {f} ")


x = int(input("Mata in värdet för x: "))
n = int(input("Mata in värdet för n: "))


calcXN(x, n)
