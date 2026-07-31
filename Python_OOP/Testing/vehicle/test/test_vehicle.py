from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 90)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.horse_power, 90)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_more_km_with_less_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_refuel_with_more_than_needed_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_correctly(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 47.5)

    def test_string_representation_of_vehicle(self):
        self.assertEqual(str(self.vehicle),
                         "The vehicle has 90 horse power with 50 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    main()
