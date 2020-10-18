import unittest
from LowestCommonAncestry import findLCA, root

class TestLowestCommonAncestry(unittest.TestCase):


  def test_4_5(self):
      self.assertAlmostEqual(findLCA(root,4,5), 2)

  def test_5_10(self):
      self.assertAlmostEqual(findLCA(root,5,10), 2)

  def test_negative_input(self):
      self.assertAlmostEqual(findLCA(root,-2,5), -1)
      self.assertAlmostEqual(findLCA(root,7,-10), -1)
      self.assertAlmostEqual(findLCA(root,-4,-7), -1)

  def test_greater_input(self):
      self.assertAlmostEqual(findLCA(root,11,5), -1)
      self.assertAlmostEqual(findLCA(root,7,15), -1)
      self.assertAlmostEqual(findLCA(root,30,24), -1)

  def test_zero_input(self):
      self.assertAlmostEqual(findLCA(root,0,4), -1)
      self.assertAlmostEqual(findLCA(root,7,0), -1)
      self.assertAlmostEqual(findLCA(root,0,0), -1)
