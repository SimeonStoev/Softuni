number_of_days = int(input())
liters_rakia = 0
rakia_degree = 0

for i in range(number_of_days):
    liters_rakia_for_day = float(input())
    rakia_degrees_for_day = float(input())
    liters_rakia += liters_rakia_for_day
    rakia_degree += liters_rakia_for_day * rakia_degrees_for_day

rakia_degree /= liters_rakia

print(f"Liter: {liters_rakia:.2f}")
print(f"Degrees: {rakia_degree:.2f}")
if rakia_degree < 38:
    print("Not good, you should baking!")
elif 38 <= rakia_degree <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
