import math

class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def get_magnitude(self):
    return math.sqrt((self.x ** 2) + (self.y ** 2))

  def get_angle(self):
    return math.atan2(self.x, self. y)

  
