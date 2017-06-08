# _*_coding:utf-8 _*_
__author__ = 'lq'

import unittest
import math
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class demoTest(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(3.14,3.14)

    def test2(self):
        self.assertNotAlmostEqual(10.0/3,3)

    def test3(self):
        self.assertGreater(math.pi,3)

    def test4(self):
        self.assertRegexpMatches("Tutorials Point (I) Private Limited","Point")

if __name__ == '__mian__':
    unittest.main()