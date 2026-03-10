class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        animals_for_species = []
        species_formated = species.title()
        if species == 'mammal':
            animals_for_species = self.mammals
            species_formated += "s"
        elif species == 'fish':
            animals_for_species = self.fishes
            species_formated += "es"
        else:
            animals_for_species = self.birds
            species_formated += "s"


        return f"{species_formated} in {self.name}: {', '.join(animals_for_species)}\nTotal animals: {self.__animals}"


zoo_name = input()
number_of_animals = int(input())
zoo = Zoo(zoo_name)
for _ in range(number_of_animals):
    animal_data = input().split()
    species = animal_data[0]
    name = animal_data[1]
    zoo.add_animal(species, name)

species_search = input()
print(zoo.get_info(species_search))