from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    ARTIFACT_TYPES = ("RenaissanceArtifact", "ContemporaryArtifact")
    COLLECTOR_TYPES = ("Museum", "PrivateCollector")

    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def is_artifact_with_same_name_in_collection(self, artifact_name: str):
        return any(artifact.name == artifact_name for artifact in self.artifacts)

    def is_collector_with_same_name_in_collection(self, collector_name: str):
        return any(collector.name == collector_name for collector in self.collectors)

    def get_collector(self, collector_name: str):
        return [collector for collector in self.collectors if collector.name == collector_name][0]

    def get_artifact(self, artifact_name: str):
        return [artifact for artifact in self.artifacts if artifact.name == artifact_name][0]

    @staticmethod
    def create_artifact(artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type == "RenaissanceArtifact":
            return RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
        else:
            return ContemporaryArtifact(artifact_name, artifact_price, artifact_space)

    @staticmethod
    def create_collector(collector_type: str, collector_name: str):
        if collector_type == "Museum":
            return Museum(collector_name)
        else:
            return PrivateCollector(collector_name)

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.ARTIFACT_TYPES:
            raise ValueError("Unknown artifact type!")

        if self.is_artifact_with_same_name_in_collection(artifact_name):
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact = self.create_artifact(artifact_type, artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.COLLECTOR_TYPES:
            raise ValueError("Unknown collector type!")

        if self.is_collector_with_same_name_in_collection(collector_name):
            raise ValueError(f"{collector_name} has been already registered!")

        collector = self.create_collector(collector_type, collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        if not self.is_collector_with_same_name_in_collection(collector_name):
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if not self.is_artifact_with_same_name_in_collection(artifact_name):
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        collector = self.get_collector(collector_name)
        artifact = self.get_artifact(artifact_name)

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        if not self.is_artifact_with_same_name_in_collection(artifact_name):
            return "No such artifact."

        artifact = self.get_artifact(artifact_name)
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        fundraising_collectors = [collector.increase_money() for collector in self.collectors if
                                  collector.available_money <= max_money]
        return f"{len(fundraising_collectors)} collector/s increased their available money."

    def get_auction_report(self):
        sorted_collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))
        all_sold_artifacts_count = sum([len(artifact.purchased_artifacts) for artifact in sorted_collectors])
        all_unsold_artifacts_count = len(self.artifacts)
        lines = ["**Auction statistics**",
                 f"Total number of sold artifacts: {all_sold_artifacts_count}",
                 f"Available artifacts for sale: {all_unsold_artifacts_count}",
                 "***"]
        for collector in sorted_collectors:
            lines.append(str(collector))
        return "\n".join(lines).strip()
