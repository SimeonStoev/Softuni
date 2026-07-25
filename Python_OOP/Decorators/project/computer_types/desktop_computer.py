import math

from project.computer_types.computer import Computer
from project.computer_types.computer_validation import ComputerValidation


class DesktopComputer(Computer):
    processors = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        # validate input data
        ComputerValidation.validate_computer(self, processor, ram)

        # if validation is ok, continue to set the processor and ram, and calculate the price
        self.processor = processor
        self.ram = ram
        processor_price = self.processors[processor]
        ram_price = int(math.log2(self.ram)) * 100
        self.price = processor_price + ram_price
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
