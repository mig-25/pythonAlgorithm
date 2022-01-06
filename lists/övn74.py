""" Läs in en array av 5 tal, beräkna summan och medel av de inlästa talen
OBS! metoden index retunerar den första förekomsten av ett värde, 
df blir index 0 vid tal 4 varje gång talet 4 matas in

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
        #OBS! metoden index retunerar den första förekomsten av ett värde, df blir index 0 vid tal 4 varje gång talet 4 matas in
        indexNr = numbers.index(number) 
        sum += numbers[indexNr]        
        avg = sum/5
    print(f"Summan av alla talen är {sum}")
    print(f"Medel av alla talen är {avg}")


sumAvgArray()
