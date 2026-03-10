string = input()
appearances = 0

for i in range(len(string)):
    if string[i:i+4].lower() == "sand" or string[i:i+5].lower() == "water" or string[i:i+4].lower() == "fish" or string[i:i+3].lower() == "sun":
        appearances += 1

print(appearances)