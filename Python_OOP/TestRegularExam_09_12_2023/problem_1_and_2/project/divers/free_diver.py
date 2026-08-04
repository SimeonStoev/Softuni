from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        new_oxygen_level = round(self.oxygen_level - (time_to_catch * 0.6))
        if new_oxygen_level < 0:
            new_oxygen_level = 0
        self.oxygen_level = new_oxygen_level

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.OXYGEN_LEVEL
