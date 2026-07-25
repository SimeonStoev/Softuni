from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        if len(manufacturer.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = manufacturer

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        if len(model.strip()) == 0:
            raise ValueError("Model name cannot be empty.")
        self.__model = model

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass
