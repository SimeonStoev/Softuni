first_empl_eff = int(input())
second_empl_eff = int(input())
third_empl_eff = int(input())
students_count = int(input())
one_hour_eff = first_empl_eff + second_empl_eff + third_empl_eff
v_hours = 0

while students_count > 0:
    v_hours += 1
    if v_hours % 4 == 0:
        continue

    students_count -= one_hour_eff

print(f"Time needed: {v_hours}h.")
