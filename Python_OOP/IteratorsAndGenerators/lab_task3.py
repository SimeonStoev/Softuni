class vowels:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text):
        self.text = text
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.text):
            if self.text[self.current].lower() in self.vowels:
                return self.text[self.current]
            else:
                return self.__next__()
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
