""" Läs in ett tal, och så länga talet inte är 9999, så beräkna medelvärdet
av de talen som läses in . Ta i akt, vad som händer om det första talet
som läses in är 9999

Exempel:

Mata in ett tal: 4
Input: 1. Du matade in 4
Mata in ett tal: 5
Input: 2. Du matade in 5
Mata in ett tal: 4
Input: 3. Du matade in 4
Mata in ett tal: 5
Input: 4. Du matade in 5
Mata in ett tal: 9999
Input: 5. Du matade in 9999
Medel av alla de inmatade talen är: 4.5
______________________________________________
Exempel: Om du matar in 9999 som första inpput

Mata in ett tal: 9999
Input: 1. Du matade in 9999
Du avslatade programmet genom skriva 9999
Medel av alla de inmatade talen är: 0
 """



def checkSumAvg():
    counter = 1
    sum = 0
    average = 0
    num = 0

    num = int(input("Mata in ett tal: "))
    print(f"Input: {counter}. Du matade in {num}")

    if num == 9999:
        print(f"Du avslatade programmet genom skriva {num}")

    while num != 9999:
        sum += num
        num = int(input("Mata in ett tal: "))
        if counter != 0:
            average = sum / counter
        counter += 1
        print(f"Input: {counter}. Du matade in {num}")

        ''' if counter != 0:
            average = sum / counter '''

    print(f"Medel av alla de inmatade talen är: {average}")
    
checkSumAvg()
