def is_lesson_exists(lesson, arr):
    return any(lesson in l for l in arr)


lessons = input().split(", ")
command = input()

while command != "course start":
    command_list = command.split(":")
    if command_list[0] == "Add":
        if not is_lesson_exists(command_list[1], lessons):
            lessons.append(command_list[1])
    elif command_list[0] == "Insert":
        if not is_lesson_exists(command_list[1], lessons):
            lessons.insert(int(command_list[2]), command_list[1])
    elif command_list[0] == "Remove":
        if is_lesson_exists(command_list[1], lessons):
            if is_lesson_exists(command_list[1] + "-Exercise", lessons):
                elem_to_remove_index = lessons.index(command_list[1])
                lessons.pop(elem_to_remove_index + 1)
            lessons.remove(command_list[1])
    elif command_list[0] == "Swap":
        if is_lesson_exists(command_list[1], lessons) and is_lesson_exists(command_list[2], lessons):
            lesson_1_index = lessons.index(command_list[1])
            lesson_2_index = lessons.index(command_list[2])
            exer_1_index = -1
            exer_2_index = -1
            if is_lesson_exists(command_list[1] + "-Exercise", lessons):
                exer_1_index = lessons.index(command_list[1]) + 1
            if is_lesson_exists(command_list[2] + "-Exercise", lessons):
                exer_2_index = lessons.index(command_list[2]) + 1

            temp = lessons[lesson_1_index]
            lessons[lesson_1_index] = lessons[lesson_2_index]
            lessons[lesson_2_index] = temp

            if exer_1_index != -1 and exer_2_index != -1:
                temp_exer = lessons[exer_1_index]
                lessons[exer_1_index] = lessons[exer_2_index]
                lessons[exer_2_index] = temp_exer
            elif exer_1_index != -1:
                temp_exer = lessons[exer_1_index]
                lessons.remove(temp_exer)
                lessons = lessons[:lesson_2_index + 1] + [temp_exer] + lessons[lesson_2_index + 1:]
            elif exer_2_index != -1:
                temp_exer = lessons[exer_2_index]
                lessons.remove(temp_exer)
                lessons = lessons[:lesson_1_index + 1] + [temp_exer] + lessons[lesson_1_index + 1:]
    else:
        if not is_lesson_exists(command_list[1], lessons):
            lessons.append(command_list[1])
            lessons.append(command_list[1] + "-Exercise")
        else:
            if not is_lesson_exists(command_list[1] + "-Exercise", lessons):
                lesson_index = lessons.index(command_list[1])
                lessons = lessons[:lesson_index + 1] + [command_list[1] + "-Exercise"] + lessons[lesson_index + 1:]

    command = input()

for index in range(len(lessons)):
    print(f"{index + 1}.{lessons[index]}")
