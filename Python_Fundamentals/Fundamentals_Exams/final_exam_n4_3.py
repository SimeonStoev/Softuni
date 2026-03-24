n = int(input())
heroes = {}

for _ in range(n):
    hero_data = input().split()
    name = hero_data[0]
    hp = int(hero_data[1])
    mp = int(hero_data[2])
    heroes[name] = {"hp": hp, "mp": mp}

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["mp"] >= mp_needed:
            heroes[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]["hp"] -= damage
        if heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name]["mp"] + amount > 200:
            amount = 200 - heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name]["hp"] + amount > 100:
            amount = 100 - heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] += amount
        print(f"{hero_name} healed for {amount} HP!")

for key, value in heroes.items():
    print(key)
    print(f"  HP: {value['hp']}")
    print(f"  MP: {value['mp']}")
