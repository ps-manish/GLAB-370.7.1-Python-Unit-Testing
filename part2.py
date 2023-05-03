import unittest

def multiply_numbers(a, b):
    return a * b

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_numbers(self):
        result = multiply_numbers(3, 5)
        self.assertEqual(result, 15)

    def test_multiply_negative_numbers(self):
        result = multiply_numbers(-4, 5)
        self.assertEqual(result, -20)

    def test_multiply_zero(self):
        result = multiply_numbers(2, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiplyNumbers)
    unittest.TextTestRunner(verbosity=2).run(suite)
