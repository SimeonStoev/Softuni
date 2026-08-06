from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMMOUNT = 50000.0

    def __init__(self):
        super().__init__(MortgageLoan.INTEREST_RATE, MortgageLoan.AMMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
