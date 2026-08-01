from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        if len(model) < 3 or len(model.strip()) == 0:
            raise ValueError("Product model must be at least 3 chars long!")
        self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            raise ValueError("Product price must be greater than zero!")
        self.__price = price

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material: str):
        self.__material = material

    @property
    def sub_type(self):
        return self.__sub_type

    @sub_type.setter
    def sub_type(self, sub_type: str):
        self.__sub_type = sub_type

    @abstractmethod
    def discount(self):
        pass
