''' ange två tal, dubblera första talet, testa om det första talet
x 2 är större än det andra talet, testa om det första talet x 2 är mindre än det andra talet, 
testa om tal1 gånger 2 är lika med tal 2
 '''


def checkDouble(in1, in2):
    if (in1 * 2) > in2:
        print(
            f"Talet {in1} * 2, är lika med {in1*2}, det är större än tal2: {in2}")
    elif (in1 * 2) < in2:
        print(
            f"Talet {in1} * 2, är lika med {in1*2}, det är inte större än tal2: {in2}")
    else:
        print(f'{in1} * 2 är: {in1*2}, dem är lika stora')


in1 = int(input("Mata in första talet: "))
in2 = int(input("Mata in andra talet: "))

checkDouble(in1, in2)
