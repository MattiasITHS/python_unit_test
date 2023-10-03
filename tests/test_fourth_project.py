import unittest
import sys
from io import StringIO
from fourth_project import Printer


class PrintTest(unittest.TestCase):

    def setUp(self):
        self.help, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_input(self):
        self.printer.set_value("Hej")
        self.printer.print_value()
        self.assertEquals(sys.stdout.getvalue().strip(), "Hej")

    def test_input_job(self):
        self.printer.set_value("Tester")
        self.printer.print_value()
        self.assertEquals(sys.stdout.getvalue().strip(), "Tester")

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
