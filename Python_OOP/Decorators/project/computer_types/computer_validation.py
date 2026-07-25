class ComputerValidation:
    computer_types = ["Desktop Computer", "Laptop"]

    @staticmethod
    def is_power_of_two(n):
        return (n & (n - 1)) == 0

    @staticmethod
    def validate_computer(computer, processor: str, ram: int):
        computer_type = "desktop computer" if computer.__class__.__name__ == "DesktopComputer" else "laptop"
        if processor not in computer.processors:
            raise ValueError(
                f"{processor} is not compatible with {computer_type} {computer.manufacturer} {computer.model}!")
        if ram < 2 or ram > computer.MAX_RAM or not ComputerValidation.is_power_of_two(ram):
            raise ValueError(
                f"{ram}GB RAM is not compatible with {computer_type} {computer.manufacturer} {computer.model}!")

    @staticmethod
    def validate_computer_type(computer_type: str):
        if computer_type not in ComputerValidation.computer_types:
            raise ValueError(f"{computer_type} is not a valid type computer!")
