Skript = {
    "Start": "Jan",
    "Slut": "Feb",
    "Poang": 30,
    "Betyg": ["G", "VG"]
}

Incidenthantering = {
    "Start": "Feb",
    "Slut": "Mars",
    "Poang": 30,
    "Betyg": ["G", "VG"]
}

Projektarbete = {
    "Start": "Mars",
    "Slut": "April",
    "Poang": 30,
    "Betyg": ["G", "VG"]
}

ItSak = {
    "Skript": Skript,
    "Incidenthantering": Incidenthantering,
    "Projektarbete": Projektarbete,
}

for info, varde in ItSak.items():
    print(f"{info}: {varde}")

# for carInfo, carData in car.items():
#     print(f"{carInfo}: {carData}")

# ''' allItems = car.items()
# print(f"Bilen har följande data: {allItems}") '''
