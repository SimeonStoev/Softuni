sub_str = input()
string = input()

while sub_str in string:
    string = string.replace(sub_str, "")

print(string)
