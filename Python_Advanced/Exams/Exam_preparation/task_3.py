def boarding_passengers(ship_capacity, *args):
    all_passengers_boarded = True
    boarded_passengers = {}
    total_groups = sum(1 for x in args)
    boarded_groups = 0

    for group in args:
        people_count = group[0]
        benefit_plan = group[1]

        if ship_capacity == 0:
            break

        if people_count > ship_capacity:
            continue

        ship_capacity -= people_count
        boarded_groups += 1

        if benefit_plan not in boarded_passengers:
            boarded_passengers[benefit_plan] = 0
        boarded_passengers[benefit_plan] += people_count

    boarded_passengers = dict(sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0])))

    result = "Boarding details by benefit plan:\n"
    for benefit_plan, people_count in boarded_passengers.items():
        result += f"## {benefit_plan}: {people_count} guests\n"

    if total_groups > boarded_groups:
        all_passengers_boarded = False

    if all_passengers_boarded:
        result += f"All passengers are successfully boarded!"
    elif ship_capacity == 0 and not all_passengers_boarded:
        result += f"Boarding unsuccessful. Cruise ship at full capacity."
    elif ship_capacity > 0 and not all_passengers_boarded:
        result += f"Partial boarding completed. Available capacity: {ship_capacity}."

    return result
