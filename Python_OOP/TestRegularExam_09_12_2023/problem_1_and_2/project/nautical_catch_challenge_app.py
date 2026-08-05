from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver


class NauticalCatchChallengeApp():
    VALID_DIVER_TYPES = ("FreeDiver", "ScubaDiver")
    VALID_FISH_TYPES = ("PredatoryFish", "DeepSeaFish")

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def is_diver_already_exists(self, diver_name):
        return any(diver for diver in self.divers if diver.name == diver_name)

    def add_diver_to_collection(self, diver_type, diver_name):
        if diver_type == "FreeDiver":
            self.divers.append(FreeDiver(diver_name))
        elif diver_type == "ScubaDiver":
            self.divers.append(ScubaDiver(diver_name))

    def is_fish_already_exists(self, fish_name):
        return any(fish for fish in self.fish_list if fish.name == fish_name)

    def add_fish_to_collection(self, fish_type: str, fish_name: str, points: float):
        if fish_type == "PredatoryFish":
            self.fish_list.append(PredatoryFish(fish_name, points))
        elif fish_type == "DeepSeaFish":
            self.fish_list.append(DeepSeaFish(fish_name, points))

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.is_diver_already_exists(diver_name):
            return f"{diver_name} is already a participant."

        self.add_diver_to_collection(diver_type, diver_name)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.is_fish_already_exists(fish_name):
            return f"{fish_name} is already permitted."

        self.add_fish_to_collection(fish_type, fish_name, points)
        return f"{fish_name} is allowed for chasing as a {fish_type}."
