class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id
        Equipment.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    def __eq__(self, other):
        return self.id == other.id
