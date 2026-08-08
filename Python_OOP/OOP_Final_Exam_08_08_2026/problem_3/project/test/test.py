from project.legendary_item import LegendaryItem
from unittest import TestCase, main


class TestLegendaryItem(TestCase):
    def setUp(self):
        self.legendary_item = LegendaryItem("123-456", 100, 10, 1000)

    def test_init(self):
        self.assertEqual(self.legendary_item.identifier, "123-456")
        self.assertEqual(self.legendary_item.power, 100)
        self.assertEqual(self.legendary_item.durability, 10)
        self.assertEqual(self.legendary_item.price, 1000)

    def test_get_identifier(self):
        self.assertEqual(self.legendary_item.identifier, "123-456")

    def test_set_identifier_with_non_numeric_values(self):
        self.assertEqual(self.legendary_item.identifier, "123-456")
        with self.assertRaises(ValueError) as ex:
            self.legendary_item.identifier = "f@oo-123"
        self.assertEqual(str(ex.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_set_identifier_with_less_than_4_characters(self):
        self.assertEqual(self.legendary_item.identifier, "123-456")
        with self.assertRaises(ValueError) as ex:
            self.legendary_item.identifier = "abc"
        self.assertEqual(str(ex.exception), "Identifier must be at least 4 characters long!")

    def test_set_identifier_with_correct_values(self):
        self.assertEqual(self.legendary_item.identifier, "123-456")
        self.legendary_item.identifier = "123-45678"
        self.assertEqual(self.legendary_item.identifier, "123-45678")

    def test_get_power(self):
        self.assertEqual(self.legendary_item.power, 100)

    def test_set_power_with_incorrect_values(self):
        self.assertEqual(self.legendary_item.power, 100)
        with self.assertRaises(ValueError) as ex:
            self.legendary_item.power = -1
        self.assertEqual(str(ex.exception), "Power must be a non-negative integer!")

    def test_set_power_with_correct_value(self):
        self.assertEqual(self.legendary_item.power, 100)
        self.legendary_item.power = 50
        self.assertEqual(self.legendary_item.power, 50)

    def test_get_durability(self):
        self.assertEqual(self.legendary_item.durability, 10)

    def test_set_durability_with_incorrect_values(self):
        self.assertEqual(self.legendary_item.durability, 10)
        with self.assertRaises(ValueError) as ex:
            self.legendary_item.durability = 0
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

        with self.assertRaises(ValueError) as ex:
            self.legendary_item.durability = 101
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

    def test_get_price(self):
        self.assertEqual(self.legendary_item.price, 1000)

    def test_set_price_with_incorrect_values(self):
        self.assertEqual(self.legendary_item.price, 1000)
        with self.assertRaises(ValueError) as ex:
            self.legendary_item.price = 0
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

        with self.assertRaises(ValueError) as ex:
            self.legendary_item.price = 15
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

        with self.assertRaises(ValueError) as ex:
            self.legendary_item.price = 11
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

    def test_set_price_with_correct_value(self):
        self.assertEqual(self.legendary_item.price, 1000)
        self.legendary_item.price = 50
        self.assertEqual(self.legendary_item.price, 50)
        self.legendary_item.price = 100
        self.assertEqual(self.legendary_item.price, 100)

    def test_is_precious(self):
        self.assertEqual(self.legendary_item.power, 100)
        self.assertTrue(self.legendary_item.is_precious)
        self.legendary_item.power = 50
        self.assertTrue(self.legendary_item.is_precious)
        self.legendary_item.power = 49
        self.assertFalse(self.legendary_item.is_precious)

    def test_enhance(self):
        self.assertEqual(self.legendary_item.power, 100)
        self.assertEqual(self.legendary_item.price, 1000)
        self.assertEqual(self.legendary_item.durability, 10)
        self.legendary_item.enhance()
        self.assertEqual(self.legendary_item.power, 200)
        self.assertEqual(self.legendary_item.price, 1010)
        self.assertEqual(self.legendary_item.durability, 20)
        self.legendary_item.durability = 100
        self.assertEqual(self.legendary_item.durability, 100)
        self.legendary_item.enhance()
        self.assertEqual(self.legendary_item.power, 400)
        self.assertEqual(self.legendary_item.price, 1020)
        self.assertEqual(self.legendary_item.durability, 100)

    def test_evaluate(self):
        self.assertEqual(self.legendary_item.durability, 10)
        self.assertEqual(self.legendary_item.power, 100)
        result = self.legendary_item.evaluate(10)
        self.assertEqual(result, f"{self.legendary_item.identifier} is eligible.")
        self.legendary_item.durability = 20
        self.assertEqual(self.legendary_item.durability, 20)
        result = self.legendary_item.evaluate(10)
        self.assertEqual(result, f"{self.legendary_item.identifier} is eligible.")
        result = self.legendary_item.evaluate(100)
        self.assertEqual(result, f"Item not eligible.")
        self.legendary_item.power = 49
        self.assertEqual(self.legendary_item.power, 49)
        result = self.legendary_item.evaluate(10)
        self.assertEqual(result, f"Item not eligible.")


if __name__ == '__main__':
    main()
