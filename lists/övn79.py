""" Läs in en array som består av nämnare och täljare, om nämnare är ett negativ, skapa ett fel meddelande,
    sedan omvandlar du det negativa talet till ett positivt tal
    Om du matar in 6 och -5 så SKA printen vara i följande format:
    
Exempel:

Mata in täljaren: 6
Mata in nämnaren: -5
 FEL!!! Nämnare får inte vara 0
Täljaren är 6 och nämnare är 5    
    
 """


def div():
    numbers = []

    number = int(input("Mata in täljaren: "))
    numbers.append(number)

    for i in range(0, 1):
        number = int(input("Mata in nämnaren: "))
        numbers.append(number)
        if numbers[1] <= 0:
            print(f" FEL!!! Nämnare får inte vara 0")
            numbers[1] = numbers[1] * -1

    print(f"Täljaren är {numbers[0]} och nämnare är {numbers[1]}")


div()
