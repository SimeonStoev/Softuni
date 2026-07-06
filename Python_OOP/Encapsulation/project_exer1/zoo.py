from codecs import replace_errors
from itertools import count


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def has_capacity_for_animals(self):
        return self.__animal_capacity > len(self.animals)

    def has_capacity_for_workers(self):
        return self.__workers_capacity > len(self.workers)

    def enough_budget(self, price):
        return self.__budget >= price

    def reduse_budget(self, sum):
        self.__budget -= sum

    def get_worker_if_exists(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                return worker
        return False

    def add_animal(self, animal, price):
        if self.enough_budget(price) and self.has_capacity_for_animals():
            self.animals.append(animal)
            self.reduse_budget(price)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.has_capacity_for_animals() and not self.enough_budget(price):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.has_capacity_for_workers():
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = self.get_worker_if_exists(worker_name)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum(worker.salary for worker in self.workers)
        if self.enough_budget(workers_salaries):
            self.reduse_budget(workers_salaries)
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_money_need = sum(animal.money_for_care for animal in self.animals)
        if self.enough_budget(animals_money_need):
            self.reduse_budget(animals_money_need)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def get_animals_data(self, animal_type):
        result = ""
        for animal in self.animals:
            if type(animal).__name__ == animal_type:
                result += f"{repr(animal)}\n"
        return result

    def get_workers_data(self, worker_type):
        result = ""
        for worker in self.workers:
            if type(worker).__name__ == worker_type:
                result += f"{repr(worker)}\n"
        return result

    def animals_status(self):
        total_animals = len(self.animals)
        total_lions = sum(1 for animal in self.animals if type(animal).__name__ == "Lion")
        total_tigers = sum(1 for animal in self.animals if type(animal).__name__ == "Tiger")
        total_cheetahs = sum(1 for animal in self.animals if type(animal).__name__ == "Cheetah")
        result = f"You have {total_animals} animals\n"
        result += f"----- {total_lions} Lions:\n"
        result += self.get_animals_data(animal_type="Lion")
        result += f"----- {total_tigers} Tigers:\n"
        result += self.get_animals_data(animal_type="Tiger")
        result += f"----- {total_cheetahs} Cheetahs:\n"
        result += self.get_animals_data(animal_type="Cheetah")
        return result.strip()

    def workers_status(self):
        total_workers = len(self.workers)
        total_keepers = sum(1 for worker in self.workers if type(worker).__name__ == "Keeper")
        total_caretakers = sum(1 for worker in self.workers if type(worker).__name__ == "Caretaker")
        total_vets = sum(1 for worker in self.workers if type(worker).__name__ == "Vet")
        result = f"You have {total_workers} workers\n"
        result += f"----- {total_keepers} Keepers:\n"
        result += self.get_workers_data(worker_type="Keeper")
        result += f"----- {total_caretakers} Caretakers:\n"
        result += self.get_workers_data(worker_type="Caretaker")
        result += f"----- {total_vets} Vets:\n"
        result += self.get_workers_data(worker_type="Vet")
        return result.strip()
