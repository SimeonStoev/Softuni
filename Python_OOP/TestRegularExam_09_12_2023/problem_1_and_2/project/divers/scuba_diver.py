from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        new_oxygen_level = round(self.oxygen_level - (time_to_catch * 0.3))
        if new_oxygen_level < 0:
            new_oxygen_level = 0
        self.oxygen_level = new_oxygen_level

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.OXYGEN_LEVEL
