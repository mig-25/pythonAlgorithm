""" 
10 tal ska läsas in, kontrollera om talen ligger mellan intervallet:
50 till 100.
Om talen ligger i detta intervall, ska ordet RÄTT! skrivas ut, annars ska
FEL! skrivas ut. OBS! Intervall nr: et ska också skrivas ut, tex Input:1 osv
Exempel:
    
Input: 1
Mata in tal: 1
Du matade in talet: 1
ERROR!!!

Input: 2
Mata in tal: 2
Du matade in talet: 2
ERROR!!!

Input: 3
Mata in tal: 56
Du matade in talet: 56
CORRECT!!!

Input: 4
Mata in tal: 2
Du matade in talet: 2
ERROR!!!

Input: 5
Mata in tal: 89
Du matade in talet: 89
CORRECT!!!

Input: 6
Mata in tal: 78
Du matade in talet: 78
CORRECT!!!

Input: 7
Mata in tal: 897
Du matade in talet: 897
ERROR!!!

Input: 8
Mata in tal: 2
Du matade in talet: 2
ERROR!!!

Input: 9
Mata in tal: 66
Du matade in talet: 66
CORRECT!!!

Input: 10
Mata in tal: 34
Du matade in talet: 34
ERROR!!!    
 """


def controllRange():
    num = 0

    for i in range(1, 11):
        print(f"Input: {i}")

        num = int(input("Mata in tal: "))
        print(f"Du matade in talet: {num}")

        if 50 > num or num > 100:
            print("ERROR!!!\n")
        else:
            print("CORRECT!!!\n")


controllRange()
