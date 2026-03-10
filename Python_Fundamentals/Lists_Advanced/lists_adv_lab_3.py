priority_task_list = []
to_do = input()

while to_do != "End":
    to_do_list = to_do.split("-")
    priority_task_list.append((int(to_do_list[0]), to_do_list[1]))

    to_do = input()

priority_task_list.sort(key=lambda x: x[0], reverse=False)
result = []
for elem in priority_task_list:
    result.append(elem[1])
print(result)
