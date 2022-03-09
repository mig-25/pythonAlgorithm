''' ange två tal, dubblera första talet, testa om det första talet
är dubbelt så stort som det andra talet,
printa som följande exempel:

Mata in första talet: 5
Mata in andra talet: 9
Talet 5 * 2 är: 10, det är dubbelt så stort än 9

om inte dubbel så stor, skriv inte dubbelt så stor
printa som följande exempel:

Mata in första talet: 4
Mata in andra talet: 10
Talet 4 * 2 är: 8, det är inte dubbelt så stort än 10

annars om dem är lika skriv ut som följande exempel:

Mata in första talet: 2
Mata in andra talet: 4
2 * 2 är: 4, dem är lika stora
 '''


def checkDouble(in1, in2):
    if (in1 * 2) > in2:
        print(
            f"Talet {in1} * 2, är lika med {in1*2}, det är dubbelt så stort som {in2}")
    elif (in1 * 2) < in2:
        print(
            f"Talet {in1} * 2, är lika med {in1*2}, det är inte dubbelt så stort som {in2}")
    else:
        print(f'{in1} * 2 är: {in1*2}, dem är lika stora')


in1 = int(input("Mata in första talet: "))
in2 = int(input("Mata in andra talet: "))

checkDouble(in1, in2)
