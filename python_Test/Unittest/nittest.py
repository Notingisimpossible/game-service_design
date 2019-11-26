import unittest
from test import tests
from test import product

class Unitetest(unittest.TestCase):
  def testunit(self):
    """测试tests"""
    pows = tests(8)
    self.assertEquals(pows, 64)

  def testP(self):
    """测试乘积"""
    cj = product(6,9)
    self.assertEquals(cj, 54)

unittest.main()