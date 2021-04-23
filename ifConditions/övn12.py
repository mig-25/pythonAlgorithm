''' ange två tal, testa om det första talet
är dubbelt så stort som det andra talet,
i så fall, skriv ut "För stort"
 '''


def checkDouble(in1, in2):
    if in1 * 2 > in2:
        print("För stort")
    else:
        print("Inte för stort")


in1 = int(input("Mata in första talet: "))
in2 = int(input("Mata in andra talet: "))

checkDouble(in1, in2)
