""" 
Bestäm hur många tal du vill läsa in . Det största och minsta talet ska
skrivas ut.
Antal gånger du ska köra loopen måste printas dynamisk och inte vara hårdkodad.

Exempel:

Hur många gånger ska loopen köras: 4
Du valde att köra loopen: 4
-----------------------------------------------------

Mata in första talet: 56
Din första input var: 56
Mata in nästa tal: 
34
Input: 2
Din input var: 34

Mata in nästa tal: 
78
Input: 3
Din input var: 78

Mata in nästa tal: 
-987
Input: 4
Din input var: -987

Största talet var: 78 och minsta talet var -987
 """


def minMax():
    counter = num = max = min = 0

    counter = int(input("Hur många gånger ska loopen köras: "))
    print(f"Du valde att köra loopen: {counter}")
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
