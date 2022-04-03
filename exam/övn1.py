# Konvertera x antal grader i celsius till kelvin, svaret ska vara med två decimaler
def kToC(cel):
    conversionRatio = 273.15
    kelvin = cel + conversionRatio
    print(f"{cel} celsius är: {kelvin:.2f} kelvin")


cel = float(input("Ange tempraturen i celsius med decimaler: "))
kToC(cel)
