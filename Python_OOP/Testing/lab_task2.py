class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

from unittest import TestCase, main

class CatTests(TestCase):
    def test_cat_size_increase(self):
        cat = Cat('cat')
        self.assertEqual(cat.name, 'cat')
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(cat.size, 0)
        cat.eat()

        self.assertEqual(cat.size, 1)

        cat.fed = False

        cat.eat()
        self.assertEqual(cat.size, 2)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('cat')
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_after_being_fed(self):
        cat = Cat('cat')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        cat = Cat('cat')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('cat')
        self.assertFalse(cat.sleepy)
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)

if __name__ == '__main__':
    main()