import Assign2_Functions    # The code to test
import unittest   # The test framework
import random



class TestFastOne(unittest.TestCase):
    def test_twonumbers(self):
        n = random.randint(2,11)
        randomlist = random.sample(range(0, 99999), n)
        print(randomlist)
        self.assertEqual(Assign2_Functions.PairwiseProductFast(randomlist), Assign2_Functions.PairwiseProduct(randomlist))

