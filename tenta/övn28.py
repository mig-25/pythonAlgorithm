""" Ange tempratur, om temp är mellan 18 till 25 grader, så ska Lagom skrivas
ut.
Om det är varmare än 25 grader så ska För varmt skrivas ut.
Om det är under 18 grader så ska det skrivas ut, För kallt.
 """


def checkTemp(temp):
    if 18 <= temp and temp <= 25:
        print(f"{temp}° är lagom varmt")
    elif temp > 25:
        print(f"{temp}° är för varmt")
    else:
        print(f"{temp}° är för kallt")


temp = float(input("Mata in tempratur: "))

checkTemp(temp)
