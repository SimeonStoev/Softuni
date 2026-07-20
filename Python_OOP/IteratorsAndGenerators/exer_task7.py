def read_next(*args):
    for iter_obj in args:
        yield from iter_obj


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
