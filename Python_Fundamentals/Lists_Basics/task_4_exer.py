integers = input()
beggars = int(input())
integers_list = integers.split(", ")
beggars_wages = [0] * beggars

for beggar in range(beggars):
    for index in range(beggar, len(integers_list), beggars):
        beggars_wages[beggar] += int(integers_list[index])

print(beggars_wages)
