import unittest
import sys; sys.path.append("src")
from dog import Dog

class TestDog(unittest.TestCase):
  
  def setUp(self):
    self.dog = Dog("Fido")
    
  def test_bark(self):
    self.assertEqual("Fido!!", self.dog.bark())
    
  def test_wag_tail(self):
    self.assertEqual("<tail wagging>...", self.dog.wag_tail())
    
if __name__ == "__main__":
  unittest.main()
