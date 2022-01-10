''' Du kan inte kopiera en Dictionairy helt enkelt genom att skriva följande,
dict2 = dict1, eftersom: dict2 endast kommer att vara en referens till dict1, 
och ändringar som görs i dict1 kommer automatiskt också att göras i dict2.

Det finns sätt att göra en kopia, ett sätt är att använda den inbyggda Dictionary-metoden copy().
 '''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()

for carInfo, carData in mydict.items():
    print(f"{carInfo}: {carData}")

# Ett annat sätt att göra en kopia är att använda den inbyggda metoden dict().
thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict1 = dict(thisdict2)
print(mydict)
