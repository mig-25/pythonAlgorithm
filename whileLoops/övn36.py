""" Läs in 4 värden för variablen num, om värdet på num är mellan 5000
till 10000, skriv ut summan och skriv sedan medelvärdet för samtliga siffror
Input 1
Skriv in ett tal: 5001
Input 2
Skriv in ett tal: 9999
Input 3
Skriv in ett tal: 65
Input 4
Skriv in ett tal: 4


Summan av talen mellan 5000 och 10000 är 15000
Medel av alla talen är 3750.0

OBS! Notera noga i svaret ovan vart svaret ska printa ut, i loppen eller utanför?
 """


def sumAvg():

    counter = 1
    sum = 0
    num = 0

    while counter <= 4:
        print(f"Input {counter}")

        if 5000 < num and num < 10000:
            sum += num
            
        num = int(input("Skriv in ett tal: "))
        
        counter += 1
        
    
    print("\n")
    print(f"Summan av talen mellan 5000 och 10000 är {sum}")
    print(f"Medel av alla talen är {sum/4}")


sumAvg()
