from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Jumbo", "Elephant", "UUU")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Jumbo")
        self.assertEqual(self.mammal.type, "Elephant")
        self.assertEqual(self.mammal.sound, "UUU")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Jumbo makes UUU")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_get_info(self):
        self.assertEqual(self.mammal.info(), "Jumbo is of type Elephant")

    def test_kingdom_is_private(self):
        # __kingdom е name-mangled, не трябва да е достъпен директно
        with self.assertRaises(AttributeError):
            test = self.mammal.__kingdom

    def test_different_instance_values(self):
        cat = Mammal("Cat", "Feline", "Meow")
        self.assertEqual(cat.make_sound(), "Cat makes Meow")
        self.assertEqual(cat.info(), "Cat is of type Feline")
        self.assertEqual(cat.get_kingdom(), "animals")


if __name__ == '__main__':
    main()
