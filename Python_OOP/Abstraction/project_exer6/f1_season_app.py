from project_exer6.formula_teams.mercedes_team import MercedesTeam
from project_exer6.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def is_team_valid(self, team_name: str) -> bool:
        return team_name in ("Red Bull", "Mercedes")

    def register_team_for_season(self, team_name: str, budget: int):
        if not self.is_team_valid(team_name):
            raise ValueError(f"Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise ValueError("Not all teams have registered for the season.")

        team_with_better_pos = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_rev_mesg = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_rev_mesg = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_rev_mesg}. Mercedes: {mercedes_rev_mesg}. {team_with_better_pos} is ahead at the {race_name} race."
