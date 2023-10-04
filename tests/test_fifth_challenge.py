import unittest
import time
from fifth_challenge import EfficiencyAdding

class TestAddingMethods(unittest.TestCase):

    def setUp(self):
        self._effi_adding = EfficiencyAdding()
        self._effi_data = dict()
    def test_first_adding_method(self):
        starting_time = time.time()
        self._effi_adding.adding_two_first_method(50000000)
        ending_time = time.time()
        self._effi_data['first method'] = ending_time - starting_time
    def test_second_adding_method(self):
        starting_time = time.time()
        self._effi_adding.adding_two_second_method(50000000)
        ending_time = time.time()
        self._effi_data['second method'] = ending_time - starting_time
    def tearDown(self):
        print(self._effi_data)
        self._effi_adding = None
        self._effi_data.clear()

if __name__ == '__main__':
    unittest.main()