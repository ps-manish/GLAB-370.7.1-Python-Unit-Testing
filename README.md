# GLAB-370.7.1-Python-Unit-Testing


## Part 1


```
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

```

In this code, we define a function called 'add_numbers' that takes two parameters a and b and returns their sum. We also define a unit test class called TestAddNumbers that inherits from unittest.TestCase and has a single test method called test_add_numbers that checks the result of the add_numbers function for two input values 3 and 5. We use the assertEqual assertion to check that the result of the function is equal to 8. Finally, we use the unittest.main() function to run the test and observe the results.


## Part 2

```
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
```
In this code, we define a function called multiply_numbers that takes two parameters a and b and returns their product. We also define a unit test class called TestMultiplyNumbers that inherits from unittest.TestCase. We have three test methods in this class, each of which checks the result of the multiply_numbers function for different input values.

In test_multiply_numbers, we check the result of multiplying 3 and 5, which should be 15. In test_multiply_negative_numbers, we check the result of multiplying -4 and 5, which should be -20. In test_multiply_zero, we check the result of multiplying 2 and 0, which should be 0.

We use the assertEqual assertion to check the results of the multiplication in each test method. Finally, we use the TestLoader and TextTestRunner classes from the unittest module to run the test suite and generate a test report with verbosity level 2.


## Part 3

```
import unittest

def square_number(x):
    return x ** 2

class TestSquareNumber(unittest.TestCase):
    def test_square_number(self):
        result = square_number(5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()

```

In this code, we define a function called square_number that takes one parameter x and returns the square of that number. We also define a unit test class called TestSquareNumber that inherits from unittest.TestCase and has a single test method called test_square_number that checks the result of the square_number function for the input value 5.

We use the assertEqual assertion to check that the result of the function is equal to 25. Finally, we use the unittest.main() function to run the test and observe that it fails.

To implement the square_number function, we simply need to change its implementation to:

```
def square_number(x):
    return x ** 2
```

We can then run the test again and observe that it passes.


## Part 4

```
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
```

In this code, we define a function called divide_numbers that takes two parameters a and b and returns the result of dividing a by b. We also define a unit test class called TestDivideNumbers that inherits from unittest.TestCase. We have two test methods in this class, test_divide_numbers and test_divide_by_zero.

In test_divide_numbers, we check the result of dividing 10 by 2, which should be 5. In test_divide_by_zero, we use the assertRaises assertion to check that a ZeroDivisionError is raised when dividing by 0.

We use the TestLoader and TextTestRunner classes from the unittest module to run the test suite and generate a test report with verbosity level 2. We also check whether all tests passed or if some tests failed by using the wasSuccessful() method of the TextTestResult object returned by TextTestRunner.

When we run this code, we should see a test report printed to the console, along with the message "All tests passed!" or "Some tests failed." depending on the outcome of the tests.


