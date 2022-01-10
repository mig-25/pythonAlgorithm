# En ordbok kan innehålla ordböcker, detta kallas kapslade ordböcker.

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for name, year in myfamily.items():
    print(f"{name}: {year}")
