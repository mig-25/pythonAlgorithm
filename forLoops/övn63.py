""" 
10 tal ska läsas in, kontrollera om talen ligger mellan intervallet:
om talet är mindre än 50 eller större än 100.
Om talen ligger i detta intervall, ska ordet RÄTT! skrivas ut, annars ska
FEL! skrivas ut. OBS! Intervall nr: et ska också skrivas ut, tex Input:1 osv
Exempel:
    
Input: 1
Mata in tal: 45
Du matade in talet: 45
ERROR!!!

Input: 2
Mata in tal: 67
Du matade in talet: 67
CORRECT!!!

Input: 3
Mata in tal: 11
Du matade in talet: 11
ERROR!!!

Input: 4
Mata in tal: 99
Du matade in talet: 99
CORRECT!!!

Input: 5
Mata in tal: 156
Du matade in talet: 156
ERROR!!!

Input: 6
Mata in tal: 89
Du matade in talet: 89
CORRECT!!!

Input: 7
Mata in tal: -12349
Du matade in talet: -12349
ERROR!!!

Input: 8
Mata in tal: 87
Du matade in talet: 87
CORRECT!!!

Input: 9
Mata in tal: 62
Du matade in talet: 62
CORRECT!!!

Input: 10
Mata in tal: 4567
Du matade in talet: 4567
ERROR!!!  
 """


def controllRange():
    num = 0

    for i in range(1, 11):
        print(f"Input: {i}")

        num = int(input("Mata in tal: "))
        print(f"Du matade in talet: {num}")

        if 50 > num or num > 100:
        #if num < 50 or num > 100:    
            print("ERROR!!!\n")
        else:
            print("CORRECT!!!\n")


controllRange()
