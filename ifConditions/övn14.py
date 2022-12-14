''' Ange tre tal, ange också en sträng, 
Kontrollera om a är större än b, och c är större än a,
ELLER
om strängen d är exakt samma anges '''

# Exempel
# a = 200
# b = 33
# c = 100

d = "hi"

    
def compare(a, b, c, d):
    if (a > b and c > a) or d == "hi":
        print("One condition is  True")
    else:
        print("not true")
        
a = int(input("Mata in värdet för a: "))
b = int(input("Mata in värdet för b: "))
c = int(input("Mata in värdet för c: "))
d = input("Mata in värdet för d: ")

compare(a, b, c, d)
