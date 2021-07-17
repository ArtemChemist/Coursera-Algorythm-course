import Assign2_Functions    # The code to test
import unittest   # The test framework
import random



class TestFastOne(unittest.TestCase):
    def test_twonumbers(self):
        n = random.randint(2,5)
        randomlist = random.sample(range(0, 10), n)
        result = True
        while result:
            result = self.assertEqual(Assign2_Functions.PairwiseProductFast(randomlist), Assign2_Functions.PairwiseProduct(randomlist))
            print(result)
