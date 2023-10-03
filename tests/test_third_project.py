import unittest
from io import StringIO
import sys
from third_project import Profile


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile("Mattias", 35, "Tester")

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), "Mattias")

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), "35")

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), "Tester")

    def tearDown(self):
        self.profile = None

