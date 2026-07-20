class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current = -1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        self.index += 1
        if self.current == self.number:
            raise StopIteration

        if self.index == len(self.sequence):
            self.index = 0
        return self.sequence[self.index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
