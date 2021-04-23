""" Läs in en array av 5 tal, beräkna summan och medel av de inlästa talen
Om du matar in 4, 5, 4, 5, 4 så SKA printen vara i följande format:

Mata in tal: 4
Mata in tal: 5
Mata in tal: 4
Mata in tal: 5
Mata in tal: 4
Summan av alla talen är 22
Medel av alla talen är 4.4
 """


def sumAvgArray():
    numbers = []
    sum = 0
    avg = 0

    for i in range(0, 5):
        number = int(input("Mata in tal: "))
        numbers.append(number)

    for number in numbers:
        index = numbers.index(number)
        sum += numbers[index]
        avg = sum/5
    print(f"Summan av alla talen är {sum}")
    print(f"Medel av alla talen är {avg}")


sumAvgArray()
