""" Läs in ett tal, och så länga talet inte är 9999, så beräkna medelvärdet
av de talen som läses in . Ta i akt, vad som händer om det första talet
som läses in är 9999
Exempel:
Input: 1
Your input nr was: 4
Input: 2
Your input nr was: 5
Input: 3
Your input nr was: 4
Input: 4
Your input nr was: 5
Input: 5
Your input nr was: 4
Input: 6
Your input nr was: 9999
The average of the supplied integers are: 4.5
______________________________________________
Exempel
Om du matar in 9999 som första inpput
You ended the program by entering 9999
The average of the supplied integers are: 0
 """

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
