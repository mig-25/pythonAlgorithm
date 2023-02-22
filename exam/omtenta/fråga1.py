def pints_to_liters():
    pints = float(input("Enter a volume in pints: "))
    liters = pints * 0.473176
    print("The volume in liters is: {:.2f}".format(liters))

pints_to_liters()
