n = int(input())
snowball_wight = 0
snowball_time = 0
snowball_quality = 0
max_value = 0

for i in range(n):
    curr_snowball_wight = int(input())
    curr_snowball_time = int(input())
    curr_snowball_quality = int(input())
    curr_snowball_value = (curr_snowball_wight // curr_snowball_time) ** curr_snowball_quality
    if curr_snowball_value > max_value:
        max_value = curr_snowball_value
        snowball_wight = curr_snowball_wight
        snowball_time = curr_snowball_time
        snowball_quality = curr_snowball_quality

print(f"{snowball_wight} : {snowball_time} = {max_value} ({snowball_quality})")
