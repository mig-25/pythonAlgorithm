""" Skriv en JavaScript-funktion för att få den största gemensamma delaren(gcd) av två heltal
Med talen 9 och 3 ska svaret printas som följande:

Mata in första heltalet: 9
Mata in andra heltalet: 3
GCD of talet:9 och talet: 3 är 3
 """


def gcd():
    gcd = 0

    num1 = int(input("Mata in första heltalet: "))
    num2 = int(input("Mata in andra heltalet: "))

    for i in range(1, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    print(f"GCD of talet:{num1} och talet: {num2} är {gcd}")


gcd()
