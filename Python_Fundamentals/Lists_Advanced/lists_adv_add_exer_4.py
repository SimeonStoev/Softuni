n = int(input())
battle_ships = []
destroyed_ships = 0

for i in range(n):
    battle_ships.append(list(map(int, input().split(" "))))

attacked_ships = list(map(str, input().split(" ")))

for cell in attacked_ships:
    cell_coord = list(map(int, cell.split("-")))
    if battle_ships[cell_coord[0]][cell_coord[1]] > 0:
        battle_ships[cell_coord[0]][cell_coord[1]] -= 1
        if battle_ships[cell_coord[0]][cell_coord[1]] == 0:
            destroyed_ships += 1

print(destroyed_ships)
