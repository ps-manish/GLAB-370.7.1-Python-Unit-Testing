import unittest

def divide_numbers(a, b):
    return a / b

class TestDivideNumbers(unittest.TestCase):
    def test_divide_numbers(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(5, 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDivideNumbers)
    test_results = unittest.TextTestRunner(verbosity=2).run(suite)

    if test_results.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
