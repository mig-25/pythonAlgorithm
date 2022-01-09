n = int(input("Ange antal frukter: "))
shoppingCart = {}

for i in range(n):
    fruit = input("Ange frukt: ")  # here i have taken keys as strings
    # here i have taken values as integers
    cost = int(input("vad kostar frukten: "))
    shoppingCart[fruit] = cost
print(f" Innehåll och pris i kundvagnen: {shoppingCart}")

cost = shoppingCart.values()
# Return values of a dictionary
total = sum(cost)
print(f"Total kostnaden för alla frukter är: {total} kr")
