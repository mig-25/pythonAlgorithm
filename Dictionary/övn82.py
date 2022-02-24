# Ta fram specifikt data från dictionary

car = {
    "brand": "Saab",
    "model": "Sport Combi",
    "year": 2009,
    "colors": ["red", "white", "blue"]
}

# ta fram data för ett specifikt nyckel
allColors = car["colors"]

print(f"Bilen finns med följande färger: {allColors}")

# med metoden get, samma resultat
modelType = car.get("model")
print(f"Bilen finns i följande modeller: {modelType}")

nrColors = len(car["colors"])
# ta fram hur många dataplatser för ett specifikt nyckel
print(f"Bilen finns med {nrColors} färger")

# key metoden tar fram alla nycklar i samlingen
allKeys = car.keys()
print(f"Bilen har följande datarubriker: {allKeys}")

# lägg till en ny rubrik
car["hp"] = 400
print(f"Bilen har följande datarubriker: {allKeys}")

# metoden values() retunerar all data i samligen
carData = car.values()
print(f"Bilen har följande data: {carData}")

# ändra data i samlingen
car["year"] = 2020
print(f"Bilen har följande data: {carData}")

# ändra data med update metoden
# car.update({"year": 2021})

# ta fram all data i form av noder i en lista
allItems = car.items()
print(f"Bilen har följande data: {allItems}")

# använd del metoden för ta bort en datanod(rubrik)
# addera först en rubrik för att sedan ta bort det
car["speed"] = 250
print(f"Bilen har följande data: {allItems}")
# ta bort rubriken speed och dess data
del car["speed"]
print(f"Bilen har följande data: {allItems}")

# använd del för att bort hela samligen
# OBS" använd med försiktighet
# del car

# använd clear för att töma en samling på all dess data
# skapa först en samling

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(f"Bilen har följande data: {x}")
thisdict.clear()
print(thisdict)

# kontrollera om datat existerar
if "model" in car:
    print("Ja, 'model' är en av rubrikerna i datasamlingen")
