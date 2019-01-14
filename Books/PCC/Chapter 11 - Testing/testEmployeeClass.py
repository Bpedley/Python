import unittest
from employeeClass import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        self.emp = Employee('Egor', 'Kuchin', 10000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 60000)

    def test_give_custom_raise(self):
        self.emp.give_raise(25000)
        self.assertEqual(self.emp.salary, 35000)


unittest.main()