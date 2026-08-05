from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.my_car = SecondHandCar("Toyota", "Corolla", 200000, 5000.0)
        self.other_car = SecondHandCar("Mercedes", "GLE", 500000, 15000.0)

    def test_init(self):
        self.assertEqual(self.my_car.model, "Toyota")
        self.assertEqual(self.my_car.car_type, "Corolla")
        self.assertEqual(self.my_car.price, 5000.0)
        self.assertEqual(self.my_car.mileage, 200000)
        self.assertEqual(self.my_car.repairs, [])

    def test_get_price(self):
        self.assertEqual(self.my_car.price, 5000.0)

    def test_set_price_with_incorrect_value(self):
        with self.assertRaises(ValueError) as ex:
            self.my_car.price = 1.0
        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

        with self.assertRaises(ValueError) as ex:
            self.my_car.price = 0.9
        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_set_price_with_correct_value(self):
        self.assertEqual(self.my_car.price, 5000.0)
        self.my_car.price = 6000.0
        self.assertEqual(self.my_car.price, 6000.0)

    def test_get_mileage(self):
        self.assertEqual(self.my_car.mileage, 200000)

    def test_set_mileage_with_incorrect_value(self):
        with self.assertRaises(ValueError) as ex:
            self.my_car.mileage = 100
        self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

        with self.assertRaises(ValueError) as ex:
            self.my_car.mileage = 99
        self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_set_mileage_with_correct_value(self):
        self.assertEqual(self.my_car.mileage, 200000)
        self.my_car.mileage = 150000
        self.assertEqual(self.my_car.mileage, 150000)

    def test_set_promotional_price_higher_than_current_price_raise(self):
        self.assertEqual(self.my_car.price, 5000.0)
        with self.assertRaises(ValueError) as ex:
            self.my_car.set_promotional_price(10000.0)
        self.assertEqual(str(ex.exception), "You are supposed to decrease the price!")

        with self.assertRaises(ValueError) as ex:
            self.my_car.set_promotional_price(5000.0)
        self.assertEqual(str(ex.exception), "You are supposed to decrease the price!")

    def test_set_promotional_price_lower_than_current_price(self):
        self.assertEqual(self.my_car.price, 5000.0)
        result = self.my_car.set_promotional_price(4000.0)
        self.assertEqual(self.my_car.price, 4000.0)
        self.assertEqual(result, "The promotional price has been successfully set.")

    def test_repair_of_car(self):
        self.assertEqual(self.my_car.repairs, [])
        self.assertEqual(self.my_car.price, 5000.0)

        impossible_repair_result = self.my_car.need_repair(3000.0, "Engine repair")
        self.assertEqual(impossible_repair_result, "Repair is impossible!")

        possible_repair_result = self.my_car.need_repair(2500, "Engine repair")
        self.assertEqual(self.my_car.price, 7500)
        self.assertEqual(self.my_car.repairs, ["Engine repair"])
        self.assertEqual(possible_repair_result, "Price has been increased due to repair charges.")

        possible_repair_result = self.my_car.need_repair(1200, "Oil change")
        self.assertEqual(self.my_car.price, 8700)
        self.assertEqual(self.my_car.repairs, ["Engine repair", "Oil change"])
        self.assertEqual(possible_repair_result, "Price has been increased due to repair charges.")

    def test_gt_compare_between_two_cars(self):
        self.assertEqual(self.my_car.car_type, "Corolla")
        self.assertEqual(self.other_car.car_type, "GLE")
        result = self.my_car > self.other_car
        self.assertEqual(result, "Cars cannot be compared. Type mismatch!")
        self.other_car.car_type = "Corolla"
        self.assertEqual(self.other_car.car_type, "Corolla")

        self.assertFalse(self.my_car > self.other_car)
        self.assertTrue(self.other_car > self.my_car)

        self.assertEqual(self.other_car.price, 15000.0)
        self.other_car.price = 5000.0
        self.assertEqual(self.other_car.price, 5000.0)

        self.assertFalse(self.my_car > self.other_car)

    def test_car_str_method(self):
        self.assertEqual(str(self.my_car),
                         "Model Toyota | Type Corolla | Milage 200000km\nCurrent price: 5000.00 | Number of Repairs: 0")
        self.my_car.need_repair(2000, "Engine repair")
        self.assertEqual(str(self.my_car),
                         "Model Toyota | Type Corolla | Milage 200000km\nCurrent price: 7000.00 | Number of Repairs: 1")


if __name__ == '__main__':
    main()
