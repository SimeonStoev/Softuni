class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.items = list(self.dictionary.items())
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
