def calculate_baggage_penalty():
    baggage = {}
    total_weight = 0

    while True:
        add_baggage = input("Do you want to add baggage (y/n)? ")
        if add_baggage.lower() != 'y':
            break
        baggage_type = input("Enter baggage type (e.g. hand luggage, checked baggage, etc.): ")
        weight = float(input("Enter baggage weight in kg: "))
        baggage[baggage_type] = weight
        total_weight += weight

    if total_weight > 20:
        penalty = (total_weight - 20) * 2
        print(f"Total weight of baggage is {total_weight:.2f} kg, with a penalty of {penalty:.2f} EUR for exceeding 20 kg.")
    else:
        print(f"Total weight of baggage is {total_weight:.2f} kg.")

calculate_baggage_penalty()