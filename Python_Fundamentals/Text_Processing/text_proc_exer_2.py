strings = input().split(" ")

smaller_string = ""
bigger_string = ""
sum = 0

if len(strings[0]) < len(strings[1]):
    smaller_string = strings[0]
    bigger_string = strings[1]
else:
    smaller_string = strings[1]
    bigger_string = strings[0]

for index in range(len(smaller_string)):
    sum += (ord(smaller_string[index]) * ord(bigger_string[index]))

for index in range(len(smaller_string), len(bigger_string)):
    sum += ord(bigger_string[index])

print(sum)
