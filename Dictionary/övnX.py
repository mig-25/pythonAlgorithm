adressBook = {}


def contactBook():
    active = True
    while active:

        name = input("Ange namn: ")
        phone = int(input(f"Vad är {name}'s telnr: "))
        adressBook[name] = phone

        repeat = input(
            "Vill du lägga till en ny kontakt? (j/n) ")
        if repeat == 'n':
            active = False

    print("\n")
    print("-------Telefonlista--------")

    for name, phone in adressBook.items():
        print(f" Namn: {name} \n Telefon: {phone}")


contactBook()
