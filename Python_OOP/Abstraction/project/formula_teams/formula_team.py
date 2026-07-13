from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.__budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos):
        pass
