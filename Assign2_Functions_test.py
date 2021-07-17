import Assign2_Functions    # The code to test
import unittest   # The test framework
import random



class TestFastOne(unittest.TestCase):
    def test_twonumbers(self):
        pasing = True
        run_counter = 0
        while (pasing and (run_counter<100)):
            n = random.randint(2,8)
            randomlist = random.sample(range(0, 9), n)
            print(randomlist)
            Fast = Assign2_Functions.PairwiseProductFast(randomlist)
            Furious = Assign2_Functions.PairwiseProduct(randomlist)
            print('Fast: {}; Furious: {}; count: {}'.format(Fast, Furious, run_counter))
            pasing = (Fast == Furious)
            run_counter = run_counter +1
        self.assertEqual(Fast, Furious)


