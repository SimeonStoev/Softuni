import unittest
from collections import deque
from exer_task_9 import simulate_bullet_lock


class TestBulletLockSimulation(unittest.TestCase):

    def all_locks_unlocked_with_bullets_remaining(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = [3, 2, 1]
        locks = deque([1, 2])
        value_of_intelligence = 10
        expected = ["Bang!", "Bang!", "1 bullets left. Earned $7"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def all_locks_unlocked_no_bullets_remaining(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = [3, 2]
        locks = deque([2, 3])
        value_of_intelligence = 10
        expected = ["Bang!", "Bang!", "0 bullets left. Earned $8"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def locks_remaining_bullets_exhausted(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = [1, 1]
        locks = deque([2, 3])
        value_of_intelligence = 10
        expected = ["Ping!", "Ping!", "Couldn't get through. Locks left: 2"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def single_bullet_single_lock_unlocked(self):
        bullet_price = 1
        gun_barrel = 1
        bullets = [5]
        locks = deque([4])
        value_of_intelligence = 10
        expected = ["Bang!", "0 bullets left. Earned $9"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def single_bullet_single_lock_failed(self):
        bullet_price = 1
        gun_barrel = 1
        bullets = [3]
        locks = deque([4])
        value_of_intelligence = 10
        expected = ["Ping!", "Couldn't get through. Locks left: 1"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def reloading_occurs(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = [3, 2, 1, 4]
        locks = deque([1, 2, 3])
        value_of_intelligence = 20
        expected = ["Bang!", "Bang!", "Reloading!", "Bang!", "1 bullets left. Earned $16"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def no_locks(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = [3, 2]
        locks = deque([])
        value_of_intelligence = 10
        expected = ["2 bullets left. Earned $10"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def no_bullets(self):
        bullet_price = 1
        gun_barrel = 2
        bullets = []
        locks = deque([1, 2])
        value_of_intelligence = 10
        expected = ["Couldn't get through. Locks left: 2"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)

    def bullets_exactly_match_locks_no_reloading(self):
        bullet_price = 1
        gun_barrel = 3
        bullets = [3, 2, 1]
        locks = deque([1, 2, 3])
        value_of_intelligence = 10
        expected = ["Bang!", "Bang!", "Bang!", "0 bullets left. Earned $7"]
        self.assertEqual(simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence), expected)


if __name__ == '__main__':
    unittest.main()
