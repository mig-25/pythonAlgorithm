""" Skapa en array med fem tal, fördubbla värdet på talen på varje indexplats
i arrayn. Exempel utprinten ska vara på följande sätt, era värden kan dock
variear beroende på siffrorna i eran array, får enbart lösas med någon typ
av for loo.

Exempel:

Mata in talet att fördubbla: 2
Det dubbla värdet av 2 är 4

Mata in talet att fördubbla: 3
Det dubbla värdet av 3 är 6

Mata in talet att fördubbla: 4
Det dubbla värdet av 4 är 8

Mata in talet att fördubbla: 5
Det dubbla värdet av 5 är 10

Mata in talet att fördubbla: 6
Det dubbla värdet av 6 är 12

 """


def doubleValue():
    result = 0
    num = []

    for i in range(1, 6):
        num = str(input("Mata in talet att fördubbla: "))

        result = int(num)*2
        print(f"Det dubbla värdet av {num} är {result}\n")


doubleValue()
