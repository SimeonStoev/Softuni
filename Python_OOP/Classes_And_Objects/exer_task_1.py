class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if len(self.animals) < self.space:
            self.animals.append(animal)
            Vet.animals.append(animal)
            return f"{animal} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            Vet.animals.remove(animal)
            return f"{animal} unregistered successfully"

        return f"{animal} not in the clinic"

    def info(self):
        number_of_animals = len(self.animals)
        left_space = self.space - number_of_animals
        return f"{self.name} has {number_of_animals} animals. {left_space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
