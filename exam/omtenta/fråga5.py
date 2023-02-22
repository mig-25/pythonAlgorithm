def measure_blood_alcohol():
    readings = []
    num_days = 7

    for i in range(num_days):
        reading = float(input(f"Enter blood alcohol level for day {i+1}: "))
        readings.append(reading)

    total = sum(readings)
    average = total / num_days

    print(f"Total blood alcohol level for the week: {total:.2f}")
    print(f"Average blood alcohol level for the week: {average:.2f}")
    
measure_blood_alcohol()
