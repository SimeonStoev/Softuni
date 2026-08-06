from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def create_loan(self, loan_type: str):
        return self.VALID_LOANS[loan_type]()

    def create_client(self, client_type: str, client_name: str, client_id: str, income: float):
        return self.VALID_CLIENTS[client_type](client_name, client_id, income)

    def has_enough_capacity(self):
        return len(self.clients) < self.capacity

    def get_client(self, client_id: str):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def get_first_possible_loan_by_type(self, loan_type: str):
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                return loan
        return None

    @staticmethod
    def is_loan_for_correct_client(client: BaseClient, loan_type: str):
        if isinstance(client, Student) and loan_type == "StudentLoan":
            return True
        if isinstance(client, Adult) and loan_type == "MortgageLoan":
            return True
        return False

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS.keys():
            raise ValueError("Invalid loan type!")

        new_loan = self.create_loan(loan_type)
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise ValueError("Invalid client type!")

        if not self.has_enough_capacity():
            return "Not enough bank capacity."

        new_client = self.create_client(client_type, client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.get_client(client_id)
        loan = self.get_first_possible_loan_by_type(loan_type)

        if not self.is_loan_for_correct_client(client, loan_type):
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.get_client(client_id)
        if not client:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans_count = 0
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans_count += 1

        return f"Successfully changed {changed_loans_count} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients_count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients_count += 1

        return f"Number of clients affected: {changed_clients_count}."

    def get_statistics(self):
        total_clients_income = sum(client.income for client in self.clients)
        total_loans_granted = sum(len(client.loans) for client in self.clients)
        total_sum_of_granted_loans = sum(loan.amount for client in self.clients for loan in client.loans)
        total_not_granted_loans = len(self.loans)
        total_sum_for_not_granted_loans = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = sum(client.interest for client in self.clients) / len(self.clients) if len(
            self.clients) > 0 else 0
        lines = [f"Active Clients: {len(self.clients)}",
                 f"Total Income: {total_clients_income:.2f}",
                 f"Granted Loans: {total_loans_granted}, Total Sum: {total_sum_of_granted_loans:.2f}",
                 f"Available Loans: {total_not_granted_loans}, Total Sum: {total_sum_for_not_granted_loans:.2f}",
                 f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"]

        return "\n".join(lines).strip()
