class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health = 0 if self.health < damage else self.health - damage

        if self.health == 0:
            return f"{self.name} was defeated"

        return

    def heal(self, ammount):
        self.health += ammount
