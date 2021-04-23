""" Läs in en array av 5 tal, skapa en ny array, och kopiera in värdet från den
gamla arrayn i den nya, och printa ut det i omvänd ordning
Om du matar in 1, 2, 3, 4, 5 så SKA printen vara i följande format:

Mata in tal: 1
Mata in tal: 2
Mata in tal: 3
Mata in tal: 4
Mata in tal: 5
Listan i omvänd ordning: [5, 4, 3, 2, 1]
 """


def listCopyReverse():
    list1 = []
    list2 = []

    for i in range(0, 5):
        number = int(input("Mata in tal: "))
        list1.append(number)

    list2 = list(list1)
    list2.reverse()
    print(f"Listan i omvänd ordning: {list2}")


listCopyReverse()
