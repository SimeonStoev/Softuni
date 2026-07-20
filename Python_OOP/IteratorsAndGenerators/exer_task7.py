def read_next(*args):
    for iter_obj in args:
        for item in iter_obj:
            yield item


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
