sequence_of_cards = input()
team_a_players = 11
team_b_players = 11
team_a_off_players = []
team_b_off_players = []

list_of_cards = sequence_of_cards.split()

for card in list_of_cards:
    team = card.split("-")[0]
    player = card.split("-")[1]
    if team == "A":
        if player not in team_a_off_players:
            team_a_off_players.append(player)
            team_a_players -= 1
    else:
        if player not in team_b_off_players:
            team_b_off_players.append(player)
            team_b_players -= 1

    if team_a_players < 7 or team_b_players < 7:
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if team_a_players < 7 or team_b_players < 7:
    print("Game was terminated")
