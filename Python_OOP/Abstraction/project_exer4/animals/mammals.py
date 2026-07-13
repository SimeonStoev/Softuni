from project_exer4.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in ("Vegetable", "Fruit"):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity
        return None


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity
        return None


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in ("Vegetable", "Meat"):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity
        return None


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity
        return None
