#_*_ coding:utf-8 _*_
__author__ = 'lq'

import unittest
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test3(self):
        self.assertTrue(4 + 5 == 9,"The result is False")

    def test5(self):
        self.assertIn(3,[1,2,3])

    def test6(self):
        self.assertIn(3,range(5))

if __name__ == '__main__':
    unittest.main()

