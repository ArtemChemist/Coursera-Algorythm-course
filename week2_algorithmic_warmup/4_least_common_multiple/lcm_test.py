import lcm    # The code to test
import unittest   # The test framework
import random

class TestFastOne(unittest.TestCase):
    def test_many(self):
        pasing = True
        run_counter = 0
        while (pasing and (run_counter<100)):
            a = random.randint(0,10**7)
            b = random.randint(0,10**7)
            Fast = lcm.lcm(a, b)
            print("{}'th test: lcm of {} and {} is {}".format(run_counter, a, b, Fast))
            run_counter = run_counter +1
        self.assertLessEqual(Fast, a*b)

    def test_fromexample(self):
        Fast = lcm.lcm(761457, 614573)
        self.assertEqual(Fast, 467970912861)



