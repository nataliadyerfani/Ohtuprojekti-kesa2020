# https://docs.python.org/3.5/library/unittest.html
# https://realpython.com/python-testing/
# run tests with $ python3 -m unittest
# for more verbose output use -v flag

import sys
sys.path.append('../src')
import unittest

from module_totest import calculate_sum


class TestSum(unittest.TestCase):
    def setUp(self):
        # If needed, initialize tests here
        self.testilista = [1, 2, 3]

    def test_sum_list(self):
        '''
        Test with valid integer list
        '''
        self.assertEqual(calculate_sum(self.testilista), 6, 'Should be 6')

    def test_sum_tuple(self):
        '''
        Test with valid integer tuple
        '''
        self.assertEqual(calculate_sum( (0, -2, 3, -2, 0) ), -1, 'Should be -1')

    def test_sum_range(self):
        '''
        Test with range object
        '''
        self.assertEqual(calculate_sum(range(10)), 45, 'Should be 45')



if __name__ == '__main__':
    unittest.main()
