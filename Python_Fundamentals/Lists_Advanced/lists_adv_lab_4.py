def is_palindrome(string):
    return string == string[::-1]


str_list = input().split()
palindrome = input()
pal_occur = 0
palyndrome_list = []

for elem in str_list:
    if is_palindrome(elem):
        palyndrome_list.append(elem)
    if elem == palindrome:
        pal_occur += 1

print(palyndrome_list)
print(f"Found palindrome {pal_occur} times")
