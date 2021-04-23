""" Läs in positiva heltal. Inläsningen avbryts med 0.
Beräkna antalet ggr två intilliggande tal är lika.
exempel:
Your input nr was: 3
Your input nr was: 3
Your input nr was: 4
Your input nr was: 5
Your input nr was: 77
Your input nr was: 77
Your input nr was: 8
Your input nr was: 9
Your input nr was: 12
Your input nr was: 12
Your input nr was: 0
There are: 3 nr of occurances of the same nr
 """


def occurence():
    num1 = num2 = occurence = 0

    num1 = int(input("Insert nr: "))
    print(f"Your input was {num1}\n")

    while num1 != 0:
        num2 = int(input("Input nr: "))
        print(f"Your input was {num2}\n")

        if num1 == num2:
            occurence += 1
        num1 = num2
    print(f"There are {occurence} occurances of the same nr")


occurence()
