""" Läs in en array av 5 tal, skriv ut det största och minsta talet
Talens index ska skrivas ut dynamisk, och inte vara hårdkodad
Använd dig av metoden min och max för att ta redan på minsta och störta talet i arrayn
Om du matar in 45, -2, 5678, -234, 6 så SKA printen vara i följande format:

Mata in värdet för index 1  : 45
Mata in värdet för index 2  : -2
Mata in värdet för index 3  : 5678
Mata in värdet för index 4  : -234
Mata in värdet för index 5  : 6
Det minsta talet är -234
Det minsta talet är 5678
 """


def minMaxNr():
    numList = []
    for i in range(1, 6):
        value = int(input("Mata in värdet för index %i : " % i))
        numList.append(value)

    print(f"Det minsta talet är {min(numList)}")
    print(f"Det minsta talet är {max(numList)}")


minMaxNr()
