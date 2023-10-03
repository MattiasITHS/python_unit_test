import unittest
from car_challenge import Car


class EasyTestCase(unittest.TestCase):
        def setUp(self):
            self.car = Car()
            self.car.start_car()
        def test_easy_inputs(self):
            self.car.add_speed()
            self.car.add_speed()
            self.car.add_speed()
            self.car.add_speed()
            self.assertEquals(self.car.current_speed(), 20)


        def test_easy_inputs_two(self):
            self.car.add_speed()
            self.car.add_speed()
            self.car.stop()
            self.assertEquals(self.car.current_speed(), 0)

        def tearDown(self):
            self.car.stop()
            self.car.turn_off_car()
            self.car = None


class MedTestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_med_inputs(self):
        with self.assertRaises(Exception):
            self.car.start_car()

    def test_med_inputs_two(self):
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEquals(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None

class HardTestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_inputs(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.car.stop()
        self.car.stop()
        self.assertEquals(self.car.current_speed(), 0)

    def test_hard_inputs_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEquals(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None
