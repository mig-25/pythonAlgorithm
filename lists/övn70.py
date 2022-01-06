""" Skapa en array på 11 tal, Addera 2 till talen som befinner sig på indexplats
     0, 2, 4, 6, 8, 10.
     Du kan hårdkoda in följande array i funktionen.
    2, 3, 5, 8, 10, 45, 1028, 1, 100000, 33, 2

    Utprinten ska ha följande format, om du skapar en array med ovan data:
    
Index 0 har nu ett värde av: 4

Index 2 har nu ett värde av: 7

Index 4 har nu ett värde av: 12

Index 6 har nu ett värde av: 1030

Index 8 har nu ett värde av: 100002

Index 10 har nu ett värde av: 4
 """


def addTwo():
    num = [2, 3, 5, 8, 10, 45, 1028, 1, 100000, 33, 2]

    #for loops starts from to 12, but not including 12 and has an increment of 2
    for i in range(0, 12, 2):
        num[i] = num[i]+2
        print(f"Index {i} har nu ett värde av: {num[i]}\n")


addTwo()
