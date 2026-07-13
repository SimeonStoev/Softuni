from project_exer4.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity
        return None


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
