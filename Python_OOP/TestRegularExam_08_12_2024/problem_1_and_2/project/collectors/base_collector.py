from abc import ABC, abstractmethod
import re


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r"^[A-Za-z0-9]+(\s[A-Za-z0-9]+)*$"
        if not re.match(pattern, value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        return self.available_money >= artifact_price and self.available_space >= artifact_space_required

    def __str__(self):
        artifacts = ', '.join(
            [artifact.name for artifact in sorted(self.purchased_artifacts, key=lambda x: x.name,
                                                  reverse=True)]) if self.purchased_artifacts else 'none'
        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: {artifacts}"
