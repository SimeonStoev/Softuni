def team_lineup(*args):
    football_contries = {}

    for player, contry in args:
        if contry not in football_contries:
            football_contries[contry] = []
        football_contries[contry].append(player)

    football_contries_sorted = dict(sorted(football_contries.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ""

    for country, players in football_contries_sorted.items():
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result
