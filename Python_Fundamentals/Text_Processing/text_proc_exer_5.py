string = input()
emoticons_positions = [index for index in range(len(string)) if string[index] == ":"]
string_len = len(string)

for emo_index in emoticons_positions:
    if emo_index != string_len - 1:
        print(string[emo_index:emo_index + 2])
