''' Utifrån två tal, skriv ut om det är lika,
om den första är strörre än den andra,
eller om den andra är störra en den första
 '''


def checkLargest(in1, in2):
    if in1 == in2:
        print(f"tal1: {in1} är detsamma som tal2: {in2}")
    elif in1 > in2:
        print(f"tal1: {in1} är större än tal2: {in2}")
    else:
        print(f"tal1: {in1} är mindre än tal2: {in2}")


in1 = int(input("Mata in första talet: "))
in2 = int(input("Mata in andra talet: "))

checkLargest(in1, in2)
