string = input()
fire_cells_list = string.split("#")
water = int(input())

effort = 0
total_fire = 0

print("Cells:")

for cells in fire_cells_list:
    fire_cells = cells.split(" = ")
    if water - int(fire_cells[1]) >= 0:
        if (fire_cells[0] == "High" and 81 <= int(fire_cells[1]) <= 125) or (
                fire_cells[0] == "Medium" and 51 <= int(fire_cells[1]) <= 80) or (
                fire_cells[0] == "Low" and 1 <= int(fire_cells[1]) <= 50):
            total_fire += int(fire_cells[1])
            water -= int(fire_cells[1])
            effort += float(fire_cells[1]) * 0.25
            print(f"- {fire_cells[1]}")

    if water == 0:
        break

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
