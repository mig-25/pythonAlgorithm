""" Läs in ett tal, Printa ut om talet är mindre än 10, mindre än 100, eller
större än 100
 """


def checkNum(num):
    if num < 10:
        print(f"{num} är mindre än 10")
    elif num < 100:
        print(f"{num} är mindre än 100")
    else:
        print(f"{num} är större än 100")


num = int(input("Mat in en siffra: "))

checkNum(num)
