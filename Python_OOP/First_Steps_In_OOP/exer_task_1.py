class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = [elem for elem in items]

    def get_items_count(self):
        return len(self.items)
