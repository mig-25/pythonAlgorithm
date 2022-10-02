def multi(num):
    
    result = 0
    for x in range(1, 11):
        result = num*2
        print(f"Omgång: {x} är svaret {result}")
        num=num+1


num = int(input("Mata in tal: "))
multi(num)

""" result = 0
num = int(input("Mata in tal: "))
for x in range(1,11):
    result = num * 2
    print(f"Omgång: {x} är svaret {result}")
    num=num+1 """

