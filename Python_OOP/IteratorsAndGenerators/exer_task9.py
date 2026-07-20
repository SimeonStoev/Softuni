import itertools


def possible_permutations(list_values):
    for perm in itertools.permutations(list_values):
        yield list(perm)


[print(n) for n in possible_permutations([1])]
