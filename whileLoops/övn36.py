""" Läs in 4 värden för variablen num, om värdet på num är mellan 5000
till 10000, skriv ut summan och skriv sedan medelvärdet för samtliga siffror
Exempel:
Input: 1
Your input nr was: 5001
Input: 2
Your input nr was: 9999
Input: 3
Your input nr was: 65
Input: 4
Your input nr was: 4
The sum of the numbers between 5000 and 10000 are: 15000
The average of all the supplied integers are: 3750
 """

counter = 1
sum = 0
num = 0

while counter <= 4:
    print(f"Input {counter}")

    if 5000 < num and num < 10000:
        sum += num
    num = int(input("Skriv in ett tal: "))
    counter += 1
print(f"Summan av talen mellan 5000 och 10000 är {sum}")
print(f"Medel av alla talen är {sum/4}")
