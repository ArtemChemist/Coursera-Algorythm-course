import sorting    # The code to test
import unittest   # The test framework
import random



class TestFastOne(unittest.TestCase):
    def test_twonumbers(self):
        length = random.randint(1,1000)
        a_list = []
        for i in range(0, length):
            a_list.append(random.randint(0, length//3))
        print("n = ", length)
        b_list = a_list[:]
        c_list = a_list[:]
        Two = sorting.partition2(b_list, 0, length-1)
        print(Two)
        Three_a, Three_b = sorting.partition3(c_list, 0, length-1)
        print(Three_a, Three_b)
        self.assertEqual(Two, Three_b)


