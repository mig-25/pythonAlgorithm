shoppingCart = {}


print("Lägg till varor och ange pris")
print("\n")
print(f"-----------Varor---------------")


def cart():
    active = True
    counter = 0
    while active:
        product = input("Ange vara: ")  # here i have taken keys as strings
        # here i have taken values as integers
        cost = int(input("vad kostar varan: "))
        shoppingCart[product] = cost

        counter = counter + 1

        # Find out if anyone else if going to take the poll.
        repeat = input("Vill du lägga till fler varor? (j/n) ")
        if repeat == 'n':
            active = False

    print("\n")
    print(f"Din kundvagn innehåller {counter} varor:")
    print(f"---------------------------------")
    for product, price in shoppingCart.items():
        print(
            f"Varan: {product}, pris: {price} kr")

    cost = shoppingCart.values()
    # Return values of a dictionary
    total = sum(cost)
    print(f"--------- Summan: {total} kr --------")


cart()
