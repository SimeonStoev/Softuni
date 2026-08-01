from project.soccer_player import SoccerPlayer

from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.test_player = SoccerPlayer("test name", 20, 15, "Manchester United")

    def test_valid_teams(self):
        self.assertEqual(SoccerPlayer._VALID_TEAMS,
                         ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])

    def test_init(self):
        player = SoccerPlayer("Pedri Rodrigez", 25, 10, "Barcelona")
        self.assertEqual(player.name, "Pedri Rodrigez")
        self.assertEqual(player.age, 25)
        self.assertEqual(player.goals, 10)
        self.assertEqual(player.team, "Barcelona")
        self.assertEqual(player.achievements, {})

    def test_get_name_of_player(self):
        self.assertEqual(self.test_player.name, "test name")

    def test_set_incorrect_player_name_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.test_player.name = "Pedri"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.test_player.name = ""
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_set_correct_player_name(self):
        self.assertEqual(self.test_player.name, "test name")
        self.test_player.name = "Fernando Pedes"
        self.assertEqual(self.test_player.name, "Fernando Pedes")

    def test_get_age(self):
        self.assertEqual(self.test_player.age, 20)

    def test_set_incorrect_age_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.test_player.age = 15
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_set_correct_age(self):
        self.assertEqual(self.test_player.age, 20)
        self.test_player.age = 16
        self.assertEqual(self.test_player.age, 16)

    def test_get_goals(self):
        self.assertEqual(self.test_player.goals, 15)

    def test_set_negative_number_for_goals(self):
        self.assertEqual(self.test_player.goals, 15)
        self.test_player.goals = -15
        self.assertEqual(self.test_player.goals, 0)

    def test_set_goals_more_than_zero(self):
        self.assertEqual(self.test_player.goals, 15)
        self.test_player.goals = 10
        self.assertEqual(self.test_player.goals, 10)

    def test_get_invalid_team(self):
        self.assertEqual(self.test_player.team, "Manchester United")

    def test_set_invalid_team_name_raise(self):
        self.assertEqual(self.test_player.team, "Manchester United")
        with self.assertRaises(ValueError) as ex:
            self.test_player.team = "Test Name"
        self.assertEqual(str(ex.exception),
                         f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!")

    def test_set_valid_team_name(self):
        self.assertEqual(self.test_player.team, "Manchester United")
        self.test_player.team = "Barcelona"
        self.assertEqual(self.test_player.team, "Barcelona")

    def test_change_team_with_invalid_new_team(self):
        self.assertEqual(self.test_player.team, "Manchester United")
        result = self.test_player.change_team("Test Name")
        self.assertEqual(self.test_player.team, "Manchester United")
        self.assertEqual(result, "Invalid team name!")

    def test_change_team_with_valid_new_team(self):
        self.assertEqual(self.test_player.team, "Manchester United")
        result = self.test_player.change_team("Barcelona")
        self.assertEqual(self.test_player.team, "Barcelona")
        self.assertEqual(result, "Team successfully changed!")

    def test_add_new_achievement(self):
        self.assertEqual(self.test_player.achievements, {})
        result = self.test_player.add_new_achievement("Champions league champion")
        self.assertEqual(self.test_player.achievements, {"Champions league champion": 1})
        self.assertEqual(result,
                         f"Champions league champion has been successfully added to the achievements collection!")

        result = self.test_player.add_new_achievement("Champions league champion")
        self.assertEqual(result,
                         f"Champions league champion has been successfully added to the achievements collection!")
        self.assertEqual(self.test_player.achievements, {"Champions league champion": 2})

        result = self.test_player.add_new_achievement("World cup champion")
        self.assertEqual(result, f"World cup champion has been successfully added to the achievements collection!")
        self.assertEqual(self.test_player.achievements, {"Champions league champion": 2, "World cup champion": 1})

    def test_two_player_by_scoring_goals(self):
        player1 = SoccerPlayer("Cristiano Ronaldo", 38, 30, "Manchester United")
        player2 = SoccerPlayer("Lionel Messi", 36, 35, "PSG")
        result1 = player1 < player2
        self.assertEqual(result1, f"{player2.name} is a top goal scorer! S/he scored more than {player1.name}.")
        player2.goals = 25
        result2 = player1 < player2
        self.assertEqual(result2, f"{player1.name} is a better goal scorer than {player2.name}.")


if __name__ == '__main__':
    main()
