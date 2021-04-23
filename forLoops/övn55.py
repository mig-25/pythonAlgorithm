""" Beräkna f(x) ^ n
x och n ska läsas in
Exempel om x läses in som 5, och n läses in som 7:

    Svaret på f(x) ^ n, om x är: 5 och n är 7, så är svaret 78125
 """


def calcXN(x, n):
    f = 1

    for i in range(1, n):
        f *= x

    print(
        f"Svaret på f(x)^n, om x är: {x} och n är: {n}, så är svaret {f} ")


x = int(input("Mata in värdet för x: "))
n = int(input("Mata in värdet för n: "))
n = n+1

calcXN(x, n)
