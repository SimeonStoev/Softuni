def is_valid_cell(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
space = []
curr_resources = 100
max_resources = 100
spaceship_x, spaceship_y = -1, -1

# Четем матрицата и намираме старта
for i in range(n):
    row = input().split()
    if "S" in row:
        spaceship_x = i
        spaceship_y = row.index("S")
        # Веднага маркираме старта като '.', за да не ни пречи
        row[spaceship_y] = "."
    space.append(row)

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

mission_outcome = ""

# Въртим цикъл, докато не получим краен изход (винаги има достатъчно команди)
while True:
    command = input()

    # 1. Всяко преместване струва 5 ресурса
    curr_resources -= 5

    move_x, move_y = commands[command]
    new_x = spaceship_x + move_x
    new_y = spaceship_y + move_y

    # 2. Проверка за излизане от границите
    if not is_valid_cell(new_x, new_y):
        mission_outcome = "lost"
        break

    # Преместваме кораба на новата позиция
    spaceship_x, spaceship_y = new_x, new_y
    current_cell = space[spaceship_x][spaceship_y]

    # 3. Проверка за Станция
    if current_cell == "R":
        curr_resources += 10
        if curr_resources > max_resources:
            curr_resources = max_resources

    # 4. Проверка за Метеорит
    elif current_cell == "M":
        curr_resources -= 5
        space[spaceship_x][spaceship_y] = "."  # Метеоритът се унищожава

    # 5. Проверка за Планета B
    elif current_cell == "P":
        # Корабът каца успешно, излиза се от цикъла
        mission_outcome = "success"
        break

    # 6. Проверка дали сме останали без ресурси (след като сме обработили клетката)
    if curr_resources < 5:
        mission_outcome = "stranded"
        break

# Принтиране на резултатите спрямо флага mission_outcome
if mission_outcome == "success":
    print(f"Mission accomplished! The spaceship reached Planet B with {curr_resources} resources left.")
elif mission_outcome == "stranded":
    print("Mission failed! The spaceship was stranded in space.")
    space[spaceship_x][spaceship_y] = "S"  # Маркираме последната позиция
elif mission_outcome == "lost":
    print("Mission failed! The spaceship was lost in space.")
    space[spaceship_x][spaceship_y] = "S"  # Маркираме последната позиция преди излизането

# Принтиране на финалната матрица
for row in space:
    print(*row)