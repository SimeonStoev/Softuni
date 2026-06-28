class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return False
        return self.name == other.name and self.health == other.health
