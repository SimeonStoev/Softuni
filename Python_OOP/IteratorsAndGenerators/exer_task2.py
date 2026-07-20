class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.dictionary):
            key = list(self.dictionary.keys())[self.current]
            value = list(self.dictionary.values())[self.current]
            return (key, value)
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
