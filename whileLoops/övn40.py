""" Läs in ett antal positiva heltal sorterade i växande ordning. Talföljden slut anges med 0.
Om det finns fel i sorteringsordningen ska utskriften ske enligt följande exempel:
     Exempel på talföjd som matas in , och dess resultat:

Mata in första talet: 2
Första siffran: 1 var 2
Mata in efterföljande tal: 3
Siffran nr: 2: var 3

Mata in efterföljande tal: 678
Siffran nr: 3: var 678

Mata in efterföljande tal: 67
Siffran nr: 4: var 67

Siffran nr: 4 var fel, dess värde är: 67, det borde har varit större än 678

Mata in efterföljande tal: 0
Siffran nr: 5: var 0

Siffran nr: 5 var fel, dess värde är: 0, det borde har varit större än 67
 """


def correctOrder():
    num1 = num2 = 0

    num1 = int(input("Mata in första talet: "))
    counter = 1
    print(f"Första siffran: {counter} var {num1}")
    while num1 != 0:
        counter += 1
        #print(f"Efterföljande siffra: {counter}")
        num2 = int(input("Mata in efterföljande tal: "))

        print(f"Siffran nr: {counter}: var {num2}\n")

        if num2 < num1:
            print(
                f"Siffran nr: {counter} var fel, dess värde är: {num2}, det borde har varit större än {num1}\n")

        num1 = num2

        if num1 == 0 or num2 == 0:
            break


correctOrder()
