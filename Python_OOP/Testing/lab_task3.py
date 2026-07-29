class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main

class TestIntegerList(TestCase):
    def setUp(self):
        self.list1 = IntegerList(1, 2, 3, 'a', 'b', 'c')

    def test_init(self):
        self.assertEqual(self.list1.get_data(), [1, 2, 3])

    def test_add_with_error_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.list1.add("a")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_add_with_correct_data(self):
        self.list1.add(4)
        self.assertEqual(self.list1.get_data(), [1, 2, 3, 4])
        self.list1.add(5)
        self.assertEqual(self.list1.get_data(), [1, 2, 3, 4, 5])

    def test_remove_index_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list1.remove_index(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove_index_with_correct_index(self):
        el1 = self.list1.remove_index(2)
        self.assertEqual(el1, 3)
        self.assertEqual(self.list1.get_data(), [1, 2])
        el2 = self.list1.remove_index(1)
        self.assertEqual(el2, 2)
        self.assertEqual(self.list1.get_data(), [1])

    def test_get_element_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list1.get(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_element_with_correct_index(self):
        el1 = self.list1.get(2)
        self.assertEqual(el1, 3)
        el2 = self.list1.get(0)
        self.assertEqual(el2, 1)

    def test_insert_element_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list1.insert(3, 6)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_element_with_element_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.list1.insert(1, "a")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_insert_element_at_index_with_correct_data(self):
        self.list1.insert(1, 4)
        self.assertEqual(self.list1.get_data(), [1, 4, 2, 3])
        self.list1.insert(0, 5)
        self.assertEqual(self.list1.get_data(), [5, 1, 4, 2, 3])

    def test_get_biggest_element_from_list(self):
        max_element = max(self.list1.get_data())
        self.assertEqual(max_element, self.list1.get_biggest())

    def test_get_index_of_element(self):
        index = self.list1.get_index(1)
        self.assertEqual(index, 0)

if __name__ == '__main__':
    main()