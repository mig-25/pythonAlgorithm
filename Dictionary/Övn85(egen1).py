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