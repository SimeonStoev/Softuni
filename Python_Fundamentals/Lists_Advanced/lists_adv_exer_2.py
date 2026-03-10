version_list = list(map(int, input().split(".")))

if version_list[2] == 9:
    if version_list[1] == 9:
        version_list[0] += 1
        version_list[1] = 0
        version_list[2] = 0
    else:
        version_list[1] += 1
        version_list[2] = 0
else:
    version_list[2] += 1

version_list = list(map(str, version_list))
print(".".join(version_list))
