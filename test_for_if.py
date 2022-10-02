def bigDiff():
    big = 0
    nextBig = 0
    diff = 0

    for i in range(1, 6):
        num = 0

        print(f"Input: {i}\n")

        num = int(input("Mata in tal: "))
        print(f"Du matade in talet: {num}\n\n")

        if num > big:
            nextBig = big
            big = num
        elif num > nextBig:
            nextBig = num

        diff = big - nextBig

    print(
        f"Skillnaden mellan den största talet {big} och det näst största talet {nextBig} är {diff}")


bigDiff()