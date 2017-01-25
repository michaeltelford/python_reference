import unittest
import sys; sys.path.append("src")
import mod

class TestMod(unittest.TestCase):
  
  def setUp(self):
    pass
    
  def test_add(self):
    self.assertEqual(5, mod.add(3, 2))
    
if __name__ == "__main__":
  unittest.main()
