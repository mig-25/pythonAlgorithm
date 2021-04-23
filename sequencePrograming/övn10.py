''' Omvandla Farhenheit till Celsius
Skapa en funktion som tar emot temp
i farenheit från anvädaren och omvandlar
det till celsius med två decimaler och svaret avrundas uppåt'''


def fToC(far):
    celsius = (far-32)/1.8
    return celsius


f = float(input("Mata in tempratur i farenheit: "))

celsius = fToC(f)

print(f"{f:.1f}° farenheit är {celsius:.1f}° grader celsius")
