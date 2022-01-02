""" 
Inom matematiken är den största gemensamma delaren av två eller flera heltal vilka
 alla inte är noll det största heltal som delar alla talen. 
 Största gemensamma delaren av heltalen a och b skrivs ofta SGD
Skriv en funktion för att få den största gemensamma delaren (sgd) av två heltal
Med talen 9 och 3 ska svaret printas som följande:

Mata in första heltalet: 9
Mata in andra heltalet: 3
SGD av talet:9 och talet: 3 är 3
 """


def gcd():
    gcd = 0

    num1 = int(input("Mata in första heltalet: "))
    num2 = int(input("Mata in andra heltalet: "))

    for i in range(1, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    print(f"SGD av talet:{num1} och talet: {num2} är {gcd}")


gcd()
