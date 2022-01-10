# Skapa tre Dictionaries, skapa seden en till en som innehåller all tre föregående

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


for name, year in myfamily.items():
    print(f"{name}: {year}")
