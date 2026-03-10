population = list(map(int, input().split(", ")))
min_wealth = int(input())
error_message = ""

for index in range(len(population)):
    if population[index] < min_wealth:
        richest_person = max(population)
        richest_person_index = population.index(richest_person)
        add_wealth = min_wealth - population[index]
        if richest_person - add_wealth < min_wealth:
            error_message = "No equal distribution possible"
            break
        else:
            population[index] += add_wealth
            population[richest_person_index] -= add_wealth

if error_message == "":
    print(population)
else:
    print(error_message)
