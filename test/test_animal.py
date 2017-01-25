import unittest
import sys; sys.path.append("src")
from animal import Animal

class TestAnimal(unittest.TestCase):
  
  def setUp(self):
    self.animal = Animal("Fido", 3)
    
  def test_speak(self):
    self.assertEqual("Fido!!", self.animal.speak())
    
if __name__ == "__main__":
  unittest.main()
