import math
class Circle:

  def __init__(self,r):
    self.__radius = r
  
  def __area(self):
    return math.pi * self.radius**2
