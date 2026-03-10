cards = input()
shuffles_count = int(input())

cards_list = cards.split(" ")
cards_count_half = int(len(cards_list) / 2)

for shuffle in range(shuffles_count):
    first_list = cards_list[:cards_count_half]
    second_list = cards_list[cards_count_half:]
    list_index = 0
    for index in range(cards_count_half):
        cards_list[list_index] = first_list[index]
        list_index += 1
        cards_list[list_index] = second_list[index]
        list_index += 1

print(cards_list)