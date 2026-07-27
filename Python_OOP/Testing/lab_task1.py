from multiprocessing.pool import worker


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main

class WorkersTest(TestCase):

    def test_worker_initialization(self):
        worker = Worker(name='Test', salary=20000, energy=100)
        self.assertEqual(worker.name, 'Test')
        self.assertEqual(worker.salary, 20000)
        self.assertEqual(worker.energy, 100)
        self.assertEqual(worker.money, 0)

    def test_worker_energy_below_or_equal_to_zero_raise(self):
        worker = Worker(name='Test', salary=20000, energy=0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

        worker.energy = -1
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_worker_energy_and_money_after_working(self):
        worker = Worker(name='Test', salary=1000, energy=100)
        self.assertEqual(worker.energy, 100)
        self.assertEqual(worker.salary, 1000)

        worker.work()
        self.assertEqual(worker.energy, 99)
        self.assertEqual(worker.money, 1000)
        worker.work()
        self.assertEqual(worker.energy, 98)
        self.assertEqual(worker.money, 2000)

    def test_worker_energy_after_rest(self):
        worker = Worker(name='Test', salary=1000, energy=100)
        self.assertEqual(worker.energy, 100)
        worker.rest()
        self.assertEqual(worker.energy, 101)
        worker.rest()
        self.assertEqual(worker.energy, 102)

    def test_worker_info_message(self):
        worker = Worker(name='Test', salary=1000, energy=100)
        self.assertEqual(worker.get_info(), f"{worker.name} has saved {worker.money} money.")

if __name__ == '__main__':
    main()