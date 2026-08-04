from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish

predatory_fish = PredatoryFish("test",  10)

print(predatory_fish.fish_details())

deep_sea_fish = DeepSeaFish("test", 10)
print(deep_sea_fish.fish_details())