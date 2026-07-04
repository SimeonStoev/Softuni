class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        self.quantity = self.quantity - quantity if self.quantity >= quantity else self.quantity

    def increase(self, quantity):
        self.quantity += quantity

    def __repr__(self):
        return self.name
