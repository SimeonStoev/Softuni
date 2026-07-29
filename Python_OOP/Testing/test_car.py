from lab_task4 import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("make", "model", 10, 50)

    def test_init(self):
        self.assertEqual(self.car.make, "make")
        self.assertEqual(self.car.model, "model")
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_init_make_param_null_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_init_model_param_null_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_init_fuel_consumption_zero_or_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_init_fuel_capacity_zero_or_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_ammount_negative_value_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_car_with_invalid_fuel_amount_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_car_with_less_than_max_fuel_ammount(self):
        self.car.refuel(30)
        self.assertEqual(self.car.fuel_amount, 30)

    def test_refuel_car_with_more_than_max_fuel_ammount(self):
        self.car.refuel(60)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive_with_too_long_distance(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(2000)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_normal_distance(self):
        self.car.refuel(50)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 30)


if __name__ == '__main__':
    main()
