#Skapa en funktion, Ange ett tal, detta talet ska sedan dubbleras, vidare ska ingångstalet ökas med 1 för varje varv i loopen, 
# detta ska sedan upprepas 10 ggr
def multi(num):
    
    result = 0
    for x in range(1, 11):
        result = num*2
        print(f"Omgång: {x} är num {num}, och {num} * 2 blir {result}")
        num=num+1


num = int(input("Mata in tal: "))
multi(num)

""" result = 0
num = int(input("Mata in tal: "))
for x in range(1,11):
    result = num * 2
    print(f"Omgång: {x} är svaret {result}")
    num=num+1 """

