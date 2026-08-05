from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


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

    def get_diver_by_name(self, diver_name: str):
        return next(diver for diver in self.divers if diver.name == diver_name)

    def get_fish_by_name(self, fish_name: str):
        return next(fish for fish in self.fish_list if fish.name == fish_name)

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

    def catch_fish_logic(self, diver, fish, is_lucky):
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver.name} missed a good {fish.name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                # diver oxygen_level = 0
                diver.has_health_issue = True
                return f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver.name} missed a good {fish.name}."

        diver.hit(fish)
        return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        if not self.is_diver_already_exists(diver_name):
            return f"{diver_name} is not registered for the competition."

        if not self.is_fish_already_exists(fish_name):
            return f"The {fish_name} is not allowed to be caught in this competition."

        diver = self.get_diver_by_name(diver_name)
        fish = self.get_fish_by_name(fish_name)

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        return self.catch_fish_logic(diver, fish, is_lucky)

    def health_recovery(self):
        divers_recovered_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                divers_recovered_count += 1
                diver.has_health_issue = False
                diver.renew_oxy()
        return f"Divers recovered: {divers_recovered_count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_diver_by_name(diver_name)
        if not diver:
            return
        lines = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            lines.append(fish.fish_details())

        return "\n".join(lines).strip()

    def competition_statistics(self):
        selected_divers = [diver for diver in
                           sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)) if
                           not diver.has_health_issue]
        lines = ["**Nautical Catch Challenge Statistics**"]

        for diver in selected_divers:
            lines.append(str(diver))

        return "\n".join(lines).strip()
