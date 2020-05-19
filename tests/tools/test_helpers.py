import sys
sys.path.append('../../src')

import unittest

from tools.helpers import str_convert


class HelpersTest(unittest.TestCase):


    def test_str_convert_bool_arg(self):
        self.assertIsNone(str_convert(True))


    def test_str_convert_int_arg(self):
        self.assertIsNone(str_convert(0))


    def test_str_convert_neg_int_arg(self):
        self.assertIsNone(str_convert(-1))


    def test_str_convert_float_arg(self):
        self.assertIsNone(str_convert(12314.1112334))


    def test_str_convert_empty_str_arg(self):
        res = str_convert('')
        self.assertTrue(isinstance(res, str))
        self.assertEqual(res, '')
    

    def test_str_convert_str_arg(self):
        res = str_convert('Trues')
        self.assertTrue(isinstance(res, str))
        self.assertEqual(res, 'Trues')
    

    def test_str_convert_booltrue_str_arg(self):
        res = str_convert('True')
        self.assertTrue(isinstance(res, bool))
        self.assertTrue(res)


    def test_str_convert_lower_case_bool_str_arg(self):
        res = str_convert('true')
        self.assertTrue(isinstance(res, bool))
        self.assertTrue(res)


    def test_str_convert_capital_true_str_arg(self):
        res = str_convert('TRUE')
        self.assertTrue(isinstance(res, bool))
        self.assertTrue(res)


    def test_str_convert_false_str_arg(self):
        res = str_convert('false')
        self.assertTrue(isinstance(res, bool))
        self.assertFalse(res)


    def test_str_convert_capital_false_str_arg(self):
        res = str_convert('FALSE')
        self.assertTrue(isinstance(res, bool))
        self.assertFalse(res)


    def test_str_convert_pos_int_arg(self):
        res = str_convert('121')
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 121)


    def test_str_convert_zero_int_arg(self):
        res = str_convert('0')
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 0)


    def test_str_convert_neg_int_arg(self):
        res = str_convert('-1')
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, -1)


    def test_str_convert_pos_float_arg(self):
        res = str_convert('0.001')
        self.assertTrue(isinstance(res, float))
        self.assertEqual(res, 0.001)


    def test_str_convert_zero_float_arg(self):
        res = str_convert('0.0')
        self.assertTrue(isinstance(res, float))
        self.assertEqual(res, 0.0)


    def test_str_convert_neg_float_arg(self):
        res = str_convert('-0.01')
        self.assertTrue(isinstance(res, float))
        self.assertEqual(res, -0.01)


if __name__ == '__main__':
    unittest.main()