import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # --- 10 Test Cases ที่เพิ่มเข้ามา ---

    #add()
    def test_add_negatives(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(10, -5), 5)

    #subtract()
    def test_subtract_positives(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    #multiply()
    def test_multiply_positives(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative_b(self):
        self.assertEqual(self.calc.multiply(3, -7), -21)

    #divide()
    def test_divide_positives(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_b(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    #modulo()
    def test_modulo_positives(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_negative_b(self):
        self.assertEqual(self.calc.modulo(10, -3), 1)


if __name__ == '__main__':
    unittest.main()