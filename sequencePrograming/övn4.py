# Beräkna summan för ett serie av 3 tal, beräkna sedan deras medel
"""
Skapa en funktion som tar in tre tal,
låt användaren mata in tre tal
printa ut summa av de inlästa talen och printa medel 
av de tre inlästa talen, avrunda svaret till decimaler
Enbart en funktion med tre argument får användas
"""


def calcSumAvg(a, b, c):
    print(f"Inmatade tal är: {a}, {b}, {c}")
    sum = a+b+c
    avg = sum / 3
    return sum, avg


a = int(input("Mata in ett tal1: "))
b = int(input("Mata in ett tal2: "))
c = int(input("Mata in ett tal3: "))

sum, avg = calcSumAvg(a, b, c)
#average = round(avg, 2)
average = "{:.2f}".format(avg)

print(f"Summan är: {sum}, medel är: {average}")
