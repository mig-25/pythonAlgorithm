# skriv ut resultatet av formeln ax^3+7 med en funktion som tar in parametrar för a och x


def formula(a, x):
    anwser = a * (x ** 3) + 7
    return anwser


a = int(input("Mata in a: "))
x = int(input("Mata in x: "))

answer = formula(a, x)

print(f"Svaret på formeln ax^3+7 är: {answer}")
