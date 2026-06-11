def plant_garden(garden_space, *args, **kwargs):
    planted_plants = {}
    allowed_plants = {plant_data[0]: plant_data[1] for plant_data in args}
    plant_request = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    all_plants_planted = True

    for plant, number_of_plants_requested in plant_request.items():

        if plant in allowed_plants:
            space = allowed_plants[plant]
            max_planted = number_of_plants_requested * space
            if max_planted <= garden_space:
                planted_plants[plant] = number_of_plants_requested
                garden_space -= max_planted
            else:
                all_plants_planted = False
                possible_plants = int(garden_space // space)
                if possible_plants > 0:
                    planted_plants[plant] = possible_plants
                    garden_space -= possible_plants * space

    result = ""
    if all_plants_planted:
        result += f"All plants were planted! Available garden space: {garden_space:.1f} sq meters.\n"
    else:
        result += "Not enough space to plant all requested plants!\n"

    if planted_plants:
        result += "Planted plants:\n"
    result += "\n".join(f"{plant}: {number}" for plant, number in planted_plants.items())

    return result
