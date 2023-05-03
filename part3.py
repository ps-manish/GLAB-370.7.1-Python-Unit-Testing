import unittest

def square_number(x):
    return x ** 2

class TestSquareNumber(unittest.TestCase):
    def test_square_number(self):
        result = square_number(5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
