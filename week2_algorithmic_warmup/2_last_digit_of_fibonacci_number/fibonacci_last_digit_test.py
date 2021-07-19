import fibonacci_last_digit    # The code to test
import unittest   # The test framework
import random

class TestFastOne(unittest.TestCase):
    def test_many(self):
        pasing = True
        run_counter = 0
        while (pasing and (run_counter<100)):
            n = random.randint(2,10**7)
            Fast = fibonacci_last_digit.get_fibonacci_last_digit_naive(n)
            print(n, Fast)
            run_counter = run_counter +1
        self.assertIn(Fast, range(0,9))

    def test_331(self):
        Fast = fibonacci_last_digit.get_fibonacci_last_digit_naive(331)
        self.assertEqual(Fast, 9)



