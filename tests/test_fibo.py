import time
import unittest
from fibo import FiboSequence


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._fibo_seq = FiboSequence()
        self._efficiency_data = dict()

    def test_recursive_method(self):
        starting_time = time.time()
        self._fibo_seq.recursive_method(25)
        ending_time = time.time()

        self._efficiency_data['recursive_method'] = ending_time - starting_time

    def test_math_method(self):
        starting_time = time.time()
        self._fibo_seq.math_method(25)
        ending_time = time.time()

        self._efficiency_data['math_method'] = ending_time - starting_time

    def tearDown(self):
        print(self._efficiency_data)
        self._fibo_seq = None
        self._efficiency_data.clear()
