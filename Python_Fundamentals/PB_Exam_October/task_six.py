k = int(input())
l = int(input())
m = int(input())
n = int(input())
number_of_substitutions = 0

for d1 in range(k, 9):
    if d1 % 2 == 0:
        for d2 in range(9, l-1, -1):
            if d2 % 2 != 0:
                for s1 in range(m, 9):
                    if s1 % 2 == 0:
                        for s2 in range(9, n-1, -1):
                            if s2 % 2 != 0 and number_of_substitutions < 6:
                                if d1 == s1 and d2 == s2:
                                    print("Cannot change the same player.")
                                else:
                                    print(f"{d1}{d2} - {s1}{s2}")
                                    number_of_substitutions += 1
