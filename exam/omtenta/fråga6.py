def measure_blood_alcohol():
    readings = {}
    num_days = 7

    for i in range(num_days):
        reading = float(input(f"Enter blood alcohol level for day {i+1}: "))
        readings[f"day {i+1}"] = reading

    with open("report.txt", "w") as file:
        for day, level in readings.items():
            file.write(f"{day}: {level:.2f}\n")

        if any(level > 5 for level in readings.values()):
            status = "FAIL"
        else:
            status = "PASS"

        file.write(f"Status: {status}\n")
        
measure_blood_alcohol()
