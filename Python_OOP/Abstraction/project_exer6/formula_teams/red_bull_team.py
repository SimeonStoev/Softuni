from project_exer6.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        sponsors_money = 0
        expenses = 250000
        if race_pos == 1:
            sponsors_money += 1500000
        elif race_pos == 2:
            sponsors_money += 800000

        if race_pos <= 8:
            sponsors_money += 20000
        elif race_pos <= 10:
            sponsors_money += 10000

        self.budget += sponsors_money - expenses

        return f"The revenue after the race is {sponsors_money - expenses}$. Current budget {self.budget}$"
