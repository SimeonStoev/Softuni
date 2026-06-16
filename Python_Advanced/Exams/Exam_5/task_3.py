def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for arg in args:
        card_name = arg[0]
        card_type = arg[1]
        if card_type == "monster":
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)

    for card, type in kwargs.items():
        if type == "monster":
            monster_cards.append(card)
        else:
            spell_cards.append(card)

    monster_cards.sort(reverse=True)
    spell_cards.sort()

    result = ""

    if len(monster_cards) > 0:
        result += "Monster cards:\n"
    for monster in monster_cards:
        result += f"  ***{monster}\n"

    if len(spell_cards) > 0:
        result += "Spell cards:\n"
    for spell in spell_cards:
        result += f"  $$${spell}\n"

    return result
