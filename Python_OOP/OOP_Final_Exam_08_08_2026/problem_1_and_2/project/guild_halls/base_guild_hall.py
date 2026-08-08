from abc import ABC, abstractmethod


class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members = []

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        value_not_valid = len(value.strip()) < 2
        if not value_not_valid:
            for word in value.split():
                if not word.isalpha():
                    value_not_valid = True
                    break
        if value_not_valid:
            raise ValueError("Guild hall alias is invalid!")
        self._alias = value

    def calculate_total_gold(self):
        return sum(member.gold for member in self.members)

    def status(self):
        sorted_members = sorted(self.members, key=lambda member: member.tag)
        return f"Guild hall: {self.alias}; Members: {' *'.join(member.tag for member in sorted_members) if self.members else 'N/A'}; Total gold: {self.calculate_total_gold()}"

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass
