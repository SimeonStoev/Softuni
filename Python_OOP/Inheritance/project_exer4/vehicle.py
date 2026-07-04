class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        curr_fuel_consumption = kilometers * self.fuel_consumption
        if self.fuel >= curr_fuel_consumption:
            self.fuel -= curr_fuel_consumption
