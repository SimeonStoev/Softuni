from project.computer_types.computer_validation import ComputerValidation
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def get_wanted_computer(self, client_budget: int, processor: str, ram: int):
        wanted_computer = [comp for comp in self.warehouse if
                           comp.price <= client_budget and comp.processor == processor and comp.ram >= ram]
        return wanted_computer[0] if wanted_computer else None

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        # validate computer type
        ComputerValidation.validate_computer_type(type_computer)

        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)

        config_result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return config_result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_to_sell = self.get_wanted_computer(client_budget, wanted_processor, wanted_ram)
        if not computer_to_sell:
            raise Exception("Sorry, we don't have a computer for you.")

        self.warehouse.remove(computer_to_sell)
        self.profits += (client_budget - computer_to_sell.price)
        return f"{computer_to_sell} sold for {client_budget}$."
