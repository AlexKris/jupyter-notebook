import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_tony = Employee('tony', 'alex', 30)
        self.custom_salary = 2500

    def test_give_default_raise(self):
        self.employee_tony.give_raise()
        self.assertEqual(5000, self.employee_tony.employee_salary)

    def test_gave_custom_raise(self):
        self.employee_tony.give_raise(self.custom_salary)
        self.assertEqual(2500, self.employee_tony.employee_salary)

if __name__ == '__main__':
    unittest.main()