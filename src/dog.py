from animal import Animal

class Dog(Animal):
  
  def __init__(self, name, age=0):
    Animal.__init__(self, name, age)
    
  def bark(self):
    return super(Dog, self).speak()

  def wag_tail(self):
    return "<tail wagging>..."