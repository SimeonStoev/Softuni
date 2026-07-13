from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        sponsors_money = 0
        expenses = 200000
        if race_pos == 1:
            sponsors_money = 1000000
        elif race_pos == 3:
            sponsors_money = 500000
        elif race_pos == 5:
            sponsors_money = 100000
        elif race_pos == 7:
            sponsors_money = 50000

        self.budget += sponsors_money - expenses

        return f"The revenue after the race is {sponsors_money - expenses}$. Current budget {self.budget}$"
