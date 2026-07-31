from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("hero", 1, health=100, damage=60)
        self.opponent = Hero("opponent", 1, health=100, damage=50)

    def test_init(self):
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 60)
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.username, "hero")

    def test_str_representation(self):
        self.assertEqual(str(self.hero), "Hero hero: 1 lvl\nHealth: 100\nDamage: 60\n")

    # Test battle method
    def test_battle_with_yourself_raise(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_hero_is_with_zero_or_negative_health_raise(self):
        with self.assertRaises(Exception) as ex:
            self.hero.health = 0
            self.hero.battle(self.opponent)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

        with self.assertRaises(Exception) as ex:
            self.opponent.health = -1
            self.hero.battle(self.opponent)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_opponent_is_with_zero_or_negative_health_raise(self):
        with self.assertRaises(Exception) as ex:
            self.opponent.health = 0
            self.hero.battle(self.opponent)
        self.assertEqual(str(ex.exception), f"You cannot fight {self.opponent.username}. He needs to rest")

        with self.assertRaises(Exception) as ex:
            self.opponent.health = -1
            self.hero.battle(self.opponent)
        self.assertEqual(str(ex.exception), f"You cannot fight {self.opponent.username}. He needs to rest")

    def test_battle_with_draw_result_and_health_zero(self):
        self.hero.damage = 100
        self.opponent.damage = 100
        self.assertEqual(self.hero.battle(self.opponent), "Draw")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.opponent.health, 0)

    def test_battle_with_draw_result_and_health_negative(self):
        self.hero.damage = 101
        self.opponent.damage = 101
        self.assertEqual(self.hero.battle(self.opponent), "Draw")
        self.assertEqual(self.hero.health, -1)
        self.assertEqual(self.opponent.health, -1)

    def test_battle_with_opponent_and_win(self):
        self.hero.damage = 110
        self.opponent.damage = 90
        self.assertEqual(self.hero.battle(self.opponent), "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 15)
        self.assertEqual(self.hero.damage, 115)

    def test_battle_with_opponent_and_lose(self):
        self.hero.damage = 90
        self.opponent.damage = 110
        self.assertEqual(self.hero.battle(self.opponent), "You lose")
        self.assertEqual(self.opponent.level, 2)
        self.assertEqual(self.opponent.health, 15)
        self.assertEqual(self.opponent.damage, 115)
    # End tests


if __name__ == '__main__':
    main()
