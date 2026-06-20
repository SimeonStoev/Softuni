def sort_games(*args, **kwargs):
    pc_games = {}
    console_games = {}

    for platform, game in args:
        if platform == "pc":
            for release_id, dic_game in kwargs.items():
                if game == dic_game:
                    pc_games[game] = release_id
        else:
            for release_id, dic_game in kwargs.items():
                if game == dic_game:
                    console_games[game] = release_id

    pc_games = dict(sorted(pc_games.items(), key=lambda x: x[1], reverse=True))
    console_games = dict(sorted(console_games.items(), key=lambda x: x[1]))

    result = ""

    if len(console_games) > 0:
        result += "Console Games:\n"
        for game, release_date in console_games.items():
            rd_last_index = release_date.rfind("_")
            release_date = release_date[:rd_last_index]
            result += f">>>{release_date}: {game}\n"

    if len(pc_games) > 0:
        result += "PC Games:\n"
        for game, release_date in pc_games.items():
            rd_last_index = release_date.rfind("_")
            release_date = release_date[:rd_last_index]
            result += f"<<<{release_date}: {game}\n"

    return result
