""" 
Omvandla dollar och pund till kr 
1 dollar är 8.45514 kr, 1 pund är 12.1283 kr
Användaren får mata in dollar och pund 
svaret ska vara med 2 decimaler
 """

sek = int()
rateDollar = float(9.1790)
ratePund = float(12.5799)


def sekToDollar(USD):
    sek = rateDollar*USD
    return sek


def sekToPound(GBP):
    sek = ratePund*GBP
    return sek


USD = int(input("Input $: "))
GBP = int(input("Input £: "))
sek = sekToDollar(USD)
sek = sekToPound(GBP)


print(f"{USD} dollar är: {sekToDollar(USD):.2f} kr, och {GBP} pund är: {sekToPound(GBP):.2f} kr")
