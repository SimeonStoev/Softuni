def merge_elem_to_list(start_index, end_index, arr):
    if start_index < 0:
        start_index = 0
    if end_index >= len(arr):
        end_index = len(arr) - 1

    merge_element = "".join([str(elem) for elem in arr[start_index:end_index + 1]])
    return arr[:start_index] + merge_element.split() + arr[end_index + 1:]


def divide_elem_to_list(index, partitions, arr):
    divide_element = []
    if len(arr[index]) % partitions == 0:
        i = 0
        step = int(len(arr[index]) / partitions)
        while i < len(arr[index]):
            divide_element.append(arr[index][i:i + step])
            i += step
    else:
        i = 0
        step = int(len(arr[index]) // partitions)
        counter = 1
        while counter < partitions:
            divide_element.append(arr[index][i:i + step])
            i += step
            counter += 1
        divide_element.append(arr[index][i:])

    return arr[:index] + divide_element + arr[index + 1:]


input_list = input().split(" ")

command = input()

while command != "3:1":
    command_list = command.split(" ")
    if command_list[0] == "merge":
        input_list = merge_elem_to_list(int(command_list[1]), int(command_list[2]), input_list)
    else:
        input_list = divide_elem_to_list(int(command_list[1]), int(command_list[2]), input_list)

    command = input()

print(" ".join(input_list))
