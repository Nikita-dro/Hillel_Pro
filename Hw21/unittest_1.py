import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_valid_inputs(self):
        cases = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
        }

        for input_value, expected_result in cases.items():
            with self.subTest(n=input_value):
                result = self.fibonacci(input_value)
                self.assertEqual(result, expected_result)

    def test_float_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(3.9)

    def test_negative_number_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-15)

    def test_str_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci('34')

    def test_bool_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(bool)

    def test_none_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(None)

    def test_large_input(self):
        result = self.fibonacci(100)
        self.assertEqual(result, 354224848179261915075)

    def test_cache(self):
        self.fibonacci(5)
        self.assertEqual(self.fibonacci.cache, [0, 1, 1, 2, 3, 5])
