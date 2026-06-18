def cookbook(*args):
    cuisines = {}
    recipes = {}

    for recipe, cuisine, ingredients in args:
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append(recipe)
        recipes[recipe] = ingredients

    cuisines = dict(sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine in cuisines:
        recipes_list = cuisines[cuisine]
        recipes_list.sort()
        cuisines[cuisine] = recipes_list

    result = ""

    for cuisine, recipes_list in cuisines.items():
        result += f"{cuisine} cuisine contains {len(recipes_list)} recipes:\n"
        for recipe in recipes_list:
            result += f"  * {recipe} -> Ingredients: {', '.join(recipes[recipe])}\n"

    return result
