import unittest
from unittest import TestCase
from sixth_challenge import ListChanger


class TestListChanger(TestCase):

    def setUp(self):
        self._list_changer_obj_1 = ListChanger([1, 2, 3, 4, 5, 6, 6])
        self._list_changer_obj_2 = ListChanger(["CA", "FL", "MC", "NY"])
        self._list_changer_obj_3 = ListChanger([True, False, True, False])

    def test_reverse_list(self):
        result = self._list_changer_obj_1.reverse_list()
        self.assertEqual(result, [6, 6, 5, 4, 3, 2, 1])

    def test_has_duplicates(self):
        result = self._list_changer_obj_1.has_duplicates()
        self.assertEqual(result, True)
        result1 =  self._list_changer_obj_2.has_duplicates()
        self.assertEqual(result1, False)

    @unittest.skip ("testing to skip")
    def test_smallest_number(self):
        result = self._list_changer_obj_1.smallest_number()
        self.assertEqual(result, 1)
        result1 = self._list_changer_obj_3.smallest_number()
        self.assertEqual(result1, False)
    def test_greatest_number(self):
        result = self._list_changer_obj_1.greatest_number()
        self.assertEqual(result, 6)

    def test_second_greatest_number(self):
        result = self._list_changer_obj_1.second_greatest_number()
        self.assertEqual(result, 5)

    def test_remove_first_and_last(self):
        result = self._list_changer_obj_1.remove_first_and_last()
        self.assertEqual(result, [2, 3, 4, 5, 6])

    def tearDown(self):
        self._list_changer_obj_1 = None
        self._list_changer_obj_2 = None
        self._list_changer_obj_3 = None