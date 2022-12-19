""" 
Bestäm hur många tal du vill läsa in . Det största och minsta talet ska
skrivas ut.
Antal gånger du ska köra loopen måste printas dynamisk och inte vara hårdkodad.

Exempel:

Hur många gånger ska loopen köras: 4
Du valde att köra loopen: 4 gånger
-----------------------------------------------------

Mata in första talet: 45
Din första input var: 45
Mata in nästa tal: 
12
Input: 2
Din input var: 12

Mata in nästa tal: 
98
Input: 3
Din input var: 98

Mata in nästa tal: 
76
Input: 4
Din input var: 76

Största talet var: 98 och minsta talet var 12
 """


def minMax():
    counter = num = max = min = 0

    counter = int(input("Hur många gånger ska loopen köras: "))
    print(f"Du valde att köra loopen: {counter} gånger")
    print("-----------------------------------------------------\n")

    num = int(input("Mata in första talet: "))
    print(f"Din första input var: {num}")

    max = num
    min = num

    for i in range(2, counter+1):
        num = int(input("Mata in nästa tal: \n"))
        print(f"Input: {i}")

        print(f"Din input var: {num}\n")

        if num > max:
            max = num
        elif num < min:
            min = num

    print(f"Största talet var: {max} och minsta talet var {min}")


minMax()
