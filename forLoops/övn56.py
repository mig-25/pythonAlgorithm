# Skriv ut multiplikationstabble från ettan till tolvans tabell
# Printen ska ske i tabell format

""" 
1       2       3       4       5       6       7       8       9       10      11      12
---------------------------------------------------------------------------------------------

1       2       3       4       5       6       7       8       9       10      11      12

2       4       6       8       10      12      14      16      18      20      22      24

osv.... """

# Printa ut kolumnerna


def multiplicationTable():
    print("\t\t\tMultiplication Table\n")
    for i in range(1, 13):
        print(i, end="\t")
    print()
    print("---------------------------------------------------------------------------------------------\n")

    # Printa ut det yttre loopen, lodrätt
    for j in range(1, 11):
        # printa ut det inre loopen, vägrätt
        for k in range(1, 13):
            print(j*k, end="\t")
        print("\n")


multiplicationTable()
