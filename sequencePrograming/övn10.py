''' Omvandla grader Fahrenheit till Celsius
Skapa en funktion som tar emot temp
i Fahrenheit från användaren och omvandlar
det till Celsius med två decimaler och svaret avrundas uppåt'''


def fToC(far):
    celsius = (far-32)/1.8
    return celsius


f = float(input("Mata in tempratur i farenheit: "))

celsius = fToC(f)

print(f"{f:.2f}° farenheit är {celsius:.2f}° grader celsius")
