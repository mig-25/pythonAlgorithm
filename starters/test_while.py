# Ett värde skall fördubblas så länge det är mindre än 1000
def doubleValue(num):
    while num < 1000:        
        sum = num * 2
        print(f"Summan är {sum}")
        num = int(input("Mata in en siffra: "))
    
    
num = int(input("Mata in en siffra: "))

doubleValue(num)


