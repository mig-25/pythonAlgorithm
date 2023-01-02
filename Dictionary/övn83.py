''' Du kan loopa genom en Dictionairy med en for loop
När du loopar genom en Dictionairy, är returvärdet nycklarna 
i datasamlingen, men det finns metoder att även retunera 
värdet till nycklarna '''

car = {
    "brand": "Saab",
    "model": "Sport Combi",
    "year": 2009,
    "colors": ["red", "white", "blue"]
}

print("Print all key names in the dictionary, one by one:")
for key in car:
    print(key)

print("Print all values in the dictionary, one by one:")

for value in car:
    print(car[value])

print("You can also use the values() method to return values of a dictionary:")

for values in car.values():
    print(values)
    
print("You can also use the keys() method to return keys of a dictionary:")

for keys in car.keys():
    print(keys)

print("Loop through both keys and values, by using the items() method")

# carInfo and carData act like aliases for keys, values pair.
for carInfo, carData in car.items():
    print(f"{carInfo}: {carData}")
