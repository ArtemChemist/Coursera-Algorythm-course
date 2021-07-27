import change_dp    # The code to test
import unittest   # The test framework
import random



class TestFastOne(unittest.TestCase):
    def test_twonumbers(self):
        m = random.randint(1,1000)
        print(m)
        Result = change_dp.get_change(m)
        print(Result)
        self.assertLessEqual(Result, 3+m//4)


