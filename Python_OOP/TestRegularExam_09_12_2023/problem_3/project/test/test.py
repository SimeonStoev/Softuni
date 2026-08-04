from unittest import TestCase, main
from project.railway_station import RailwayStation

class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway_station = RailwayStation("Dobrich")

    def test_init(self):
        self.assertEqual(self.railway_station.name, "Dobrich")
        self.assertEqual(len(self.railway_station.arrival_trains), 0)
        self.assertEqual(len(self.railway_station.departure_trains), 0)

    def test_get_name(self):
        self.assertEqual(self.railway_station.name, "Dobrich")

    def test_set_name_with_less_than_3_chars_error(self):
        self.assertEqual(self.railway_station.name, "Dobrich")
        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = "Do"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = ""
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_set_name_with_correct_length(self):
        self.assertEqual(self.railway_station.name, "Dobrich")
        self.railway_station.name = "Sofia"
        self.assertEqual(self.railway_station.name, "Sofia")

    def test_new_train_arrival(self):
        self.assertEqual(len(self.railway_station.arrival_trains), 0)
        self.railway_station.new_arrival_on_board("Train 1")
        self.assertEqual(len(self.railway_station.arrival_trains), 1)
        self.assertEqual(self.railway_station.arrival_trains[0], "Train 1")
        self.railway_station.new_arrival_on_board("Train 2")
        self.assertEqual(len(self.railway_station.arrival_trains), 2)
        self.assertEqual(self.railway_station.arrival_trains[1], "Train 2")

    def test_moving_train_from_arrival_to_departure(self):
        self.assertEqual(len(self.railway_station.arrival_trains), 0)
        self.assertEqual(len(self.railway_station.departure_trains), 0)
        self.railway_station.new_arrival_on_board("Train 1")
        self.railway_station.new_arrival_on_board("Train 2")
        self.assertEqual(len(self.railway_station.arrival_trains), 2)
        result = self.railway_station.train_has_arrived("Train 2")
        self.assertEqual(result, "There are other trains to arrive before Train 2.")
        result = self.railway_station.train_has_arrived("Train 1")
        self.assertEqual(result, "Train 1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.railway_station.departure_trains[0], "Train 1")
        result = self.railway_station.train_has_arrived("Train 2")
        self.assertEqual(result, "Train 2 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.railway_station.departure_trains[1], "Train 2")

        with self.assertRaises(IndexError) as ex:
            result = self.railway_station.train_has_arrived("Train 3")
        self.assertEqual(str(ex.exception), "pop from an empty deque")

    def test_train_leaving_the_station(self):
        self.assertEqual(len(self.railway_station.departure_trains), 0)
        self.railway_station.departure_trains.append("Train 1")
        self.railway_station.departure_trains.append("Train 2")
        self.assertEqual(len(self.railway_station.departure_trains), 2)
        self.assertEqual(self.railway_station.departure_trains[0], "Train 1")
        self.assertEqual(self.railway_station.departure_trains[1], "Train 2")

        self.assertFalse(self.railway_station.train_has_left("Train 2"))
        self.assertTrue(self.railway_station.train_has_left("Train 1"))
        self.assertTrue(self.railway_station.train_has_left("Train 2"))
        self.assertFalse(self.railway_station.train_has_left("Train 3"))

        self.assertEqual(len(self.railway_station.departure_trains), 0)

if __name__ == '__main__':
    main()