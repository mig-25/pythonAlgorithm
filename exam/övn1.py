def kmToMiles(km):
    conversionRatio = 0.621371
    miles = km * conversionRatio
    print(f"Avståndet i mil är: {miles:.2f} mil")


km = float(input("Ange avståndet i km med decimaler: "))
kmToMiles(km)
