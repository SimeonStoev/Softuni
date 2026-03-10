string_seq_1 = input().split(", ")
string_seq_2 = input().split(", ")

string_seq_result = []

for elem in string_seq_1:
    if any(elem in string for string in string_seq_2):
        string_seq_result.append(elem)

print(string_seq_result)
