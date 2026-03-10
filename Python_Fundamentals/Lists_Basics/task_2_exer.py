factor = int(input())
count = int(input())
numb_list = []

for i in range(1, count+1):
    numb_list.append(i * abs(factor))

print(numb_list)