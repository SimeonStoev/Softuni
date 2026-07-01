class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"

    def __eq__(self, other):
        return self.name == other.name
